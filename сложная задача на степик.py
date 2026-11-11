from random import *


def shif_cher_eng():
    bias = 0
    shif_text = ""
    for i in text:
        for j in i:
            if j.isalpha():
                bias += 1
        for j in i:
            if j.isupper():
                shif_text += chr(((ord(j) - 65 + bias) % 26) + 65)
            elif j.islower():
                shif_text += chr(((ord(j) - 97 + bias) % 26) + 97)
            else:
                shif_text += j
        shif_text += " "
        bias = 0
    return shif_text


text = input().split()
print(shif_cher_eng())
