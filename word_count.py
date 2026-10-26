while True:
    text = input("Введите строку: ").strip()

    if not text:
        print("Вы ничего не ввели")
        continue
    break

split_result_words = text.lower().split()
counts = {}

for word in split_result_words:
    counts[word] = counts.get(word, 0) + 1

result_of_sort_counts = sorted(counts)

for index in result_of_sort_counts:
    print(f"{index}: {counts[index]}")

total_values = 0

for value in counts.values():
    total_values += value

print(f"Всего слов: {total_values}")
print(f"Уникальных слов: {len(counts)}")

best_quantity = 0
best_word = ""

for current_word in result_of_sort_counts:
    quantity = counts[current_word]
    if quantity > best_quantity:
        best_quantity = quantity
        best_word = current_word

print(f"Чаще всего: {best_word} ({best_quantity} раз)")