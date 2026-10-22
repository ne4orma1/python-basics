

while True: 
    text = input("Введите число от 1 до 10: ").strip()

    if not text.isdigit():
        print("Нужно ввести число от 1 до 10")
        continue
    else:
        number = int(text)
        if 1 <= number <= 10:
                break
        else:
            print("Число должно быть от 1 до 10")

for i in range(1, 11):
    total = number * i
    print(f"{number} X {i} = {total}")
    

    