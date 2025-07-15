peso = int(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

estatura_cuadrada = altura ** 2
imc = peso / estatura_cuadrada

if imc < 20:
    print("Estas Bajo peso deberias ir a un nutricionista")
elif imc >= 20 and imc <= 25:
    print("Estas en Peso normal te estas cuidando bien")
elif imc > 25:
    print("Estas en Sobrepeso deberias ir a un nutricionista para que te de una dieta adecuada")
elif imc > 30:
    print("Estas en Obesidad deberias ir a un nutricionista para que te de una dieta adecuada y aun medico para que te de un tratamiento adecuado")
elif imc > 40: 
    print("Estas en Obesidad deberias ir a un nutricionista para que te de una dieta adecuada y aun medico para que te de un tratamiento adecuado")        