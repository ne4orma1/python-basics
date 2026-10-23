phrase = input("Введите слово или фразу: ").lower().replace(" ", "")

result = phrase

if not result:
    print("Строка пустая")
elif result == result[::-1]:
    print("Фраза палиндром")
else:
    print("Фраза не палиндром")


# Loop decision fot this task

# phrase = input("Введите слово или фразу: ").lower()

# result = ""

# for char in phrase:

#     if char.isalnum():
#         result += char
        
# if not result:
#     print("Фраза пустая")
# elif result == result[::-1]:
#     print("Фраза палиндром")
# else:
#     print("Фраза не палиндром")

