"""Напишите программу, которая запрашивает у пользователя
натуральное десятичное число и выводит его двоичное представление.
Реализуйте алгоритм перевода числа в двоичную систему счисления,
используя основные концепции представления чисел
(подсказка: через деление с остатком).
Выведите полученное представление числа на экран.
"""

n = 6
n_bin = ''
while n > 0:
    n_bin = str(n % 2) + n_bin
    n //= 2
print(n_bin)
