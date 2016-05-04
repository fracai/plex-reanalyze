#!/usr/bin/env python

import argparse

from plexapi.server import PlexServer
from requests import put as PUT


def analyze_item(server, key):
    server.query('/library/metadata/%s/analyze' % key, method=PUT)


def process_album(server, album, prefix_path=[], depth=0, dryrun=False):
    if prefix_path and album.title != prefix_path[0]:
        return
    print multi_str('\t', depth) + 'album: ' + album.title
    for item in album.photos():
        if item.TYPE == 'photo':
            print multi_str('\t', depth + 1) + 'photo: ' + item.title
            if not dryrun:
                analyze_item(server, item.ratingKey)
        elif item.TYPE == 'photoalbum':
            process_album(server, item, prefix_path[1:] if prefix_path else None, depth=depth + 1, dryrun=dryrun)


def multi_str(string, count):
    output = ''
    for _ in range(count):
        output += string
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reanalyze plex media items')
    parser.add_argument('-b', '--baseurl', dest='baseurl',
                        help='base url to be used when connecting to Plex')
    parser.add_argument('-l', '--library', dest='library',
                        help='media library to examine')
    parser.add_argument('-p', '--prefix', dest='prefix',
                        help='folder path that should be scanned')
    parser.add_argument('-n', '--dry-run', dest='dryrun', action='store_true', default=False,
                        help='don\'t analyze anything, just print the matching items')

    args = parser.parse_args()

    plex = PlexServer(baseurl=args.baseurl)
    library = plex.library.section(args.library)

    if args.prefix:
        prefix = args.prefix.split('/')
    else:
        prefix = None

    for album in library.all():
        process_album(plex, album, prefix, dryrun=args.dryrun)
