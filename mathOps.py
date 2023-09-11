import sys

if len(sys.argv) != 4:
    print("python mathOps.py <num1> <num2> <op>")
    sys.exit(1)

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
op = sys.argv[3]

if op == "soma":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif op == "subtração":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif op == "multiplicação":
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
elif op == "divisão":
    if num2 == 0:
        print("Erro: não é possível dividir por 0.")
    else:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
else:
    print("Operação não reconhecida.")

