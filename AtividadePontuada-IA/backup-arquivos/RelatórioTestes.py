import matplotlib.pyplot as plt

def gerar_graficos(resultados):
    # Exemplo de gráfico comparando o número de perguntas feitas por cada estratégia
    labels = ['largura', 'profundidade', 'gulosa', 'a_estrela']
    valores = [len(resultados['largura']), len(resultados['profundidade']),
               len(resultados['gulosa']), len(resultados['a_estrela'])]

    plt.bar(labels, valores)
    plt.xlabel('Estratégia de Busca')
    plt.ylabel('Número de Perguntas')
    plt.title('Comparação entre Estratégias de Busca')
    plt.show()
