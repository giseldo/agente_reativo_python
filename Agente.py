from EstadoQuadrado import EstadoQuadrado
from PontosCardeais import PontosCardeais
from PosXY import PosXY

class Agente:
    
    lista_percepcoes = list()

    def __init__(self) -> None:
        pass


    # acao do agente a partir das percepcoes ele envia uma mensagem para o ambiente para limpar e mover
    def acao(self, ambiente):
        posXY = ambiente.getPosicaoAgente()
        if self.lista_percepcoes[PontosCardeais.NORTE.value] == EstadoQuadrado.SUJO.value: 
            posXY.X = posXY.X-1
        elif self.lista_percepcoes[PontosCardeais.SUL.value] == EstadoQuadrado.SUJO.value: 
            posXY.X = posXY.X+1
        elif self.lista_percepcoes[PontosCardeais.LESTE.value] == EstadoQuadrado.SUJO.value: 
            posXY.Y = posXY.Y-1
        elif self.lista_percepcoes[PontosCardeais.OESTE.value] == EstadoQuadrado.SUJO.value: 
            posXY.Y = posXY.Y+1
        ambiente.limparQuadrado()
        ambiente.setPosicaoAgente(posXY)
            

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
        
        

    
    