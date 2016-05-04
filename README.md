# plex-reanalyze
a script for analyzing Plex media

The Plex scanner can crash when processing a large number of media, such as a photo library. This script queries for all media in a given library, skips any that is not in the requested album, and requests each item be individually analyzed.

# examples

Re-analyze just the photos taken on 1 Jan 2015 (presuming your photos are arranged into dated folders).

`plex-reanalyze --baseurl http://plex-server:32400 --library Photos --prefix 2015/01/01`

Just print the matching media items; don't actually request the analysis.

`plex-reanalyze --baseurl http://plex-server:32400 --library Photos --prefix 2015/01/01 --dry-run`
