print("Выберите направление: шифрование или дешифрование(1 или 2)")
variant = int(input())
if variant != 1 and variant != 2:
    while variant != 1 and variant != 2:
        print("вы ввели неверное число повторите попытку")
        variant = int(input())
print("Выберите язык: русский или английский (1 или 2)")
language = int(input())
if language != 1 and language != 2:
    while language != 1 and language != 2:
        print("вы ввели неверное число повторите попытку")
        language = int(input())
print("Укажите шаг здвига:")
k = int(input())
print("Введите текст")
text = input()


def shif_cher_rus(k):
    shif_text = ""
    for i in text:
        if i.isupper():      
            shif_text += chr(((ord(i) - 1040 + k) % 32) + 1040)
        elif i.islower():
            shif_text += chr(((ord(i) - 1072 + k) % 32) + 1072)
        else:
            shif_text += i
    return shif_text


def shif_cher_eng(k):
    shif_text = ""
    for i in text:
        if i.isupper():
            shif_text += chr(((ord(i) - 65 + k) % 26) + 65)
        elif i.islower():
            shif_text += chr(((ord(i) - 97 + k) % 26) + 97)
        else:
            shif_text += i
    return shif_text


def reshif_cher_rus(k):
    reshif_text = ""
    for i in text:
        if i.isupper():    
            reshif_text += chr(((ord(i) - 1040 - k) % 32) + 1040)
        elif i.islower():
            reshif_text += chr(((ord(i) - 1072 - k) % 32) + 1072)
        else:
            reshif_text += i
    return reshif_text


def reshif_cher_eng(k):
    reshif_text = ""
    for i in text:
        if i.isupper():    
            reshif_text += chr(((ord(i) - 65 - k) % 26) + 65)
        elif i.islower():
            reshif_text += chr(((ord(i) - 97 - k) % 26) + 97)
        else:
            reshif_text += i
    return reshif_text
for i in range(25):
    print(reshif_cher_eng(i))


if variant == 1:
    if language == 1:
        print(shif_cher_rus(k))
    else:
        print(shif_cher_eng(k))
elif variant == 2:
    if language == 1:
        print(reshif_cher_rus(k))
    else:
        print(reshif_cher_eng(k))
