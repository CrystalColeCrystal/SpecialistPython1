# Дано вещественное число x. Проверьте, является ли оно положительным или отрицательным.
# Формат входных данных: дано одно вещественное число number. Гарантируется, что number ≠ 0.
# Формат выходных данных: Требуется вывести тип числа текстом
number=float(input("Введите вещественное число, не равное 0: "))
if number>0:
    print("Число положительное")
else:
    print("Число отрицательное")
