# Agente Reativo


Esse Agente de Limpeza é do tipo "agente reativo", ele só reage se vir sujeira. Se ele não vir sujeira ele se move aleatoriamente. Mas ele ainda não leva em conta o "Objetivo" que é "deixar tudo limpo". Com novas técnicas de "busca" poderemos alterá-lo para incluir um objetivo de "deixar tudo limpo" e assim o classificaremos de "agente baseado em objetivo" no futuro, mas esse ainda não é o caso.

A classe principal é um loop que inicia os métodos de perceber e de agir do agente. Existe uma certa dependência entre o agente e o ambiente indesejada nesse código. O repositório https://github.com/giseldo/agente_dirigido_por_tabela tem uma versão mais elegante com independência entre o agente e o ambiente, e descreve um cenário mais simples. 

```
agente = Agente()
ambiente = Ambiente(5)
util = Util()

ambiente.setPosicaoAgente(PosXY(1, 1))

util.imprimir(ambiente, agente)

while True:
    agente.perceber(ambiente)
    agente.acao(ambiente)
    util.imprimir(ambiente, agente)
```

Para executar

```
python Principal.py
```

Saída esperada

```
Medida de desempenho: Quantidade de quadrados limpos: 2
Custo: Quantidade de movimentos realizados: 2
[[8. 0. 1. 1. 1.]
 [1. 0. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
 
Medida de desempenho: Quantidade de quadrados limpos: 3
Custo: Quantidade de movimentos realizados: 3
[[0. 0. 1. 1. 1.]
 [8. 0. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
```
Legenda
#### 1 = Tem Sujeira no quadrado
#### 0 = O Quadrado Limpo
#### 8 = É o agente

Este arquivo pode ser facilmente executado com a IDE na nuvem https://repl.it
Basta selecionar a opção Run no Repl.it
