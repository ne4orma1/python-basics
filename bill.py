price = float(input( "Введите цену товара: " ))
quantity = float(input( "Введите количество товара: " ))
tax = float(input( "Введите процент налога: " ))

tax_free_price = price * quantity
sum_of_tax = tax_free_price * tax / 100
cost = tax_free_price + sum_of_tax

print(f"Сумма без налога: {tax_free_price:.2f}")
print(f"Сумма налога: {sum_of_tax:.2f}")
print(f"Итоговая сумма: {cost:.2f}")

