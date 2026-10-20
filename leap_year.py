year = input("Введите год: ")

if not year.isdigit():
    print("Введите год")
else:
    year = int(year)
    if (year % 4 == 0) and (year % 100 != 0) or year % 400 == 0:
        print(f"{year} год - это высокостный год")
    else:
        print(f"{year} год - не высокостный")

