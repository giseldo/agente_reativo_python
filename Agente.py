import random
from EstadoQuadrado import EstadoQuadrado
from PontosCardeais import PontosCardeais
from PosXY import PosXY

class Agente:
    
    lista_percepcoes = list()

    qtdQuadradosLimpos = 1
    qtdMovimentos = 1
    # bateria = 15 descomente essa linha


    def __init__(self) -> None:
        pass

    # acao do agente a partir das percepcoes ele envia uma mensagem para o ambiente para limpar e mover
    def acao(self, ambiente):
        posXY = ambiente.getPosicaoAgente()
        # if self.qtdMovimentos < self.bateria:
        # descomente esse if acima e idente tudo tudo que tem abaixo do if neste médodo
        if self.lista_percepcoes[PontosCardeais.NORTE.value] == EstadoQuadrado.SUJO.value: 
            posXY.X = posXY.X-1
            ambiente.limparQuadrado()
            self.qtdQuadradosLimpos = self.qtdQuadradosLimpos + 1
            self.qtdMovimentos = self.qtdMovimentos + 1
            ambiente.setPosicaoAgente(posXY)
        elif self.lista_percepcoes[PontosCardeais.SUL.value] == EstadoQuadrado.SUJO.value: 
            posXY.X = posXY.X+1
            ambiente.limparQuadrado()
            self.qtdQuadradosLimpos = self.qtdQuadradosLimpos + 1
            self.qtdMovimentos = self.qtdMovimentos + 1
            ambiente.setPosicaoAgente(posXY)
        elif self.lista_percepcoes[PontosCardeais.LESTE.value] == EstadoQuadrado.SUJO.value: 
            posXY.Y = posXY.Y-1
            ambiente.limparQuadrado()
            self.qtdQuadradosLimpos = self.qtdQuadradosLimpos + 1
            self.qtdMovimentos = self.qtdMovimentos + 1
            ambiente.setPosicaoAgente(posXY)
        elif self.lista_percepcoes[PontosCardeais.OESTE.value] == EstadoQuadrado.SUJO.value: 
            posXY.Y = posXY.Y+1
            ambiente.limparQuadrado()
            self.qtdQuadradosLimpos = self.qtdQuadradosLimpos + 1
            self.qtdMovimentos = self.qtdMovimentos + 1
            ambiente.setPosicaoAgente(posXY)
        else:   
            #movimento aleatorio
            numeroAleatorio =random.randrange(4)
            if numeroAleatorio == 0:
                if posXY.X-1 >= 0:
                    ambiente.limparQuadrado()
                    self.qtdMovimentos = self.qtdMovimentos + 1
                    ambiente.setPosicaoAgente(PosXY(posXY.X-1,posXY.Y))
            elif numeroAleatorio == 1:
                if posXY.X+1 < len(ambiente.tabuleiro):
                    ambiente.limparQuadrado()
                    self.qtdMovimentos = self.qtdMovimentos + 1
                    ambiente.setPosicaoAgente(PosXY(posXY.X+1,posXY.Y))
            elif numeroAleatorio == 2:
                if posXY.Y-1 >= 0:
                    ambiente.limparQuadrado()
                    self.qtdMovimentos = self.qtdMovimentos + 1
                    ambiente.setPosicaoAgente(PosXY(posXY.X,posXY.Y-1))
            elif numeroAleatorio == 3:
                if posXY.Y+1 < len(ambiente.tabuleiro):
                    ambiente.limparQuadrado()
                    self.qtdMovimentos = self.qtdMovimentos + 1
                    ambiente.setPosicaoAgente(PosXY(posXY.X,posXY.Y+1))
            

    def perceber(self, ambiente):
        posXY = ambiente.getPosicaoAgente()
        PosNorte = EstadoQuadrado.IMPOSSIVEL.value
        PosSul = EstadoQuadrado.IMPOSSIVEL.value
        PosLeste = EstadoQuadrado.IMPOSSIVEL.value
        PosOeste = EstadoQuadrado.IMPOSSIVEL.value
        if posXY.X-1 >= 0:
            PosNorte = ambiente.tabuleiro[posXY.X-1][posXY.Y]
        if posXY.X+1 < len(ambiente.tabuleiro):
            PosSul = ambiente.tabuleiro[posXY.X+1][posXY.Y]
        if posXY.Y-1 >= 0:
            PosLeste = ambiente.tabuleiro[posXY.X][posXY.Y-1]
        if posXY.Y+1 < len(ambiente.tabuleiro):
            PosOeste = ambiente.tabuleiro[posXY.X][posXY.Y+1]
        self.lista_percepcoes = [PosNorte, PosSul, PosLeste, PosOeste]
        
        

    
    