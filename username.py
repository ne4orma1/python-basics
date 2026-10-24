while True:

    username = input("Введите имя: ").strip()

    if not username:
        print("Имя не введено")
        
    elif username[0].isdigit():
        print("Имя не должно начинаться с цифры")
        
    elif not username.isalnum():
        print("Имя должно состоять только из цифр и букв")
        
    elif len(username) < 3:
        print("Имя слишком короткое")
        
    elif len(username) > 16:
        print("Имя слишком длинное")
        
    else:
        result = username.lower()
        print(f"Имя принято: {result}")
        break

    
    
