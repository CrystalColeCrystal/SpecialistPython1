# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def palindrome(number):
    lst=[]
    while number>0:
        lst.append(number%10)
        number=number//10
    for i in range(0, int(len(lst)/2)):
        if lst[i]!=lst[len(lst)-i-1]:
            return "NO"
    return "YES"

print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
