import datetime

# VARIAVEIS

saldo = 0
LIMITE = 500
saques = 0
LIMITE_SAQUES = 10
extrato = ""

# definindo as funções, saque, deposito, extrato, formato_moeda
# limite do valor do saque:500, limite do numero de saque diario= 10, o estrato deve conter as operações e o valor do saldo.
# todas as operações estaram em formato moeda
# mostrar no extrato data e hora da operação


ultima_data = datetime.datetime.now(datetime.timezone(
    datetime.timedelta(hours=-3), "BRT")).date()


def verificar_data():
    global saques, ultima_data
    data_atual = datetime.datetime.now(datetime.timezone(
        datetime.timedelta(hours=-3), "BRT")).date()
    if data_atual != ultima_data:
        saques = 0
        ultima_data = data_atual


def minha_data():
    data_formato_utc_brazil = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=-3), "BRT"))
    return data_formato_utc_brazil.strftime("%d/%m/%Y %H:%M:%S")


def formato_moeda(valor):
    return f"R$ {valor:.2f}\n".replace(".", ",")


def deposito(valor):
    global saldo, extrato

    if valor > 0:
        saldo += valor
        extrato += f"{minha_data()
                      } | + {formato_moeda(valor)}"
    else:
        print("Valor invalido.")


def sacar(valor):
    global saldo, extrato, saques, LIMITE

    verificar_data()

    if saques >= LIMITE_SAQUES:
        print(f"Voce atingiu o limite de {
              LIMITE_SAQUES} saques, aguarde 24h para uma nova transação")

    elif valor > saldo:
        print("Saldo insuficiente")

    elif valor > LIMITE:
        print(f"Valor do saque de R$: {valor:.2f}".replace(
            ".", ","), f"é superior ao limite de {LIMITE}")

    elif valor <= saldo:
        print(f"Realizando saque de R$: {valor:.2f}".replace(".", ","))
        saldo -= valor
        saques += 1
        extrato += f"{minha_data()} | - {formato_moeda(valor)}"

    else:
        print("Operação invalida")


def meu_extrato():
    print("================Extrato================")
    print(extrato if extrato else "numhuma operação realizada")
    print(f"Seu saldo é {formato_moeda(saldo)}{minha_data()}")


menu = """
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
"""

while True:
    opcoes = input(menu).lower()
    if opcoes == "d":
        valor = int(input("Valor do deposito:  "))
        deposito(valor)

    elif opcoes == "s":
        valor = int(input("Digite o valor do Saque:  "))
        sacar(valor)

    elif opcoes == "e":
        meu_extrato()

    elif opcoes == "q":
        break
    else:
        print("Opção invalida")
