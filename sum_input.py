count = 0
total = 0


while True:
    text = input("Введите число или 'стоп' ").strip().lower()
    if text == "стоп":
        break
    if not text.isdigit():
        print("Это не число, введите целое число или 'стоп'")
        continue
    number = int(text)
    count += 1
    total += number

if count == 0:
    print("Чисел не введено")
else:
    print(f"Чисел введено: {count}")
    print(f"Сумма всех чисел: {total}")
    print(f"Среднее: {total / count:.2f}")
