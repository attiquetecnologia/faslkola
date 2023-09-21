num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
res = 0
print("Digite a opção desejada!")
print("1 - Somar")
print("2 - Subtrair")
opt = input("")
if opt =="1":
    res = float(num1) + float(num2)
elif opt =="2":
    res = float(num1) - float(num2)
else:
    print("Opção inválida!, tente novamente!")
print("O resultado é: " + str(res))
