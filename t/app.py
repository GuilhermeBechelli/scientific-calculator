import math

def menu():
    print("===== Calculadora Científica =====")
    print("1. Raiz quadrada")
    print("2. Potência")
    print("3. Logaritmo")
    print("4. Seno")
    print("5. Cosseno")
    print("6. Tangente")
    print("0. Sair")

def calcular_raiz_quadrada():
    num = float(input("Digite um número: "))
    result = math.sqrt(num)
    print("A raiz quadrada de", num, "é:", result)

def calcular_potencia():
    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))
    result = math.pow(base, expoente)
    print(base, "elevado a", expoente, "é igual a:", result)

def calcular_logaritmo():
    num = float(input("Digite um número: "))
    result = math.log10(num)
    print("O logaritmo de", num, "na base 10 é:", result)

def calcular_seno():
    angulo = float(input("Digite o ângulo em graus: "))
    radianos = math.radians(angulo)
    result = math.sin(radianos)
    print("O seno de", angulo, "é:", result)

def calcular_cosseno():
    angulo = float(input("Digite o ângulo em graus: "))
    radianos = math.radians(angulo)
    result = math.cos(radianos)
    print("O cosseno de", angulo, "é:", result)

def calcular_tangente():
    angulo = float(input("Digite o ângulo em graus: "))
    radianos = math.radians(angulo)
    result = math.tan(radianos)
    print("A tangente de", angulo, "é:", result)

while True:
    menu()
    opcao = int(input("Selecione uma opção: "))

    if opcao == 1:
        calcular_raiz_quadrada()
    elif opcao == 2:
        calcular_potencia()
    elif opcao == 3:
        calcular_logaritmo()
    elif opcao == 4:
        calcular_seno()
    elif opcao == 5:
        calcular_cosseno()
    elif opcao == 6:
        calcular_tangente()
    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
