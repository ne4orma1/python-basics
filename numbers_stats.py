
while True:

    text = input("Введите строку с числами через пробел: ").strip()

    numbers = text.split()

    if not numbers:
        print("Строка пуста")
        continue

    check_numbers = "".join(numbers)

    if not check_numbers.isdigit():
        print("Нужны только целые числа")
        continue
    
    break


int_numbers = []

for number in numbers:
    number = int(number)
    int_numbers.append(number)
#    int_numbers.append(int(number)) - второй вариант записи

len_int_numbers = len(int_numbers)
min_int_numbers = min(int_numbers)
max_int_numbers = max(int_numbers)
sum_int_numbers = sum(int_numbers)
average = sum_int_numbers/len_int_numbers
ascending_numbers = sorted(int_numbers)
descending_numbers = sorted(int_numbers, reverse=True)

above_average = []

for int_number in int_numbers:
    if int_number > average:
        above_average.append(int_number)


print(f"количество: {len_int_numbers}, минимум: {min_int_numbers}, максимум: {max_int_numbers}, сумма: {sum_int_numbers}, среднее: {average:.2f}, числа по возрастанию: {ascending_numbers}, числа по убыванию: {descending_numbers}, числа больше среднего: {above_average}")


    
# from if not numbers:
#   all_digits = True              

#   for part in numbers:
#        if not part.isdigit():
#            all_digits = False     
#            break                  

#    if not all_digits:
#        print("Нужны только целые числа")
#        continue
# to break