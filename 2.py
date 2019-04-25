import argparse
import sys

parser = argparse.ArgumentParser(description='Calculus')

parser.add_argument(
    'values',
    metavar='VALUES',
    type=float,
    nargs='+',
    help='row of numbers')

parser.add_argument(
    '-a',
    '--action',
    action='append',
    type=str,
    choices=["+", "-", "*", "/"],
    help='arithmetics')

parser.add_argument(
    '-v',
    '--verbose',
    metavar='VALUE',
    type=float,
    action='store',
    help='ignore nubers dreater than this')

args = parser.parse_args()
values = args.values

v1 = values[0]
v2 = values[1]

sum_ = v1 + v2
diff_ = v1 - v2
pr_ = v1 * v2
div_ = v1 / v2


if '+' in args.action:
    print(sum_)

if '-' in args.action:
    print(diff_)

if '*'  in args.action:
    print(pr_)

if '/' in args.action:
    print(div_)
