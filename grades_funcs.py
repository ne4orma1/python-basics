def average(marks):
    return sum(marks) / len(marks)

def add_grade(gradebook, name, grade):
    if name not in gradebook:
        gradebook[name] = []
    gradebook[name].append(grade)

def best_student(gradebook):
    best_name = ""
    best_average = 0

    for student in sorted(gradebook):
        marks = gradebook[student]
        student_average = average(marks)
        if student_average > best_average:
            best_average = student_average
            best_name = student
    return best_name, best_average

def print_report(gradebook):
    for name in sorted(gradebook):
        marks = gradebook[name]
        average_marks = average(marks)
        marks_text = []
        for mark in marks:
            marks_text.append(str(mark))
        print(f"{name}: {', '.join(marks_text)} | средний: {average_marks:.2f}")

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

gradebook = {}

while True:
    student_name = input("Введите имя ученика: ").strip().lower()
    if not student_name:
        print("Имя не может быть пустым")
        continue

    if student_name == "стоп":
        break

    print(f"Ученик: {student_name.title()}")
    grade = ask_int("Введите оценку: ", 1, 12)
    add_grade(gradebook, student_name.title(), grade)

if not gradebook:
    print("Журнал пуст")
else:
    print_report(gradebook)
    best_name, best_grade = best_student(gradebook)
    print(f"Лучший ученик: {best_name} (средний {best_grade:.2f}) ")