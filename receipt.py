
MAX_TRIES = 3
tries = 0

receipt = ""

total = 0

while tries < MAX_TRIES:

    product = input("Введите продукт: ").strip()
    cost = input("Введите цену продукта: ").strip()

    if not product:
        print("Вы не ввели продукт")
        continue

    if not cost.isdigit():
        print("Неверная цена продукта")
        continue

    
    
    cost = int(cost)
    receipt += f"{product:<12}{cost:>8.2f}\n"
    total += cost
    tries += 1

print(f"{receipt}{'ИТОГО:':<12}{total:>8.2f}")

    