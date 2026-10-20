year = input("Введите год: ")

if not year.isdigit():
    print("Введите год")
elif int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
    print(f"{year} год - это высокостный год")
else:
    print(f"{year} год - не высокостный")
