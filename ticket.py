PRICE = 100

while True:

    age = input("Введите свой возраст: ").strip()

    if not age.isdigit():
        print("Укажите ваш возраст")
        continue
    break


age = int(age)

if age <= 5:
    print("Вход для вас бесплатный")
elif age <= 17:
    print(f"Цена билета: {PRICE / 2:.2f}")
elif age <= 64:
    while True:
        is_student = input("У вас есть студенческий билет? ").strip().lower()
        if is_student == "да":
            print(f"Цена билета: {PRICE / 2:.2f}")
            break
        elif is_student == "нет":
            print(f"Цена билета: {PRICE:.2f}")
            break
        else:
            print("Напишите да или нет")

else:        
    print(f"Цена билета: {PRICE * 0.4:.2f}")