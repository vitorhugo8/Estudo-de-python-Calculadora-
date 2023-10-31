while True:
    num1 = int(input("Olá!\nEsta é a calculadora Rudimentar! Insira um primeiro valor para começarmos: "))
    num2 = int(input("Insira um segundo valor: "))
    decisão = str(input("Que operação deseja realizar com estes números? (M - multiplicação, D - divisão, A - adição, S - subtração, Q - sair: ) "))

    if decisão == "M" or decisão == "m":
        calculo = num1 * num2
        print(f"Certo! O resultado é: {calculo}")
    elif decisão == "D" or decisão == "d":
        calculo = num1 / num2
        print(f"Certo, o resultado é: {calculo}")
    elif decisão == "A" or decisão == "a":
        calculo = num1 + num2
        print(f"Certo, o resultado é: {calculo}")
    elif decisão == "S" or decisão == "s":
        calculo = num1 - num2
        print(f"Certo, o resultado é: {calculo}")
    elif decisão == "Q" or decisão == "q":
        print("Saindo da calculadora.")
        break
    else:
        print("Perdão, é necessário inserir uma operação válida")

    continuar = input("Deseja fazer outra operação? (S - Sim, N - Não): ")
    if continuar.lower() != "s":
        print("Saindo da calculadora.")
        break
