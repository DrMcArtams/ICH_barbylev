"""Напишите программу, которая запрашивает у пользователя три числа
и проверяет, являются ли они уникальными (не повторяются).
Выведите соответствующее сообщение на экран с помощью команды print.
Используйте операторы сравнения и логические операторы для решения задачи.

Пример вывода:

Введите первое число: 5
Введите второе число: 10
Введите третье число: 5

Числа не являются уникальными.
"""
print("Введите три целых числа:")
a, b, c = input(), input(), input()

if a == b or c == b or a == c:
    print("Числа не являются уникальными.")
