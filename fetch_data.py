# fetch 2018 data
from urllib import urlretrieve
from glob import glob
import tarfile
from os import mkdir

DL_PATH = 'raw'
FINAL = 'data'

base = 'https://snakedown-2018-snapshots-battlesnake-io.storage.googleapis.com'
fmt = 'games_2018-%02d-%02d.json.tar.gz'

# just packing some data in here so we fetch all the files
sets = {
        1: [19, 31],
        2: [1, 28],
        3: [1,31],
        4: [1,3]}

def download():
    for month,v in sets.items():
        day = v[0]
        last = v[1]

        while day <= last:
            fname = fmt % (month, day)
            print " > fetching: %s" % fname
            urlretrieve('%s/%s' % (base, fname), '%s/%s' % (DL_PATH, fname))
            day += 1

def extract():
    for fname in glob("%s/games_2018*.tar.gz" % DL_PATH):
        with tarfile.open(fname) as tar:
            first = fname.split('/')[-1]
            out = '%s/%s' % (FINAL, first)
            mkdir(out)
            print '> extracting: %s' % fname
            tar.extractall(out)

