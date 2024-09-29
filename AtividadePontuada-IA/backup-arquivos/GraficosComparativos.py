def gerar_graficos(resultados):
    # Médias de cada estratégia
    medias = {algoritmo: sum(resultados[algoritmo]) / len(resultados[algoritmo]) for algoritmo in resultados}

    # Gráfico de barras
    labels = list(medias.keys())
    valores = list(medias.values())

    plt.bar(labels, valores, color=['blue', 'green', 'orange', 'red'])
    plt.xlabel('Estratégia de Busca')
    plt.ylabel('Número médio de perguntas')
    plt.title('Comparação entre Estratégias de Busca')
    plt.show()

    # Gráfico de dispersão para variabilidade dos testes
    for algoritmo, resultados_algoritmo in resultados.items():
        plt.scatter([algoritmo] * len(resultados_algoritmo), resultados_algoritmo, alpha=0.6, label=algoritmo)

    plt.xlabel('Estratégia de Busca')
    plt.ylabel('Número de perguntas')
    plt.title('Variabilidade dos testes')
    plt.legend()
    plt.show()
