# Grade calculator
grade = input("Введите оценку: ").strip()

if not grade.isdigit():
    print("Нужно ввести целое число")
else:
    score = int(grade)
    if score > 100:
        print("Оценка должна быть от 0 до 100")
    elif score >= 90:
        print("Твоя оценка: А")
    elif 80 <= score <= 89:
        print("Твоя оценка: В")
    elif 70 <= score <= 79:
        print("Твоя оценка: С")
    elif 60 <= score <= 69:
        print("Твоя оценка: D")
    else:
        print("Твоя оценка: F")
