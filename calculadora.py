def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    return a / b

def main():
    while True:
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Suma:", int(suma(a, b)))
            print("Resta:", int(resta(a, b)))
            print("Multiplicación:", int(multiplicacion(a, b)))
            print("División:", int(division(a, b)))
        except ValueError:
            print("Por favor, ingrese solo números.")

main()   