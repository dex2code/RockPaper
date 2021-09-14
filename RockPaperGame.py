from time import sleep
from random import choice

user_score = 0
computer_score = 0
choices = ["к", "н", "б"]

jokes = [
    "Посмотри в глупь себя",
    "Классное имя Изяслав: когда надо - Изя, когда надо - Слава",
    "Ночью подошёл к холодильнику – пришлось в очереди стоять",
    "У меня такой ИНН, что тебе и не СНИЛС",
    "Матрасы полосатые для того, чтобы знать, в каком направлении ложиться",
    "Доброе дело надо делать внезапно, чтобы не догнали",
    "Что сразу дураков не убивает, то делает их ещё дурнее",
    "В жизни главное - не лениться, захотел поспать - поспи",
    "Умный в гору не пойдёт - арендует вертолёт",
    "Ехал на дачу, поспорил с навигатором - проспорил"
    ]


def show_score():
    print()
    sleep(1)
    print(">>> Счет игры: ", user_score, ":", computer_score, sep="",  end=" ")
    if user_score > computer_score:
        print("(Пользователь выигрывает)")
    elif user_score < computer_score:
        print("(Компьютер выигрывает)")
    else:
        print("(Ничья)")
    print()


def show_joke():
    joke = choice(jokes)
    print(">>> -", joke)



print("******************************")
print("*                            *")
print("*   Камень-Ножницы-Бумага!   *")
print("*                            *")
print("******************************")
print()


max_score = 0
while max_score not in [1, 2, 3, 4, 5]:
    max_score = int(input(">>> До скольки очков играем? (1-5): "))

    if max_score not in [1, 2, 3, 4, 5]:
        print("!!! Вы можете выбрать от 1 до 5!")
        print()
        sleep(1)

show_score()


while user_score < max_score and computer_score < max_score:
    sleep(1)
    user_choice = ""
    while user_choice not in ["к", "н", "б", "о"]:
        user_choice = input(">>> Загадайте фигуру (К)амень, (Н)ожницы, (Б)умага или (О)становите игру: ").lower()
        
        if user_choice not in ["к", "н", "б", "о"]:
            print("!!! Введите первую букву своего выбора: \"К\" - камень, \"Н\" - ножницы, \"Б\" - бумага или \"О\" - остановить игру")
            print()
            sleep(1)


    print(">>> Выбор пользователя: ", end="")

    if user_choice == "к":
        print("Камень")

    elif user_choice == "н":
        print("Ножницы")

    elif user_choice == "б":
        print("Бумага")

    elif user_choice == "о":
        print("Остановить игру")
        show_score()
        print(">>> Анекдот на прощание: ")
        show_joke()
        print()
        print("Удачи!")
        quit()


    print(">>> Выбор компьютера: ", end="")
    for i in range(3):
        sleep(1)
        print(".", end=" ")
    sleep(1)

    computer_choice = choice(choices)

    if computer_choice == "к":
        print("Камень")

    elif computer_choice == "н":
        print("Ножницы")

    elif computer_choice == "б":
        print("Бумага")


    print(">>> ", end="")

    if user_choice == "к":
        if computer_choice == "к":
            print("В этот раз ничья")
        if computer_choice == "н":
            print("Пользователь победил!")
            user_score += 1
        if computer_choice == "б":
            print("Компьютер победил!")
            computer_score += 1
            print()
            print(">>> Утешительный анекдот:")
            show_joke()

    elif  user_choice == "н":
        if computer_choice == "к":
            print("Компьютер победил!")
            computer_score += 1
            print()
            print(">>> Утешительный анекдот:")
            show_joke()
        if computer_choice == "н":
            print("В этот раз ничья")
        if computer_choice == "б":
            print("Пользователь победил!")
            user_score += 1

    elif  user_choice == "б":
        if computer_choice == "к":
            print("Пользователь победил!")
            user_score += 1
        if computer_choice == "н":
            print("Компьютер победил!")
            computer_score += 1
            print()
            print(">>> Утешительный анекдот:")
            show_joke()
        if computer_choice == "б":
            print("В этот раз ничья")

    show_score()

print(">>> Игра закончена со счетом ", user_score, ":", computer_score)
if user_score > computer_score:
    print(">>> Пользователь выиграл!")
else:
    print(">>> Компьютер выиграл!")

sleep(1)
print()
print(">>> Анекдот на прощание: ")
show_joke()
print()
print("Удачи!")
quit()
