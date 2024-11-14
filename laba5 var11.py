# вар.11
# задание №1
import math

xtr = float(input('введите вес снаряда в кг: '))
a = 60
v = 35
g = 9.81
if xtr < 0:
    print('вес снаряда не может быть отрицательный')
else:
    y = xtr * math.tan(a) + ((g * xtr ** 2) / (2 * v ** 2 * math.cos(a) ** 2))
    print(round((y), 2))

# # задание №2

a = float(input('Введите первое положительное число, выше 0 (большее): '))
b = float(input('Введите второе положительное число, выше 0 (меньшее): '))

if a <= 0 or b <= 0:
    print('Вы не выполнили условия')
elif a > b:
    while a >= b:
        a -= b
    if a < 0:
        print(round((a + b), 4))
    else:
        print(round((a), 4))
else:
    print('Вы не выполнили условия')

# задание №3

x0 = float(input('Введите начальную точку (меньшую): '))
x1 = float(input('Введите конечную точку (большую): '))
dx = float(input('Введите шаг (больше 0): '))
x = x0

while x < x1:
    if dx <= 0:
        print('Вы не выполнили условие')
        break
    elif x < 0:
        z = x ** 2
    elif 0 < x <= 1:
        z = math.sin(x)
    else:
        z = math.cos(x)
    print(f'Ответ {round((x + dx), 4)}: {z}')
    x += dx
if x0 > x1:
        print('Вы не выполнили условие')