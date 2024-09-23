from datetime import datetime, timedelta # bibliotecas para data e hora

creditos = 0 # inicia sem créditos
login = 'user'
senha = '1234'
historico = []  # matriz que armazena os dados

# adiciona o registro na matriz
def adicionarRegistro(matriz, dataHoraRetirada, dataHoraDevolucao):
    matriz.append([dataHoraRetirada, dataHoraDevolucao])

# função para printar a dara e hora de entrada e saída
def printRegistros(matriz):
    for i, registro in enumerate(matriz):
        print(f"Registro {i+1}:")
        print(f"  Data e Hora de Retirada: {registro[0]}")
        print(f"  Data e Hora de Devolução: {registro[1]}")

# data hora de entrada e saída
def dataHora(tempoUtilizacao):
    dataHoraRetirado = input(
        "Digite a data e hora de retirada (formato YYYY-MM-DD HH:MM): ")

    retirada = datetime.strptime(
        dataHoraRetirado, "%Y-%m-%d %H:%M")  # converte para datetime

    # calcula a data e hora de devolução
    devolucao = retirada + timedelta(hours=tempoUtilizacao)

    return retirada, devolucao

while True:
    usuarioDigitado = str(input("\nPara prosseguir digite o Usuário. "))
    senhaDigitada = str(input("Para prosseguir digite a senha. "))

    if (senhaDigitada == senha and usuarioDigitado == login):  # verificação do usuário e da senha
        while True:
            print("\nO que você deseja fazer?")
            print("| 1 - Compra de créditos;")
            print("| 2 - Impressão do relatório de entradas/saídas;")
            print("| 3 - Utilizar créditos;")

            try:
                acao = int(input("\nQual opção você deseja? "))
            except ValueError:
                print("\nPor favor, insira um número válido.")
                continue

            if acao == 1:  # compra de créditos
                try:
                    quantidadeCredito = float(
                        input("\nQual a quantidade de crédito que você deseja comprar? "))
                    if quantidadeCredito > 0:
                        creditos = creditos + quantidadeCredito
                        print(f"Sua qauntidade de crédito atual é de {creditos}.")
                    else:
                        print("Impossivel fazer compra de crédito igual a 0 ou negativa!")
                except ValueError:
                    print("Erro ao comprar créditos!")
            elif acao == 2:  # printar registros
                try:
                    printRegistros(historico)
                except ValueError:
                    print("Erro ao exibir os registros!")
            elif acao == 3:  # utilizar créditos
                try:
                    print(f"\nAtualmente você possuí {creditos} creditos.")
                    quantidadeUtilizar = int(
                        input("Quantos créditos você deseja utilizar? "))

                    if quantidadeUtilizar <= creditos and 5 < creditos:
                        dataHoraRetirada, dataHoraDevolucao = dataHora(quantidadeUtilizar)
                        adicionarRegistro(historico, dataHoraRetirada, dataHoraDevolucao)

                        creditos = creditos - quantidadeUtilizar

                        print(f"Créditos utilizados com sucesso. Seus créditos atuais são: {creditos}.")
                    else:
                        print("Você não possui créditos suficientes!")
                except ValueError:
                    print("Erro ao utilizar créditos!")
    else:
        print("Usuário ou senha incorretos, digite novamente as credenciais!")