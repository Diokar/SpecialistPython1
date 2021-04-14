# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

a = int(input("a= "))
b = int(input("b= ",))

def palindrome(number):
    return str(number) == str(number)[::-1]
S=0
s=0
while a<=b:
    S = palindrome(a)
    #print('Число ',a ,S)
    if S == True: s+=1
    a +=1
print("Количество палиндромов",s )
