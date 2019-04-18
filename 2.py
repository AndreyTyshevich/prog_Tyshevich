import argparse
import sys

parser = argparse.ArgumentParser(description='Калькулятор')

parser.add_argument(
    # название поля в объекте, где будут сохранены параметры
    'values',
    # название параметров, которое будет отображено в справке
    metavar='VALUES',
    type=float,
    # параметров будет не меньше одного
    nargs='+',
    # краткое описание параметров
    help='входная последовательность чисел')

parser.add_argument(
    # короткое название опции
    '-a',
    # длинное название опции
    '--action',
    # парсер сохранит значение True, если встретит эту опцию
    action='append',
    type=str,
    choices=["+", "-", "*", "/"],
    # краткое описание опции
    help='арифметические действия')

parser.add_argument(
    # короткое название опции
    '-v',
    # длинное название опции
    '--verbose',
    # название параметра, которое будет отображено в справке
    metavar='VALUE',
    type=float,
    # парсер сохранит значение параметра, если встретит эту опцию
    action='store',
    # краткое описание опции
    help='игнорировать числа, не превышающие указанное')

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
