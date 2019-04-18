# импортируем модуль
import sys

# выводим на экран список всех аргументов
n = 0
for arg in sys.argv:
    if len(arg)%3 == 0:
        n += 1
print(n)
