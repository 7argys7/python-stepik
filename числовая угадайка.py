from random import *


def is_valid(n, grant):
    if 1 <= n <= grant:
        return True
    else:
        return False


print("Введите границу для случайного выбора")
n = int(input())
attempt = 0
again = "да"
print("Добро пожаловать в числовую угадайку")

while again == "да":
    num = randint(1, n)
    print("Введите число:")
    while True:
        digit = int(input())
        print(num)
        if is_valid(digit, n) == False:
            print(f"А может быть все-таки введем целое число от 1 до {n}?")
            continue
        if digit < num:
            print("Ваше число меньше загаданного, попробуйте еще рзаок")
            attempt += 1
        elif digit > num:
            print("Ваше число больше загаданного, попробуйте еще разок")
            attempt += 1
        else:
            print("Вы угадали, поздравляем!")
            print("Количество попыток:", attempt)
            break
    attempt = 0
    print("Хотите сыграть ище раз?(да или нет)")
    again = input().lower()
    if again == "нет":
        break
    print("Хотите поменять границу для случайного выбора?(да или нет)")
    gran = input().lower()
    if gran == "да":
        print("Введите границу для случайного выбора")
        n = int(input())


print("Спасибо, что играли в числовую угадайку. Еще увидимся")
