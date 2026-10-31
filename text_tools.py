def count_words(text):

    words_list = text.lower().split()
    counts = {}

    for word in words_list:
        counts[word] = counts.get(word, 0) + 1

    return counts

def top_word(counts):

    sorted_counts = sorted(counts)
    best_quantity = 0
    best_word = ""

    for current_word in sorted_counts:
        quantity = counts[current_word]
        if quantity > best_quantity:
            best_quantity = quantity
            best_word = current_word
    return best_word, best_quantity

def common_words(text1, text2):

    words_list1 = text1.lower().split()
    words_list2 = text2.lower().split()
    words1_set = set(words_list1)
    words2_set = set(words_list2)
    words_common = words1_set & words2_set
    sorted_words = sorted(words_common)

    return sorted_words

first_string = "Привет мир привет"
second_string = "мир ПРИВЕТ всем"

result1 = count_words(first_string)
result2 = count_words(second_string)

top, top_count = top_word(result1)
print(f"Чаще всего: {top} ({top_count} раз)")

top, top_count = top_word(result2)
print(f"Чаще всего: {top} ({top_count} раз)")

result3 = common_words(first_string, second_string)
if not result3:
    print("Общих слов нет")
else:
    print(f"Общие слова: {', '.join(result3)}")