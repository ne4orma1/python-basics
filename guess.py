SECRET = 37
MAX_TRIES = 5
tries = 0

while tries < MAX_TRIES:
    text = input("Угадайте число: ").strip()
    if not text.isdigit():
        print("Введите целое число")
        continue

    number = int(text)
    tries += 1

    if number == SECRET:
        if tries == 1:
            word = "попытку"
        elif tries <= 4:
            word = "попытки"
        else:
            word = "попыток"
        print(f"Вы угадали за {tries} {word}! Загаданное число - {SECRET}")
        break
    elif tries == MAX_TRIES:
        print(f"У вас закончились попытки, число было {SECRET}")
    elif number < SECRET:
        print("Больше")
    elif number > SECRET:
        print("Меньше")

