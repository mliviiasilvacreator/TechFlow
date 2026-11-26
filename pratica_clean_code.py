

# pratica_clean_code.py

# Constantes do sistema
PRIORIDADE_URGENTE = 3
PRIORIDADE_NORMAL = 2
PRIORIDADE_BAIXA = 1

PRAZO_CRITICO = 1
PRAZO_MEDIO = 3
PRAZO_BAIXO = 7


def calcular_prioridade(tempo_aberto, categoria, cliente_vip):
    """
    Calcula a prioridade de um chamado.
    """

    categoria = categoria.lower().strip()

    if cliente_vip:
        return PRIORIDADE_URGENTE

    if categoria == "urgente" or categoria == "critica":
        return PRIORIDADE_URGENTE

    if tempo_aberto >= 7:
        return PRIORIDADE_URGENTE

    if categoria == "normal" or tempo_aberto >= 3:
        return PRIORIDADE_NORMAL

    return PRIORIDADE_BAIXA


def calcular_prazo(prioridade):
    """
    Calcula o prazo de atendimento do chamado.
    """

    if prioridade == PRIORIDADE_URGENTE:
        return PRAZO_CRITICO

    elif prioridade == PRIORIDADE_NORMAL:
        return PRAZO_MEDIO

    else:
        return PRAZO_BAIXO


def exibir_chamados(chamados):
    """
    Exibe os dados e resultados dos chamados.
    """

    for chamado in chamados:
        prioridade = calcular_prioridade(
            chamado["tempo_aberto"],
            chamado["categoria"],
            chamado["cliente_vip"]
        )

        prazo = calcular_prazo(prioridade)

        print(f"Chamado: {chamado['nome']}")
        print(f"Prioridade: {prioridade}")
        print(f"Prazo: {prazo} dia(s)")
        print("-" * 30)


# Dados para testar o programa
lista_chamados = [
    {
        "nome": "Problema no servidor",
        "tempo_aberto": 8,
        "categoria": "urgente",
        "cliente_vip": False
    },
    {
        "nome": "Erro no sistema",
        "tempo_aberto": 3,
        "categoria": "normal",
        "cliente_vip": False
    },
    {
        "nome": "Solicitacao de acesso",
        "tempo_aberto": 1,
        "categoria": "baixa",
        "cliente_vip": False
    }
]


if __name__ == "__main__":
    exibir_chamados(lista_chamados)
