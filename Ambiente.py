from EstadoQuadrado import EstadoQuadrado
from PosXY import PosXY
import numpy as np


class Ambiente():
    
    def __init__(self, x) -> None:
        self.iniciarTabuleiroTodoSujo(x, x)
        pass

    def iniciarTabuleiroTodoSujo(self, x, y):
        self.tabuleiro = np.zeros((x, y))
        tamanho = len(self.tabuleiro)
        l = 0
        c = 0
        while l < tamanho:
            while c < tamanho:
                self.tabuleiro[l][c] = 1
                c = c + 1
            c = 0
            l = l + 1

    # retorna a posicao do agente
    def getPosicaoAgente(self):
        tamanho = len(self.tabuleiro)
        posXY = PosXY()
        l = 0
        c = 0
        while l < tamanho:
            while c < tamanho:
                if self.tabuleiro[l][c] == EstadoQuadrado.AGENTE.value:
                    posXY.X = l
                    posXY.Y = c                    
                c = c + 1
            c = 0
            l = l + 1 
        
        return posXY
    
    def limparQuadrado(self):
        posXYoriginal = self.getPosicaoAgente()
        self.tabuleiro[posXYoriginal.X][posXYoriginal.Y] = EstadoQuadrado.LIMPO.value

    def setPosicaoAgente(self, posXY):
        self.tabuleiro[posXY.X][posXY.Y] = EstadoQuadrado.AGENTE.value


        

                
            
            

        

    