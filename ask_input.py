def ask_text(prompt):
    while True:
        text = input(prompt).strip()
        if not text:
            print("Строка пустая")
            continue
        return text

def ask_int(prompt, low, high):
    while True:
        text = input(prompt).strip()
        if not text:
            print("Строка пустая")
            continue
        if not text.isdigit():
            print("Нужно целое число")
            continue
        asked_number = int(text)
        if asked_number < low or asked_number > high:
            print(f"Число от {low} до {high}")
            continue
        return asked_number

def ask_yes_no(prompt):
    while True:
        text = input(prompt).strip().lower()
        if not text:
            print("Строка пустая")
            continue
        elif text == "да":
            return True
        elif text == "нет":
            return False
        else:
            print("Нужно ответить да или нет")

name = ask_text("Введите имя: ")
age = ask_int("Введите возраст: ", 1, 120)
subscribed = ask_yes_no("Подписаться на рассылку? (да/нет): ")

if subscribed:
    answer = "да"
else:
    answer = "нет"

print(f"{name}, {age} лет, рассылка: {answer}")