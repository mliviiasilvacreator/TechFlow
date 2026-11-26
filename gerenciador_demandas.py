
# GERENCIADOR DE DEMANDAS

# Lista para armazenar as demandas
demandas = []


def cadastrar_demanda():
    print("\n--- CADASTRAR DEMANDA ---")

    identificador = input("ID: ").strip()

    if not identificador:
        print("Erro: ID não pode ficar vazio.")
        return

    for demanda in demandas:
        if demanda["id"] == identificador:
            print("Erro: ID já cadastrado.")
            return

    titulo = input("Título: ").strip()
    solicitante = input("Solicitante: ").strip()
    prioridade = input("Prioridade: ").strip()
    cep = input("CEP: ").strip()
    cidade = input("Cidade: ").strip()
    status = input("Status: ").strip()

    if not all([
        titulo,
        solicitante,
        prioridade,
        cep,
        cidade,
        status
    ]):
        print("Erro: todos os campos são obrigatórios.")
        return

    nova_demanda = {
        "id": identificador,
        "titulo": titulo,
        "solicitante": solicitante,
        "prioridade": prioridade,
        "cep": cep,
        "cidade": cidade,
        "status": status
    }

    demandas.append(nova_demanda)

    print("Demanda cadastrada com sucesso!")


def listar_demandas():
    print("\n--- LISTAR DEMANDAS ---")

    if not demandas:
        print("Nenhuma demanda cadastrada.")
        return

    for demanda in demandas:
        print("-" * 30)

        for campo, valor in demanda.items():
            print(f"{campo}: {valor}")


def buscar_demanda():
    print("\n--- BUSCAR DEMANDA ---")

    identificador = input("Digite o ID: ").strip()

    for demanda in demandas:
        if demanda["id"] == identificador:
            print("Demanda encontrada:")

            for campo, valor in demanda.items():
                print(f"{campo}: {valor}")

            return

    print("Demanda não encontrada.")


def atualizar_status():
    print("\n--- ATUALIZAR STATUS ---")

    identificador = input("Digite o ID: ").strip()

    for demanda in demandas:
        if demanda["id"] == identificador:
            novo_status = input("Novo status: ").strip()

            if not novo_status:
                print("Erro: status não pode ficar vazio.")
                return

            demanda["status"] = novo_status

            print("Status atualizado!")
            return

    print("Demanda não encontrada.")


def excluir_demanda():
    print("\n--- EXCLUIR DEMANDA ---")

    identificador = input("Digite o ID: ").strip()

    for demanda in demandas:
        if demanda["id"] == identificador:
            demandas.remove(demanda)
            print("Demanda excluída!")
            return

    print("Demanda não encontrada.")


def menu():
    while True:
        print("\n===== GERENCIADOR DE DEMANDAS =====")
        print("1 - Cadastrar demanda")
        print("2 - Listar demandas")
        print("3 - Buscar demanda")
        print("4 - Atualizar status")
        print("5 - Excluir demanda")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_demanda()

        elif opcao == "2":
            listar_demandas()

        elif opcao == "3":
            buscar_demanda()

        elif opcao == "4":
            atualizar_status()

        elif opcao == "5":
            excluir_demanda()

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()