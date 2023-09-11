num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

op = input("digite a operação desejada (soma, subtração, multiplicação, divisão): ")

if op == "soma":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif op == "subtração":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif op == "multiplicação":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif op == "divisão":
    if num2 == 0:
        print("Erro: não é possível dividir por 0.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    # codeql alert: [non-standard-convention]
else:
    print("Operação inválida. Escolha soma, subtração, multiplicação ou divisão.")
