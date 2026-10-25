tasks = []
while True:
    list_of_choice = ["1. Добавить задачу", "2. Показать задачи", "3. Удалить задачу", "4. Выход"]
    for item in list_of_choice:
        print(item)

    user_choice = input("Выберите пункт: ").strip()

    if not user_choice:
        print("Ввод пустой")
        continue

    if not user_choice.isdigit():
        print("Введите номер пункта")
        continue

    choice_number = int(user_choice)

    if choice_number == 1:
        text_of_task = input("Введите текст задачи: ").strip()
        if not text_of_task:
            print("Задача не может быть пустой")
        else:
            tasks.append(text_of_task)
            print("Задача добавлена")
    elif choice_number == 2:
        if not tasks:
            print("Список задач пуст")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")
    elif choice_number == 3:
        if not tasks:
            print("Список задач пуст")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")
            delete_number = input("Введите номер задачи, которую хотите удалить: ").strip()
            if not delete_number:
                print("Ввод пустой")
                continue
            if not delete_number.isdigit():
                print("Введите номер задачи")
                continue
            number_of_delete = int(delete_number)
            if number_of_delete <= 0 or number_of_delete > len(tasks):
                print("Такой задачи нет")
                continue
            deleted_task = tasks.pop(number_of_delete - 1)
            print(f"Задача удалена: {deleted_task}")
    elif choice_number == 4:
        print("Пока!")
        break
    else:
        print("Такого пункта нет")




