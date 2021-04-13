# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
from random import randint
numbers = []
n = int(input("число n: "))
list = []
for el in range(n):
    list.append(randint(-100,100))
print(list)
#Сформировали список со случайными числами

s=0
for el in list:
    if el > 0:
        s = s + el

print(s)
