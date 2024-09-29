def rodar_testes(problema, n_testes=100):
    resultados = {
        'largura': [],
        'profundidade': [],
        'gulosa': [],
        'a_estrela': []
    }

    for _ in range(n_testes):
        # Gerar um estado inicial aleatório (sintomas e histórico)
        sintomas_iniciais = random.sample(problema.sintomas_possiveis, k=random.randint(1, 3))
        estado_inicial = {'sintomas': sintomas_iniciais, 'historico': []}
        problema.estado_inicial = estado_inicial

        # Executar e armazenar o número de passos até a solução
        resultados['largura'].append(len(busca_em_largura(problema)['sintomas']))
        resultados['profundidade'].append(len(busca_em_profundidade(problema)['sintomas']))
        resultados['gulosa'].append(len(busca_heuristica_gulosa(problema)['sintomas']))
        resultados['a_estrela'].append(len(busca_a_estrela(problema)['sintomas']))

    return resultados
