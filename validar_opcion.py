while True:
    texto = input("Ingrese un texto: ")
    if texto.isalpha():    
        print("El texto es alfabetico")
    elif texto.isdigit():  
        print("El texto es numerico")
    else:
        print("El texto es alfanumerico")

    if input("Desea verifcar otro texto? (s/n): ").lower() == "n":
        break    