# Agente Reativo


Esse Agente de Limpeza é do tipo "agente reativo", ele só reage se vir sujeira. Se ele não vir sujeira ele se move aleatoriamente. Mas ele ainda não leva em conta o "Objetivo" que é "deixar tudo limpo". Com novas técnicas de "busca" poderemos alterá-lo para incluir um objetivo de "deixar tudo limpo" e assim o classificaremos de "agente baseado em objetivo" no futuro, mas esse ainda não é o caso.

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
1 = Tem Sujeira no quadrado
0 = O Quadrado Limpo
8 = É o agente
