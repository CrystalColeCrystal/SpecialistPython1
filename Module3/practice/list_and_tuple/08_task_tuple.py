# Даны примеры создания кортежей.
# Выясните, какие из них являются корректными.
# Все некорректные объявления и создающие не котрежи закомментируйте (#)
tup1 = (2, 4, -6)
tup2 = (2, "Василия", -6)
tup3 = 2, 4, -6
tup4 = (2) #<class 'int'>
tup5 = (2,)
tup6 = 2,
tup7 = tuple([2, 4, -6, 12])
tup8 = tuple(2, 7, 8, -5) # tuple expected at most 1 argument, got 4
tup9 = tuple()
tup10 = tuple("hello")
tup11 = ()
tup12 = 2 and #<class 'int'>
