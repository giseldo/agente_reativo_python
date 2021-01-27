import time
class Util:

    def __init__(self) -> None:
        pass

    def imprimir(self, ambiente, agente):
        print(ambiente.tabuleiro)
        print(" ")
        print("Medida de desempenho 1 : Quantidade de quadrados limpos: {}". format(agente.qtdQuadradosLimpos))
        print("Medida de desempenho 2 : Quantidade de movimentos realizados: {}". format(agente.qtdMovimentos))
        # print("Movimentos Restantes {}". format(agente.bateria - agente.qtdMovimentos)) descomente essa linha
        time.sleep(2)