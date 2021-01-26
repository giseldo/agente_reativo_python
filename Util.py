import time
class Util:

    def __init__(self) -> None:
        pass

    def imprimir(self, ambiente, agente):
        print(ambiente.tabuleiro)
        print(" ")
        print("Quantidade de quadrados limpos: {}". format(agente.qtdQuadradosLimpos))
        print("Quantidade de movimentos realizados: {}". format(agente.qtdQuadradosLimpos))
        time.sleep(2)