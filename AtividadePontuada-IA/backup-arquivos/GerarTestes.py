import random

def gerar_testes(problema, n_testes=100):
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

        # Executar cada algoritmo e medir o desempenho
        resultados['largura'].append(busca_em_largura(problema))
        # (Implementar busca em profundidade, gulosa e A* e adicionar os resultados)

    return resultados
