from datetime import datetime

print("=== ASSISTENTE INTELIGENTE DE TI ===")

def analisar_mensagem():
    mensagem = input("Digite a mensagem que deseja analisar: ")

    print("Mensagem recebida:")
    print(mensagem)

    palavras_suspeitas = [
        "bloqueada",
        "urgente",
        "clique aqui",
        "senha",
        "atualizar dados"
    ]

    termos_encontrados = []

    for palavra in palavras_suspeitas:
        if palavra in mensagem.lower():
            termos_encontrados.append(palavra)

    if termos_encontrados:
        print("ALERTA: possível sinal de phishing!")
        print("Termos encontrados:")

        for termo in termos_encontrados:
            print("-", termo)

        print("\nMotivos do alerta:")

        for termo in termos_encontrados:
            if termo == "urgente":
                print("- Linguagem de urgência para pressionar o usuário.")

            elif termo == "bloqueada":
                print("- Ameaça de bloqueio da conta.")

            elif termo == "clique aqui":
                print("- Incentivo para clicar em um link.")

            elif termo == "senha":
                print("- Possível tentativa de obter informações de acesso.")

            elif termo == "atualizar dados":
                print("- Solicitação de atualização de dados pessoais.")

    else:
        print("Nenhum termo suspeito encontrado.")

    quantidade = len(termos_encontrados)

    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if quantidade == 0:
        risco = "BAIXO"
    elif quantidade <= 2:
        risco = "MÉDIO"
    else:
        risco = "ALTO"

    print("Nível de risco:", risco)

    with open("historico.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write("Nova análise realizada\n")
        arquivo.write("Data e hora: " + data_hora + "\n")
        arquivo.write("Mensagem: " + mensagem + "\n")
        arquivo.write("Quantidade de termos suspeitos: " + str(quantidade) + "\n")
        arquivo.write("Risco: " + risco + "\n")
        arquivo.write("--------------------------\n")

def consultar_historico():
    try:
        with open("historico.txt", "r", encoding="utf-8") as arquivo:
            historico = arquivo.read()

        if historico:
            print("\n=== HISTÓRICO DE ANÁLISES ===")
            print(historico)
        else:
            print("O histórico ainda está vazio.")

    except FileNotFoundError:
        print("Ainda não existe um histórico de análises.")

while True:
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Analisar mensagem")
    print("2 - Consultar histórico")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        analisar_mensagem()

    elif opcao == "2":
        consultar_historico()

    elif opcao == "3":
        print("Encerrando o Assistente de TI. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")