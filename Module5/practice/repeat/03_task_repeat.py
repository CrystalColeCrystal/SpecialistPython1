# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.


def palindrome(number):
    return str(number)==str(number)[::-1]
a=int(input("a = "))
b=int(input("b = "))
s=list(range(a,b+1))
i=0
for el in s:
    i+=palindrome(el)
print(i)
