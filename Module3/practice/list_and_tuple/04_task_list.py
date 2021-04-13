# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
my_list = [0, 10, 2, 1, -12]
summ = 0
summ1 = 0
i = 0
for summ in my_list:
    if summ > 0:
        summ1 = summ1 + summ


print(summ1)
