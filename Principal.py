from PosXY import PosXY
from Util import Util
from Ambiente import Ambiente
from Agente import Agente

agente = Agente()
ambiente = Ambiente(5)
util = Util()

# coloca o agente no ambiente
ambiente.setPosicaoAgente(PosXY(1, 1))

util.imprimir(ambiente, agente)

while True:
    agente.perceber(ambiente)
    agente.acao(ambiente)
    util.imprimir(ambiente, agente)



