#Игра "Камень-ножницы-бумага"

import random

player_score = 0
computer_score = 0

#Выбор компьютера
def get_computer_choice():
    choices = ["камень", "ножницы", "бумага"]
    return random.choice(choices)

#Определение победителя
def determine_winner(player_choice, computer_choice):
    global player_score, computer_score
    if player_choice == "камень":
        if computer_choice == "ножницы":
            player_score += 1
            print("Вам присуждается балл!")
        elif computer_choice == "бумага":
            computer_score += 1
            print("Балл присуждается компьютеру!")
        else:
            print("Ничья!")  #никому не присуждается балл

    elif player_choice == "ножницы":
        if computer_choice == "бумага":
            player_score += 1
            print("Вам присуждается балл!")
        elif computer_choice == "камень":
            computer_score += 1
            print("Балл присуждается компьютеру!")
        else:
            print("Ничья!")

    else:
        if computer_choice == "камень":
            player_score += 1
            print("Вам присуждается балл!")
        elif computer_choice == "ножницы":
            computer_score += 1
            print("Балл присуждается компьютеру!")
        else:
            print("Ничья!")


#Основная логика игры и объяснение правил
def main():
    global player_score, computer_score
    print("Добро пожаловать в игру 'Камень-Ножницы-Бумага'!")
    print("Правила:")
    print("Камень бьет ножницы")
    print("Ножницы бьют бумагу")
    print("Бумага бьет камень")
    print("Игра продолжается, пока кто-то не наберет 3 очка")
    #Сколько изначально очков у игрока и компьютера



    while player_score < 3 and computer_score < 3:  #Пока не набереться 3 очка, то будут запрашивать у игрока выбор
        player_choice = input("Введите ваш выбор: ").lower()

        if player_choice not in ["камень", "ножницы", "бумага"]:
            print("Ошибка! Попробуйте снова!")

        computer_choice = get_computer_choice()
        print(f"Компьютер выбрал {computer_choice}")

        determine_winner(player_choice, computer_choice)  #определение победителя
        if player_score == 3:
            print("Вы победили!")

#следит за счетом
        print(f"Счет: Вы = {player_score}, Компьютер = {computer_score}")


    print("Игра окончена!")
main()

