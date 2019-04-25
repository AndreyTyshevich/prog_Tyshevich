import sys
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path',
                    metavar='PATH',
                    type=str)
parser.add_argument('-fo',
                    '--folders_only',
                    help='exclude files from the tree',
                    action='store_true')
parser.add_argument('-fn',
                    '--full_name',
                    help='show full path',
                    action='store_true')
args = parser.parse_args()
path = args.path


def get_name_of_it(path, obj):
    if args.full_name:
        print(os.path.join(path, obj))
    else:
        print(obj)


def recur(path):
    for obj in os.listdir(path):
        if args.folders_only:
            if not os.path.isfile(os.path.join(path, obj)):
                get_name_of_it(path, obj)
        else:
            get_name_of_it(path, obj)

        obj = os.path.join(path, obj)
        if os.path.isdir(obj):
            recur(obj)


recur(path)
