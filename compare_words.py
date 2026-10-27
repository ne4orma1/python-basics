while True:
    text1 = input("Введите первую строку: ").strip()

    if not text1:
        print("Вы ничего не ввели")
        continue
    break

while True:
    text2 = input("Введите вторую строку: ").strip()

    if not text2:
        print("Вы ничего не ввели")
        continue
    break
    
split_lower_words1 = text1.lower().split()
split_lower_words2 = text2.lower().split()
words1 = set(split_lower_words1)
words2 = set(split_lower_words2)
first_words_len = len(words1)
second_words_len = len(words2)
print(f"Слов в первой строке: {first_words_len}") 
print(f"Слов во второй строке: {second_words_len}")
general_words = words1 & words2
only_first = words1 - words2
only_second = words2 - words1
all_words = words1 | words2
one_of_two_words = words1 ^ words2
general_words_sorted = sorted(general_words)
only_first_sorted = sorted(only_first)
only_second_sorted = sorted(only_second)
all_words_sorted = sorted(all_words)
one_of_two_sorted = sorted(one_of_two_words)
general_words_sorted_join = ", ".join(general_words_sorted)
only_first_sorted_join = ", ".join(only_first_sorted)
only_second_sorted_join = ", ".join(only_second_sorted)
all_words_sorted_join = ", ".join(all_words_sorted)
one_of_two_sorted_join = ", ".join(one_of_two_sorted)

if not general_words_sorted_join:
    print("Общие: нет")
else:
    print(f"Общие: {general_words_sorted_join}")

if not only_first_sorted_join:
    print("Только в первой: нет")
else:
    print(f"Только в первой: {only_first_sorted_join}")

if not only_second_sorted_join:
    print("Только во второй: нет")
else:
    print(f"Только во второй: {only_second_sorted_join}")

print(f"Все слова: {all_words_sorted_join}")

if not one_of_two_sorted_join:
    print("Только в одной из строк: нет")
else:
    print(f"Только в одной из строк: {one_of_two_sorted_join}")