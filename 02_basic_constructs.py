# ============================
# 2.1 Часть 1
# ============================

# --- Задача 1: На easy ---
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print((a ** 10 + b ** 10) ** 0.5)

#  --- Задача 2: Индекс массы тела  ---
mass = float(input())
height = float(input())
IMT = mass / (height ** 2)
if 18.5 <= IMT <= 25:
    print("Оптимальная масса")
elif IMT <= 18.5:
    print("Недостаточная масса")
else:
    print("Избыточная масса")

#  --- Задача 3: Стоимость строки ---
string = input()
lenstr = len(string) * 60
print(f'{lenstr // 100} р. {lenstr % 100} коп.')

#  --- Задача 4: количество слов ---
string = input().split()
print(len(string))

#  --- Задача 5: Зодиак ---
year = (int(input()) + 4) % 12
zodiak = [
    "Дракон",
    "Змея",
    "Лошадь",
    "Овца",
    "Обезьяна",
    "Петух",
    "Собака",
    "Свинья",
    "Крыса",
    "Бык",
    "Тигр",
    "Заяц",
]
print(zodiak[year])

#  --- Задача 6: Переворот числа ---
digit = input()
if len(digit) == 5:
    print(int(digit[::-1]))
else:    
    print(int(digit[0] + digit[:0:-1]))

#  --- Задача 7: Stanard American Convention ---
digit = [i for i in input()]
digit.reverse()
cnt = 0
for i in range(3, len(digit) , 3):
    digit.insert(i + cnt, ",")
    cnt += 1
digit.reverse()
print("".join(digit))

#  --- Задача 8: Задача Иосифа Флавия ---
n = int(input())
k = int(input())
live = [i for i in range(1, n + 1)]
new_live = []
while len(live) != 1:
    idx = (k - 1) % len(live)
    new_live += live[:idx]
    del live[:idx + 1]
    live += new_live
    new_live = []
    
print(*live)
    


