# Comment
age = input("Введите свой возраст: ").strip()
is_student = input("У вас есть студенческий билет? ").strip().lower()
price = 100

if not age.isdigit():
    print("Укажите ваш возраст")
else:
    age = int(age)
    if age <= 5:
        print("Вход для вас бесплатный")
    elif age <= 17:
        print(f"Цена билета: {price / 2:.2f}")
    elif age <= 64:
        if is_student == "да":
            print(f"Цена билета: {price / 2:.2f}")
        elif is_student == "нет":
            print(f"Цена билета: {price:.2f}")
        else:
            print("Ответьте да или нет")
    else:
        print(f"Цена билета: {price * 0.4:.2f}")
