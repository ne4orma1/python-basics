def square(number):
    return number * number
     
first_func = square(5)
print(f"Результат первой функции: {first_func}")

def is_even(number):
    return number % 2 == 0

while True:
    user_choice = input("Введите целое число: ").strip()

    if not user_choice:
        print("Число не введено")
        continue

    if not user_choice.isdigit():
        print("Нужно ввести целое число")
        continue

    number_input = int(user_choice)
    even = is_even(number_input)
    if even:
        print(f"Число: {number_input} - четное")
    else:
        print(f"Число: {number_input} - нечетное")
    break

def greet(name, word="Привет"):
    return f"{word}, {name}!"

only_name = "Макс"
second_arg = "Пока"
print(greet(only_name))
print(greet(only_name, second_arg))
print(greet(only_name, word=second_arg))

def min_max(min_max_numbers):
    return min(min_max_numbers), max(min_max_numbers)

list_of_numbers = [4, 9, 1, 7]
lowest, highest = min_max(list_of_numbers)
print(f"Минимум: {lowest}, максимум: {highest}")

empty_numbers = []

def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

result_of_average = average(list_of_numbers)
result_of_empty = average(empty_numbers)
print(f"Среднее значение: {result_of_average:.2f}")
print(f"Среднее значение: {result_of_empty:.2f}")