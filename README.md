# plex-reanalyze
a script for analyzing Plex media

The Plex scanner can crash when processing a large number of media, such as a photo library. This script queries for all media in a given library, skips any that is not in the requested album, and requests each item be individually analyzed.


# requirements

- python-plexapi
- requests

The current release of python-plexapi does not include photo library support, so you must install from source.


# installation

```sh
# clone plex-reanalyze
git clone https://github.com/fracai/plex-reanalyze

# create a python virtual environment
cd plex-reanalyze
virtualenv venv

# clone python-plexapi
git clone https://github.com/mjs7231/python-plexapi

# optionally checkout the latest commit that I've tested this with
# git checkout 5701af7ed40bac952992820ee57706f037bd7e74

# activate the virtual environment
. venv/bin/activate

# install PlexAPI
cd python-plexapi
python setup.py install

# try out the script
cd ..
./plex-reanalyze.py -h
```


# examples

Re-analyze just the photos taken on 1 Jan 2015 (presuming your photos are arranged into dated folders).

`plex-reanalyze --baseurl http://plex-server:32400 --library Photos --prefix 2015/01/01`

Just print the matching media items; don't actually request the analysis.

`plex-reanalyze --baseurl http://plex-server:32400 --library Photos --prefix 2015/01/01 --dry-run`
