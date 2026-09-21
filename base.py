'''
import math

x = float(input("Введите x: "))
eps = float(input("Введите eps: "))

term = 1.0
total = term
n = 0
while abs(term) >= eps:
    n += 1
    term *= x / n
    total += term

exact = math.exp(x)

print("\n--- Результаты ---")
print(f"x = {x}")
print(f"eps = {eps}")
print(f"Приближённое значение (ряд Тейлора): {total:.15f}")
print(f"Стандартное значение math.exp(x):    {exact:.15f}")
print(f"Абсолютная погрешность:              {abs(total - exact):.3e}")
print(f"Относительная погрешность:           {abs(total - exact) / abs(exact):.3e}")
print(f"Учтено слагаемых:                    {n + 1}")
print(f"Последнее учтённое слагаемое:        {term:.3e}")
'''
import math
x = float(input("Input x "))
if abs(x) >= 1:
    print("bad user")
eps = float(input("Input e "))

exact = math.atan(x)
print(f"Стандартное значение math.exp(x):    {exact:.15f}")

result = x
buf = x
n = 1
while abs(buf) > eps:
    buf *= (-1)*x * x * (2 * n - 1)/(2*n + 1)
    n += 1
    result += buf
print(f"My variant {result:.15f}")