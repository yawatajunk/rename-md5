#!/usr/bin/env python

import os
import sys


def rename(filepath):
    import hashlib

    try:
        f = open(filepath, 'rb')
    except IOError:
        return 1

    data = f.read()
    hash = hashlib.md5(data).hexdigest()

    dirname = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    _, ext = os.path.splitext(filename)
    new_filepath = os.path.join(dirname, hash + ext)

    os.rename(filepath, new_filepath)
    return 0


if __name__ == '__main__':
    import argparse as ap

    parser = ap.ArgumentParser(description='Rename a file with its MD5 hash')
    parser.add_argument('filename', type=str, help='file name to be renamed')
    args = parser.parse_args()
    res = rename(args.filename)
    sys.exit(res)
