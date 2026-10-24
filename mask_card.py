
while True:

    card_number = input("Введите номер карты: ").strip().replace(" ", "")

    if not card_number:
        print("Вы ничего не ввели")

    elif not card_number.isdigit():
        print("Номер карты должен состоять только из цифр")

    elif len(card_number) != 16:
        print("Неверный номер карты")
    
    else:
        last_four = card_number[-4:]
        masked_part = "**** "
        print(f"{masked_part*3}{last_four}")
        break
        
