# 2.	Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

a = int(input("введите кординаты X: "))
b = int(input("введите кординаты Y: "))

if a > 0 and b > 0:
    print("1 четверть")
elif a < 0 and b < 0:
    print("3 четверть")
elif a > 0 and b < 0:
    print("4 четверть")
elif a < 0 and b > 0:
    print("2 четверть")
else:
    print("Вы на кординатных осях")
