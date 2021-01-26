from PosXY import PosXY
from Util import Util
from Ambiente import Ambiente
from Agente import Agente

agente = Agente()
ambiente = Ambiente(4)
util = Util()

posXY = PosXY()
posXY.X = 1
posXY.Y = 1
ambiente.setPosicaoAgente(posXY)
util.imprimir(ambiente)

while True:
    agente.perceber(ambiente)
    agente.acao(ambiente)
    util.imprimir(ambiente)



