# Дан треугольник со сторонами a, b и c. Определите, является ли он равнобедренным.
# Формат входных данных: дано три натуральных числа. Гарантируется, что отрезки с данными длинами образуют треугольник.
# Формат выходных данных: Выведите «YES», если треугольник равнобедренный, и «NO» в противном случае.


a=int(input("Введите длину 1й стороны треугольника: "))
b=int(input("Введите длину 2й стороны треугольника: "))
c=int(input("Введите длину 3й стороны треугольника: "))
if a==b or b==c or a==c:
    print("YES")
else:
    print("NO")
