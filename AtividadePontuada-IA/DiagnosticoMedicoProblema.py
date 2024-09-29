import random
import pandas as pd
from collections import deque
import heapq

# Definição do problema de Diagnóstico Médico
class DiagnosticoMedicoProblema:
    def __init__(self, estado_inicial, especialidades, sintomas_possiveis):
        self.estado_inicial = estado_inicial
        self.especialidades = especialidades
        self.sintomas_possiveis = sintomas_possiveis

    def acoes_possiveis(self, estado_atual):
        sintomas_faltantes = [s for s in self.sintomas_possiveis if s not in estado_atual['sintomas']]
        return sintomas_faltantes

    def resultado(self, estado_atual, acao):
        novo_estado = estado_atual.copy()
        novo_estado['sintomas'].append(acao)
        return novo_estado

    def teste_objetivo(self, estado_atual):
        for especialidade, sintomas_necessarios in self.especialidades.items():
            if all(s in estado_atual['sintomas'] for s in sintomas_necessarios):
                estado_atual['especialidade'] = especialidade  # Adiciona a especialidade no estado
                return True
        return False

    def funcao_custo(self, estado_atual, proximo_estado):
        return 1

    def heuristica(self, estado_atual):
        for especialidade, sintomas_necessarios in self.especialidades.items():
            sintomas_faltantes = [s for s in sintomas_necessarios if s not in estado_atual['sintomas']]
            if sintomas_faltantes:
                return len(sintomas_faltantes)
        return 0

# Algoritmo de busca em largura
def busca_em_largura(problema):
    fronteira = deque([problema.estado_inicial])
    explorados = set()

    while fronteira:
        estado_atual = fronteira.popleft()
        if problema.teste_objetivo(estado_atual):
            return estado_atual

        explorados.add(tuple(estado_atual['sintomas']))
        for acao in problema.acoes_possiveis(estado_atual):
            novo_estado = problema.resultado(estado_atual, acao)
            if tuple(novo_estado['sintomas']) not in explorados:
                fronteira.append(novo_estado)

    return None

# Algoritmo de busca em profundidade
def busca_em_profundidade(problema):
    fronteira = [problema.estado_inicial]
    explorados = set()

    while fronteira:
        estado_atual = fronteira.pop()
        if problema.teste_objetivo(estado_atual):
            return estado_atual

        explorados.add(tuple(estado_atual['sintomas']))
        for acao in problema.acoes_possiveis(estado_atual):
            novo_estado = problema.resultado(estado_atual, acao)
            if tuple(novo_estado['sintomas']) not in explorados:
                fronteira.append(novo_estado)

    return None

# Algoritmo de busca gulosa
def busca_gulosa(problema):
    fronteira = []
    heapq.heappush(fronteira, (0, problema.estado_inicial))  # (custo, estado)
    explorados = set()

    while fronteira:
        custo, estado_atual = heapq.heappop(fronteira)
        if problema.teste_objetivo(estado_atual):
            return estado_atual

        explorados.add(tuple(estado_atual['sintomas']))
        for acao in problema.acoes_possiveis(estado_atual):
            novo_estado = problema.resultado(estado_atual, acao)
            if tuple(novo_estado['sintomas']) not in explorados:
                heuristica = problema.heuristica(novo_estado)
                heapq.heappush(fronteira, (custo + 1 + heuristica, novo_estado))

    return None

# Algoritmo A*
def busca_a_star(problema):
    fronteira = []
    heapq.heappush(fronteira, (0, problema.estado_inicial))  # (custo total, estado)
    explorados = set()

    while fronteira:
        custo_total, estado_atual = heapq.heappop(fronteira)
        if problema.teste_objetivo(estado_atual):
            return estado_atual

        explorados.add(tuple(estado_atual['sintomas']))
        for acao in problema.acoes_possiveis(estado_atual):
            novo_estado = problema.resultado(estado_atual, acao)
            if tuple(novo_estado['sintomas']) not in explorados:
                custo = problema.funcao_custo(estado_atual, novo_estado)
                heuristica = problema.heuristica(novo_estado)
                heapq.heappush(fronteira, (custo_total + custo + heuristica, novo_estado))

    return None

# Função para simular os testes
# Função para simular os testes
def executar_testes(num_testes, especialidades, sintomas_possiveis):
    resultados = {
        'Teste': [],
        'Sintomas': [],
        'Busca em Largura': [],
        'Busca em Profundidade': [],
        'Busca Gulosa': [],
        'A*': []
    }
    
    for i in range(num_testes):
        sintomas_selecionados = random.sample(sintomas_possiveis, random.randint(1, len(sintomas_possiveis)))
        estado_inicial = {'sintomas': sintomas_selecionados, 'historico': []}
        problema = DiagnosticoMedicoProblema(estado_inicial, especialidades, sintomas_possiveis)

        # Exibindo sintomas informados pelo paciente
        print(f'Paciente informa sintomas: {sintomas_selecionados}')

        # Executa as buscas e coleta a especialidade recomendada
        resultado_largura = busca_em_largura(problema)
        especialidade_largura = resultado_largura['especialidade'] if resultado_largura else 'Nenhuma especialidade encontrada'

        resultado_profundidade = busca_em_profundidade(problema)
        especialidade_profundidade = resultado_profundidade['especialidade'] if resultado_profundidade else 'Nenhuma especialidade encontrada'

        resultado_gulosa = busca_gulosa(problema)
        especialidade_gulosa = resultado_gulosa['especialidade'] if resultado_gulosa else 'Nenhuma especialidade encontrada'

        resultado_a_star = busca_a_star(problema)
        especialidade_a_star = resultado_a_star['especialidade'] if resultado_a_star else 'Nenhuma especialidade encontrada'

        # Adiciona resultados à tabela
        resultados['Teste'].append(i + 1)
        resultados['Sintomas'].append(sintomas_selecionados)
        resultados['Busca em Largura'].append(especialidade_largura)
        resultados['Busca em Profundidade'].append(especialidade_profundidade)
        resultados['Busca Gulosa'].append(especialidade_gulosa)
        resultados['A*'].append(especialidade_a_star)

        # Mensagem de debug para verificar progresso
        print(f'Especialidade recomendada (Largura): {especialidade_largura}')
        print(f'Especialidade recomendada (Profundidade): {especialidade_profundidade}')
        print(f'Especialidade recomendada (Gulosa): {especialidade_gulosa}')
        print(f'Especialidade recomendada (A*): {especialidade_a_star}')
        print('-' * 50)

    return resultados

# Exemplo de especialidades médicas e sintomas
especialidades = {
    "cardiologista": ["dor no peito", "fadiga"],
    "neurologista": ["dor de cabeça", "tontura"],
    "infectologista": ["febre", "calafrios"],
    "gastroenterologista": ["dor abdominal", "náusea"]
}

sintomas_possiveis = ["febre", "dor no peito", "fadiga", "dor de cabeça", "tontura", "calafrios", "dor abdominal", "náusea"]

# Executa os testes e coleta resultados
resultados = executar_testes(100, especialidades, sintomas_possiveis)

# Cria um DataFrame do pandas e exibe a tabela
tabela_resultados = pd.DataFrame(resultados)
print(tabela_resultados)

# Se precisar salvar em um arquivo CSV
tabela_resultados.to_csv("resultados_busca.csv", index=False)

# Código para salvar resultados em Excel
tabela_resultados = pd.DataFrame(resultados)
tabela_resultados.to_excel('resultados_teste.xlsx', index=False)

print("Resultados salvos em 'resultados_teste.xlsx'")
