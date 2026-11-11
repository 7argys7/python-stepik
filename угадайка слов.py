from random import *

word_list = [
    "ПРОЕБАЛСЯ НЕМНОЖКО",
    # Еда и продукты (1–6)
    "яблоко",
    "хлеб",
    "молоко",
    "сахар",
    "соль",
    "перец",
    # Животные (7–27)
    "птица",
    "кошка",
    "собака",
    "лошадь",
    "тигр",
    "медведь",
    "лиса",
    "волк",
    "заяц",
    "ёжик",
    "белка",
    "бабочка",
    "пчела",
    "муравей",
    "паук",
    "комар",
    "рыба",
    "акула",
    "дельфин",
    "кит",
    "осьминог",
    # Растения (28–39)
    "дерево",
    "цветок",
    "яблоня",
    "берёза",
    "дуб",
    "сосна",
    "клён",
    "роза",
    "ромашка",
    "тюльпан",
    "лилия",
    "сирень",
    # Природа и погода (40–54)
    "солнце",
    "река",
    "гора",
    "зима",
    "весна",
    "лето",
    "осень",
    "снег",
    "дождь",
    "ветер",
    "гроза",
    "радуга",
    "туман",
    "молния",
    "облако",
    # Космос (55–59)
    "космос",
    "планета",
    "звезда",
    "луна",
    "комета",
    # Дом и вещи (60–82)
    "книга",
    "замок",
    "фонарь",
    "часы",
    "ключ",
    "дверь",
    "окно",
    "стена",
    "стол",
    "стул",
    "шкаф",
    "кровать",
    "диван",
    "ложка",
    "вилка",
    "тарелка",
    "чашка",
    "кастрюля",
    "нож",
    "чайник",
    "холодильник",
    "плита",
    "пылесос",
    # Транспорт (83–88)
    "машина",
    "велосипед",
    "самолёт",
    "корабль",
    "поезд",
    "ракета",
    # Школа (89–98)
    "школа",
    "учитель",
    "урок",
    "тетрадь",
    "ручка",
    "карандаш",
    "линейка",
    "доска",
    "парта",
    "рюкзак",
    # Музыка и искусство (99–100)
    "музыка",
    "картина",
    # Места (101–105)
    "город",
    "театр",
    "океан",
    "остров",
    "мост",
]


def get_word():
    return choice(word_list).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # голова, торс, обе руки, одна нога
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # голова, торс, обе руки
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # голова, торс и одна рука
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # голова и торс
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # голова
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # начальное состояние
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]


def hint(hiden_word):
    hiden_word = hiden_word.lower()
    food = word_list[1:7]
    animal = word_list[7:28]
    plants = word_list[28:40]
    weather = word_list[40:55]
    space = word_list[55:60]
    house = word_list[60:83]
    transport = word_list[83:89]
    shcool = word_list[89:99]
    music = word_list[99:101]
    places = word_list[101:]
    if hiden_word in food:
        return "еда"
    if hiden_word in animal:
        return "животные"
    if hiden_word in plants:
        return "растения"
    if hiden_word in weather:
        return "Природа и погода"
    if hiden_word in space:
        return "космос"
    if hiden_word in house:
        return "дом и вещи"
    if hiden_word in transport:
        return "транспорт"
    if hiden_word in shcool:
        return "школа"
    if hiden_word in music:
        return "искуство"
    if hiden_word in places:
        return "места"


def play():
    guessed_letters = []
    guessed_words = []
    hiden_word = get_word()
    tries = 6
    guessed = False
    word_completion = ["_" for i in range(len(hiden_word))]

    print("Давайте играть в угадайку слов!")
    print(display_hangman(tries))
    print("Хотите играть с подсказками?(только на последней попытке)")
    hin = input().lower()
    print("Хотите чтобы отображалась первая и последняя буква в слове?")
    variant = input().lower()
    if variant == "да":
        word_completion[0] = hiden_word[0]
        word_completion[-1] = hiden_word[-1]
    print(*word_completion)
    print("Введите слово:")

    while True:
        word = input().upper()
        if word in guessed_letters or word in guessed_words:
            print("Вы уже изпользовали это слово введите другое")
            continue
        if not word.isalpha:
            print("Введите слово (или букву) состоящее только из букв")
        if len(word) > 1:
            if word == hiden_word:
                print("Поздравляю! Вы отгадали слово")
                print("Сыграть еще раз?")
                again = input().lower()
                if again == "да":
                    play()
                break
            else:
                guessed_words.append(word)
                tries -= 1
                if tries == 0:
                    print(display_hangman(tries))
                    print("Вы програли, неугадали слово:", hiden_word)
                    print("Сыграть еще раз?")
                    again = input().lower()
                    if again == "да":
                        play()
                    break
                print(display_hangman(tries))
                print(f"Не верно, у вас осталось {tries} попыток")
                print(word)
                print(*word_completion)

        else:
            guessed_letters.append(word)
            for i in word:
                for j in range(len(hiden_word)):
                    if i in hiden_word[j]:
                        guessed = True
                        word_completion[j] = i
                if guessed == True:
                    print("Угадали букву:")
                    print(word)
                    print(*word_completion)
                else:
                    tries -= 1
                    if tries == 0:
                        print(display_hangman(tries))
                        print("Вы програли, неугадали слово:", hiden_word)
                        print("Сыграть еще раз?")
                        again = input().lower()
                        if again == "да":
                            play()
                        break
                    print(display_hangman(tries))
                    print(word)
                    print(*word_completion)
                    print("Неугадали, осталось попыток:", tries)
                guessed = False
        if word_completion.count("_") == 0:
            print("Поздравляю! Вы отгадали слово")
            print("Сыграть еще раз?")
            again = input().lower()
            if again == "да":
                play()
            break
        if hin == "да":
            if tries == 1:
                print("подсказка:", hint(hiden_word))


hiden_word = get_word()
play()
