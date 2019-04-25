# импортируем модуль
import sys

for arg in sys.argv[1:]:
    f = open(arg)
    print(f.read())
