import random
import matplotlib.pyplot as plt
import heapq
from collections import deque

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


# Função para exibir as informações do paciente
def mostrar_informacoes_paciente(estado):
    print("\nInformações do paciente:")
    print(f"Sintomas coletados: {estado['sintomas']}")
    if 'especialidade' in estado:
        print(f"Especialidade médica recomendada: {estado['especialidade']}")
    else:
        print("Ainda coletando informações...")

# Algoritmo de busca em largura com exibição das informações
def busca_em_largura_com_exibicao(problema):
    fronteira = deque([problema.estado_inicial])
    explorados = set()

    while fronteira:
        estado_atual = fronteira.popleft()
        mostrar_informacoes_paciente(estado_atual)  # Mostra as informações do paciente
        if problema.teste_objetivo(estado_atual):
            return estado_atual

        explorados.add(tuple(estado_atual['sintomas']))
        for acao in problema.acoes_possiveis(estado_atual):
            novo_estado = problema.resultado(estado_atual, acao)
            if tuple(novo_estado['sintomas']) not in explorados:
                fronteira.append(novo_estado)

    return None


# Exemplo de especialidades médicas e sintomas
especialidades = {
    "cardiologista": ["dor no peito", "fadiga"],
    "neurologista": ["dor de cabeça", "tontura"],
    "infectologista": ["febre", "calafrios"],
    "gastroenterologista": ["dor abdominal", "náusea"]
}

sintomas_possiveis = ["febre", "dor no peito", "fadiga", "dor de cabeça", "tontura", "calafrios", "dor abdominal", "náusea"]

# Estado inicial do problema
estado_inicial = {'sintomas': [], 'historico': []}

# Criação do problema
problema = DiagnosticoMedicoProblema(estado_inicial, especialidades, sintomas_possiveis)

# Executa o algoritmo de busca em largura e exibe informações do paciente durante o processo
estado_final = busca_em_largura_com_exibicao(problema)

# Exibe o resultado final
print("\nTriagem concluída!")
mostrar_informacoes_paciente(estado_final)
