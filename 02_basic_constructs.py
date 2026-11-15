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


# ============================
# 2.2 Часть 2
# ============================

#  --- Задача 1: Кординатные четверти ---
n = int(input())
quarter_1 = 0
quarter_2 = 0
quarter_3 = 0
quarter_4 = 0

for i in range(n):
    coord = input().split()
    x = int(coord[0])
    y = int(coord[1])
    if  x > 0 and y > 0:
        quarter_1 += 1
    elif x < 0 and y > 0:
        quarter_2 += 1
    elif x < 0 and y < 0:
        quarter_3 += 1
    elif x > 0 and y < 0:
        quarter_4 += 1

print("Первая четверть:", quarter_1)
print("Вторая четверть:", quarter_2)
print("Третья четверть:", quarter_3)
print("Четвертая четверть:", quarter_4)

#  --- Задача 2: Больше предыдущего ---
n = input().split()
count = 0

for i in range(1, len(n)):
    if int(n[i - 1]) < int(n[i]):
        count += 1

print(count)
#  --- Задача 3: Назад, вперед и наоборот ---

n = input().split()
for i in range(1, len(n)):
    if len(n) % 2 == 1 and i == len(n) - 1:
        continue
    if i % 2 == 0:
        continue
    n[i - 1], n[i] = n[i], n[i - 1]
print(*n)

#  --- Задача 4: Сдвиг в развитии ---

n = input().split()
n_ins = n.insert(0, n[-1])
del n[-1]
print(*n)

#  --- Задача 5: Различные элементы ---
