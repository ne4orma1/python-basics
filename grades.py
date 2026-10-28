gradebook = {}
while True:
    student_name = input("Введите имя ученика или 'стоп': ").strip().lower()
    if not student_name:
        print("Имя не может быть пустым")
        continue

    if student_name == "стоп":
        break

    print(f"Ученик: {student_name.title()}")

    while True:
        grade = input("Введите оценку: ").strip()
        if not grade.isdigit():
            print("Оценка должна быть целым числом от 1 до 12")
            continue
        int_grade = int(grade)
        if int_grade < 1 or int_grade > 12:
            print("Оценка должна быть целым числом от 1 до 12")
            continue
        break

    title_name = student_name.title()

    if title_name not in gradebook:
        gradebook[title_name] = []
    gradebook[title_name].append(int_grade)

if not gradebook:
    print("В журнале ничего нет")
else:
    for name in sorted(gradebook):
        marks = gradebook[name]
        marks_text = []
        for mark in marks:
            marks_text.append(str(mark))
        average = sum(marks) / len(marks)
        print(f"{name}: {', '.join(marks_text)} | средний: {average:.2f}")

    best_student = ""
    best_average = 0

    for student in sorted(gradebook):
        marks = gradebook[student]
        average = sum(marks) / len(marks)
        if average > best_average:
            best_average = average
            best_student = student
    print(f"Лучший ученик: {best_student} (средний {best_average:.2f})")