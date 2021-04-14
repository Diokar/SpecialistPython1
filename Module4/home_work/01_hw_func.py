# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    a = sum(map(int,str(ticket_number%1000)))
    b = sum(map(int,str(ticket_number//1000)))
    if a == b:
        return (True)


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
