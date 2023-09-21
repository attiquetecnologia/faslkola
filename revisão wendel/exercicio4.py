n1 = int(input("Digite a 1º nota:"))
n2 = int(input("Digite a 2º nota: "))
n3 = int(input("Digite a 3º nota: "))

numero = (n1 + n2 + n3) / 3

if numero >= 7:
    print("Aprovado!!")
elif numero <= 5:
    print("Recuperação!")
elif numero > 5:
    print("Reprovado!")
    