# 1.	Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

numberDay = int(input("ВВедите число от 1 до 7: "))

if numberDay == 1 or numberDay == 2 or numberDay == 3 or numberDay == 4 or numberDay == 5:
        print("День недели  не выходной")
elif numberDay == (6 or 7):
        print("День недели выходной")
else:
        print("Сказали же ввести число от 1 до 7")