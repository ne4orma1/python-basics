name = input("Как тебя зовут? ")
age = input("Сколько тебе лет? ") 
name = name.strip()
print(f"Привет,{name}! Через 10 лет тебе будет {int(age) + 10}.")
