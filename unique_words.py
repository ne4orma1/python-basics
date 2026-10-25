while True:
    text = input("Введите строку: ").strip().lower()
    if not text:
        print("Текст пустой")
        continue
    break

split_words = text.split()
unique_words = []
for word in split_words:
    if word not in unique_words:
        unique_words.append(word)

sorted_words = sorted(unique_words)
length_split_words = len(split_words)
length_unique_words = len(unique_words)
result_unique_words = ", ".join(unique_words)
result_sorted_words = ", ".join(sorted_words)
print(f"Всего слов: {length_split_words}")
print(f"Уникальных слов: {length_unique_words}")
print(f"Слова: {result_unique_words}")
print(f"По алфавиту: {result_sorted_words}")

