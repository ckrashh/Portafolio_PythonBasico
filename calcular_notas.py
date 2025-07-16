aprobaron = 0
alumnos = 0

while True:
    while True:
        pasar = False
        try:
            nota1 = float(input("\nIngrese la primera nota: "))
            nota2 = float(input("Ingrese la segunda nota: "))
            nota3 = float(input("Ingrese la tercera nota: "))
            if  0 <= nota1 <= 7 and 0 <= nota2 <= 7 and 0 <= nota3 <= 7:
                break
            else:
                print("Por favor, ingresa notas entre 0 y 7.")
        except ValueError:
            print("Por favor, ingresa solo numeros.")

    promedio = (nota1 + nota2 + nota3) / 3.

    if float(promedio) > 3.9:
        pasar = True

    if pasar:
        print(f"\nAprobaste el curso con un promedio de {promedio:.1f} Felecidades")
        aprobaron += 1
    else:
        print(f"\nNo aprobaste el curso con tu promedio de {promedio:.1f} Tendras que estudiar mas.")

    alumnos += 1
    

    if input("\nDeseas calcular otra nota? (s/n): ").lower() == "n":
        break

print(f"\nAlumnos aprobados: {aprobaron} de {alumnos}")    