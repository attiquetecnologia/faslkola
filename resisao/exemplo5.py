num1 = imput("Digite o primeiro numero: ")
num2 = imput("Digite o segundo numero: ")
res = 0
print("Digite a opção desejada!")
print("1 - Somar")
print("2 - Subtrair")
opt = input("")
if opt=="1":
    res = float(num1) + float(num2)
elif opt=="2":
    res = float(num1) - float(num2)
else:
    print("Opção Invalida, tente novamente!")

print("O resultado é: "
      + str(res))    
