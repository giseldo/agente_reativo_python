from PosXY import PosXY
from Util import Util
from Ambiente import Ambiente
from Agente import Agente

agente = Agente()
ambiente = Ambiente(2)
util = Util()

posXY = PosXY()
posXY.X = 0
posXY.Y = 0
ambiente.setPosicaoAgente(posXY)
util.imprimir(ambiente, agente)

while True:
    agente.perceber(ambiente)
    agente.acao(ambiente)
    util.imprimir(ambiente, agente)



