def busca_em_profundidade(problema):
    fronteira = [problema.estado_inicial]
    explorados = set()

    while fronteira:
        estado_atual = fronteira.pop()
        if problema.teste_objetivo(estado_atual):
            return estado_atual  # Solução encontrada

        explorados.add(tuple(estado_atual['sintomas']))
        for acao in problema.acoes_possiveis(estado_atual):
            novo_estado = problema.resultado(estado_atual, acao)
            if tuple(novo_estado['sintomas']) not in explorados:
                fronteira.append(novo_estado)

    return None  # Solução não encontrada
