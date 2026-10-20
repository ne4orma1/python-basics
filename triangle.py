a = float(input("Введите сторону 'а': "))
b = float(input("Введите сторону 'b': "))
c = float(input("Введите сторону 'c': "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    if a == b and a == c and b == c:
        print("Треугольник равносторонний")
    elif a == b and a != c and b != c or a == c and a != b and c != b or b == c and b !=a and c != a:
        print("Треугольник равнобедренный")
    elif a != b and a != c and b != c:
        print("Треугольник разносторонний")
else:
    print("Треугольник не существует")
