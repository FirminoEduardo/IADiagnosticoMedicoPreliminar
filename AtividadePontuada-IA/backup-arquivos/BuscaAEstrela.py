def busca_a_estrela(problema):
    fronteira = []
    heapq.heappush(fronteira, (problema.heuristica(problema.estado_inicial), problema.estado_inicial, 0))
    explorados = set()

    while fronteira:
        _, estado_atual, custo_atual = heapq.heappop(fronteira)
        if problema.teste_objetivo(estado_atual):
            return estado_atual  # Solução encontrada

        explorados.add(tuple(estado_atual['sintomas']))
        for acao in problema.acoes_possiveis(estado_atual):
            novo_estado = problema.resultado(estado_atual, acao)
            novo_custo = custo_atual + problema.funcao_custo(estado_atual, novo_estado)
            if tuple(novo_estado['sintomas']) not in explorados:
                heapq.heappush(fronteira, (novo_custo + problema.heuristica(novo_estado), novo_estado, novo_custo))

    return None  # Solução não encontrada
