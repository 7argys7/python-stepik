from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
nonpunctuation = "il1Lo0O"

chars = ""
print("Сколько паролей нужно создать?")
amount = int(input())
print("Укажите длину одного пароля:")
lens = int(input())
print("Включать ли цифры?")
numbers = input().lower()
if numbers == "да":
    chars += digits
print("Включать ли прописные буквы?(большие)")
uper = input().lower()
if uper == "да":
    chars += uppercase_letters
print("Включать ли строчные буквы?(маленькие)")
lower = input().lower()
if lower == "да":
    chars += lowercase_letters
print("Включать ли символы?")
symbol = input().lower()
if symbol == "да":
    chars += punctuation
print("исключить неоднозначные символы?(il1Lo0O)")
nonsymbol = input().lower()

def generate_password(lenght, chars):
    for i in range(amount):
        if nonsymbol == "да":
            for i in chars:
                if i in nonpunctuation:
                    chars = chars.replace(i, "")             
        for j in range(lenght):
            print(chars[randint(0, len(chars) - 1)], end="")

generate_password(lens, chars)