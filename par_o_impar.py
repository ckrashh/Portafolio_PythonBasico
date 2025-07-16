while True:
    try:
        num = int(input("Ingrese un número: "))
        if num % 2 == 0:
            print(f"El número {num} es par")
            break
        else:
            print(f"El número {num} es impar")
            break
    except ValueError:
        print("Por favor, ingrese solo numeros.")
    