# #Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# #number = int(input('Введите число >0: '))
# your_number=number
# summa=0
#
# if number<0:
#     print("Не соблюдено условие. Введите число >0.")
#
# while number>0:
#     ost = number%10
#     summa+= ost
#     number//=10
# print(f"сумма цифр числа {your_number} равна {summa}")

# #Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# #n = int(input("Введите число больше 1: "))
# list_numbers=[i for i in range(1,n)]
# print(list_numbers)
# sum_numbers = []
# multi=1
# for number in list_numbers:
#     multi=multi*number
#     sum_numbers.append(multi)
# print(sum_numbers)

# #Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#
# Пример:
#
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


# #numbers = []
# for n in range(1, 7):
#     number = (1+1/n)**n
#     numbers.append(number)
#
# print(numbers)



#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# #print("Задан список чисел от -3 до 3: ")
# numbers = [-3,-2,-1,0,1,2,3]
# print(numbers)
# filename='numbers.txt'
# indexes=[]
# with open('numbers.txt') as file_object:
#     for line in file_object:
#         indexes.append(int(line.rstrip()))
# index_1=indexes[0]
# index_2=indexes[1]
#
# product = numbers[index_1] * numbers[index_2]
# print(f'Произведение чисел из списка {numbers} на позициях, указанных в numbers.txt(2,4) равно {product}')





#Реализуйте алгоритм перемешивания списка.

import random
base_list=[1,2,3,4,5,6]
new_list=[]
print(f"Изначальный список чисел: {base_list}")
new_list = random.sample(base_list,len(base_list))
print(f"Новый перемешаный список:{new_list}")


