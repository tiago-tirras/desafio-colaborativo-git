import time

print("Hello, welcome to the calculator program!\n")


while True:
    print("---Menu de Operações---\n")
    print("1.somar")
    print("2.subtrair")
    print("3.multiplicar")
    print("4.dividir")
    print("5.potenciação")
    print("6.sair")


    escolha = input("escolha uma opção:")

    if escolha == "6":
        print("encerrando o programa em:")
        for i in range(5,0,-1):
            print(i)
            time.sleep(1)
        print("programa encerrado!")
        break
        

    if escolha == "1":
        n1 = int(input("digite o primeiro valo que deseja somar:"))
        n2 = int(input("digite o segundo valor para a soma:"))

        print("o valor da soma é:", n1 + n2)

    if escolha == "2":
        n1 = int(input("digite o primeiro valor:"))
        n2 = int(input("digite o segundo valor:"))
        resultado = n1 - n2

        print(f"o valor da subtração entre {n1} e {n2} é: ",resultado)

    if escolha =="3":
        n1 = int(input("digite o primeiro valor: "))
        n2 = int(input("digite o segundo valor: "))
        resultado = n1 * n2

        print(f"o resultado da multiplicação entre {n1} e {n2} é: ", resultado)

    if escolha =="4":
        n1 = int(input("digite o primeiro valor: "))
        n2 = int(input("digite o segundop valor : "))
        resultado = n1 / n2    

        print(f"o resultado da divisão entre {n1} e {n2} é: ", resultado)

# ADICIONADO: Nova operação de potenciação
    if escolha == "5":
        n1 = int(input("digite o primeiro valor: "))
        n2 = int(input("digite o segundo valor: "))
        resultado = n1 ** n2

        print(f"o resultado da potenciação entre {n1} e {n2} é: ", resultado)


    print("meu nome é Arthur Severo")
    print("meu nome é jõao Pedro")