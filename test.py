word = input() + " запретил букву"

for i in range(1072, 1104):
    if chr(i) not in word:
        continue
    new_text = ""
    print(" ".join(word.split()) + " " + chr(i))
    for j in word:
        if j != chr(i):
            new_text += j
    word = new_text.strip()
    if len(word) == 0:
        break