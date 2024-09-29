import heapq

def busca_heuristica_gulosa(problema):
    fronteira = []
    heapq.heappush(fronteira, (problema.heuristica(problema.estado_inicial), problema.estado_inicial))
    explorados = set()

    while fronteira:
        _, estado_atual = heapq.heappop(fronteira)
        if problema.teste_objetivo(estado_atual):
            return estado_atual  # Solução encontrada

        explorados.add(tuple(estado_atual['sintomas']))
        for acao in problema.acoes_possiveis(estado_atual):
            novo_estado = problema.resultado(estado_atual, acao)
            if tuple(novo_estado['sintomas']) not in explorados:
                heapq.heappush(fronteira, (problema.heuristica(novo_estado), novo_estado))

    return None  # Solução não encontrada
