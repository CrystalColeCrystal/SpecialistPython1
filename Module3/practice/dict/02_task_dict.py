# Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря.


# TODO: your code here
# Нужно получить словарь:
# {'name': 'Петр', 'surname': 'Первый', 'age': 42, 'rate': 1300}

keys = ['name', 'surname', 'age', 'rate']
values = ['Петр', 'Первый', 42, 1300]
dictionary = dict()
for key, value in zip(keys, values):
    dictionary[key] = value
print(dictionary)
