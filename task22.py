# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random
n = int(input("enter number of elements for set n: "))
m = int(input("enter number of elements for set m: "))
list_n = [random.randint(0,100) for i in range (int(n))]
set_n = set(list_n)
list_m = [random.randint(0,100) for i in range (int(m))]
set_m = set(list_m)
print (set_n)
print (set_m)
new_set = set_n.union(set_m)
print(sorted(new_set))
