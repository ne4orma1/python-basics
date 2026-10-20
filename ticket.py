age = input("Введите свой возраст: ").strip()
is_student = input("У вас есть студенческий билет? ").strip().lower()
price = 100

if not age.isdigit():
    print("Укажите ваш возраст")
else:
    age = int(age)
    if is_student == "да" and 18 <= age <= 64:
        print(f"Цена билета: {price / 2}")
    elif is_student == "нет"  and 18 <= age <= 64:
        print(f"Цена билета: {price}")
    elif 0 <= age <= 5:
        print("Вход для вас бесплатный")
    elif 6 <= age <= 17:
        print(f"Цена билета: {price / 2}")
    elif age >= 65:
        print(f"Цена билета: {price * 0.4}")
    else:
        print("Ответьте да или нет")
