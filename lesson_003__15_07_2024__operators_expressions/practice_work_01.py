"""n школьников делят k яблок поровну,
неделящийся остаток остаётся в корзинке.
Сколько яблок достанется каждому школьнику?
Сколько яблок останется в корзинке?
Программа получает на вход числа n и k
и должна вывести искомое количество яблок (два числа).

"""
n = 3
k = 7

print("Сколько яблок достанется каждому школьнику?", k // n)
print("Сколько яблок останется в корзинке?", k % n)
