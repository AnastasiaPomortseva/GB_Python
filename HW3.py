# #Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# #numbers = [2,6,4,2,7,9]
# print(numbers)
# i = 0
# n=len(numbers)
# sum_numbers = 0
# for i in range(n):
#     if i % 2 != 0:
#         sum_numbers = sum_numbers + numbers[i]
#         i += 1
#
# print(f"Сумма элементов списка, стоящих на нечетной позиции: {sum_numbers}")

#############################################

# #Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];

# #from random import randint
#
# number = int(input("Введите размер списка: "))
# numbers = []
# new_numbers = []
# result = 0
# i = 0
#
# for i in range(number):
#     numbers.append(randint(0, number))
# for i in range(len(numbers)):
#     while i<len(numbers)/2 and number>len(numbers)/2:
#         number=number - 1
#         result = numbers[i] * numbers[number]
#         new_numbers.append(result)
#         i += 1
#
#
# print(numbers)
# print(new_numbers)
#
#
##########################################

# #Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# #list= [1.1, 1.5, 10.05, 3.4, 5.7]
# i=0
# base_max=0
# base_min=list[0]%1
# result=0
# for i in range(len(list)):
#     if list[i]%1 > base_max:
#          base_max=list[i]%1
#
#     if list[i]%1 < base_min:
#         base_min = list[i]%1
# result=base_max - base_min
#
# print(base_min)
# print(base_max)
# print(result)


#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

from random import randint

# number = int(input("Введите число: "))
# n=number
# def get_fibonacci(n):
#     fibonacci_list = []
#     a, b = 1, 1
#     for i in range(n - 1):
#         fibonacci_list.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range(n):
#         fibonacci_list.insert(0, a)
#         a, b = b, a - b
#     return fibonacci_list
#
# fibonacci_list = get_fibonacci(n)
# print(fibonacci_list)

#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def convert_to(number,base):
    new_number=''
    ost='01'
    while number >0:
        new_number=ost[number%base]+new_number
        number //= base
    return new_number

print(convert_to(100, 2))


