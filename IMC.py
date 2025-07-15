peso = int(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad: "))

estatura_cuadrada = altura ** 2
imc = peso / estatura_cuadrada

if imc < 20:
    print("Bajo peso")
elif imc >= 20 and imc <= 25:
    print("Peso normal")
elif imc > 25:
    print("Sobrepeso")
elif imc > 30:
    print("Obesidad")
elif imc > 40: 
    print("Obesidad morbida")        