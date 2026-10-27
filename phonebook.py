contacts = {}
while True:
    list_of_choice = ["1. Добавить контакт", "2. Найти по имени", "3. Удалить контакт", "4. Показать все", "5. Выход"]
    for item in list_of_choice:
        print(item)

    user_choice = input("Выберите пункт: ").strip()

    if not user_choice:
        print("Ввод не может быть пустым")
        continue

    if not user_choice.isdigit():
        print("Введите номер пункта")
        continue

    chosen_number = int(user_choice)

    if chosen_number == 1:
        contact_name = input("Введите имя контакта: ").strip()
        if not contact_name:
            print("Имя не может быть пустым")
            continue
        if contact_name in contacts:
            print("Такой контакт уже есть")
            continue
        contact_telephone = input("Введите номер телефона: ").strip()
        if not contact_telephone.isdigit():
            print("Телефон должен состоять из цифр")
            continue
        contacts[contact_name] = contact_telephone
        print("Контакт добавлен")       
    elif chosen_number == 2:
        find_name = input("Укажите имя: ").strip()
        if not find_name:
            print("Имя не может быть пустым")
            continue
        if find_name in contacts:
            print(f"{find_name}: {contacts[find_name]}")
        else:
            print("Контакт не найден")
            continue
    elif chosen_number == 3:
        contact_to_delete = input("Укажите имя контакта, который хотите удалить: ").strip()
        if not contact_to_delete:
            print("Имя не может быть пустым")    
            continue
        if contact_to_delete in contacts:
            deleted_contact_telephone = contacts.pop(contact_to_delete)
            print(f"Контакт удален: {contact_to_delete}, {deleted_contact_telephone}")
        else:
            print("Контакт не найден")
            continue   
    elif chosen_number == 4:
        if not contacts:
            print("Справочник пуст")
            continue   
        result_of_sorted_contacts = sorted(contacts)
        for name in result_of_sorted_contacts:
            print(f"{name}: {contacts[name]}")
    elif chosen_number == 5:
        print("Пока!")
        break    
    else:
        print("Такого пункта нет")