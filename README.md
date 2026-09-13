# FlyFood

Projeto da disciplina PISI2 — Desenvolvimento de um algoritmo de roteamento para entregas com drones.

## Contexto

No ano de 2030, o trânsito está caótico e as empresas de delivery não conseguem mais fazer entregas em um tempo aceitável. Um ex-aluno do BSI-UFRPE cria a empresa **FlyFood**, que realiza entregas utilizando drones.

Os drones podem sair do local de origem do pedido com vários pedidos no compartimento de carga e entregá-los em vários endereços espalhados pela cidade. Porém, a capacidade das baterias ainda é um problema, então é preciso otimizar ao máximo o trajeto do drone para concluir todas as entregas dentro do ciclo da bateria.

O objetivo é elaborar um **algoritmo de roteamento**: um algoritmo capaz de definir o menor trajeto para a realização de todas as entregas do drone.

## Modelagem

Para abstrair as questões de encontrar endereços e obter coordenadas GPS, o problema utiliza uma **matriz** que representa os pontos da cidade:

- O ponto R é considerado, por convenção, a **origem** e o **retorno**, sendo representado pela coord. (0, 0).
- Cada ponto de entrega é identificado por uma letra ('A', 'B', 'C', 'D', ...).

O drone **não anda na diagonal** — ele só percorre a matriz na horizontal ou na vertical. A distância é medida em **dronômetros**.

## Formato de entrada

O algoritmo deve ler uma matriz a partir de um arquivo, contendo os pontos de entrega e o ponto de origem/retorno.

## Saída esperada

Deve ser retornada a **ordem em que o drone deve percorrer os pontos de entrega** — a de **menor custo** (menor distância em dronômetros).

A resposta é a sequência de pontos (em forma de string) que produz o menor circuito possível, partindo e retornando ao ponto 'R'. O ponto 'R' **não precisa ser incluído** na sequência de resposta.