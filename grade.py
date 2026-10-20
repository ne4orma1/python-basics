# Grade calculator
grade = input("Введите оценку: ").strip()

if not grade.isdigit():
    print("Нужно ввести целое число")
elif int(grade) > 100:
    print("Оценка должна быть от 0 до 100")
elif 90 <= int(grade) <= 100:
    print("Твоя оценка: А")
elif 80 <= int(grade) <= 89:
    print("Твоя оценка: В")
elif 70 <= int(grade) <= 79:
    print("Твоя оценка: С")
elif 60 <= int(grade) <= 69:
    print("Твоя оценка: F")
