"""Напишите программу, которая запрашивает у пользователя число N и выводит первые N чисел Фибоначчи. Числа Фибоначчи -
это последовательность чисел, где каждое следующее число является суммой двух предыдущих чисел (начиная с 0 и 1).
Используйте цикл while для решения задачи.
Выведите числа через запятую с помощью команды print.

Пример вывода:

Введите число N: 7

Первые 7 чисел Фибоначчи: 0,  1, 1, 2, 3, 5, 8

"""

N = 1

result = f"Последовательность Фибоначчи для {N} элементов: "
n_2, n_1 = 0, 1
count = 2
while N >= count:
    result += str(n_2) + ', '
    n = n_2 + n_1
    n_2, n_1 = n_1, n
    count += 1
else:
    result += str(n_2)
print(result)

