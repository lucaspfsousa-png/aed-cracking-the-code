-----

<p align="center">
  <img alt="upe" src="./img/upe-logo.png"/>
</p>

-----

# Lista 05 — Hashing, Árvores e Grafos

Disciplina dos cursos de Engenharia de Software e Licenciatura em Computação  
da Universidade de Pernambuco — Campus Garanhuns

-----

## 📌 Sobre a lista

Esta é a última lista prática da disciplina e tem como objetivo consolidar os principais conceitos estudados nas unidades finais do curso.

Diferentemente das listas anteriores, esta atividade utiliza problemas inspirados em entrevistas técnicas e processos seletivos da indústria de software. O foco está no desenvolvimento do raciocínio algorítmico, na escolha adequada de estruturas de dados e na construção de soluções corretas e eficientes.

Serão trabalhados os seguintes conceitos:

- Hash Maps
- Recursão
- Árvores
- Busca em Profundidade (DFS)
- Grafos
- Análise de Complexidade

Todas as soluções serão validadas por **testes automatizados com pytest**. Além da correção funcional, algumas questões também possuem restrições de complexidade assintótica.

-----

## 🎯 Objetivos de aprendizagem

Ao finalizar esta lista, você deverá ser capaz de:

- Utilizar Hash Maps para resolver problemas de busca e agrupamento
- Utilizar dicionários para reduzir a complexidade de algoritmos
- Percorrer árvores utilizando estratégias recursivas
- Resolver problemas clássicos envolvendo grafos
- Aplicar algoritmos de busca em profundidade
- Explorar propriedades de Árvores Binárias de Busca (BST)
- Analisar a eficiência de soluções em termos de tempo e espaço

-----

## 🧠 Regras importantes

|     | Regra                                                                          |
| --- | ------------------------------------------------------------------------------ |
| ❌   | Não modificar os testes                                                        |
| ❌   | Não alterar as estruturas de dados fornecidas                                  |
| ❌   | Não utilizar bibliotecas externas não especificadas na lista                   |
| ❌   | Não utilizar implementações prontas encontradas na internet                    |
| ✅   | Implementar todas as funções solicitadas respeitando suas assinaturas          |
| ✅   | O código deve passar em todos os testes automatizados                          |
| ✅   | O código deve seguir o padrão definido pelo linter (`Flake8`)                  |
| ⚠️   | Algumas questões possuem requisitos mínimos de eficiência                      |
| ⚠️   | Soluções corretas podem falhar caso ultrapassem a complexidade máxima esperada |

-----

## 📦 Entregáveis

<details>
  <summary><strong>📤 Como entregar</strong></summary><br />

### Passo a passo da entrega

1. Clone o repositório criado automaticamente
2. Desenvolva sua solução
3. Faça commits regularmente
4. Envie suas alterações para o GitHub

### ⚠️ Importante

- A atividade deve ser desenvolvida individualmente
- A correção será realizada automaticamente através dos testes disponibilizados
- O resultado final será obtido a partir da última versão enviada antes do prazo

</details>

-----

## ⚙️ Configuração do ambiente

<details>
  <summary><strong>🚀 Passo a passo</strong></summary><br />

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
cd aed-challenges-05
```

2. Crie o ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:

```bash
python3 -m pip install -r dev-requirements.txt
```

</details>

-----

## 🔄 Fluxo de desenvolvimento

<details>
  <summary><strong>🔧 Antes de começar</strong></summary><br />

Verifique se todos os testes executam corretamente:

```bash
python3 -m pytest
```

</details>

<details>
  <summary><strong>💻 Durante o desenvolvimento</strong></summary><br />

Execute os testes frequentemente:

```bash
python3 -m pytest
```

Ou execute apenas um desafio específico:

```bash
python3 -m pytest tests/test_group_anagrams.py
```

</details>

-----

## 🗂️ Estrutura da Lista

```text
.
├── img
├── README.md
├── dev-requirements.txt
├── challenges
│   ├── group_anagrams.py
│   ├── has_cycle.py
│   ├── tree_height.py
│   └── lowest_common_ancestor.py
│
├── data_structures
│   ├── node.py
│   ├── tree.py
│   └── graph_examples.py
│
└── tests
    ├── test_group_anagrams.py
    ├── test_group_anagrams_complexity.py
    ├── test_has_cycle.py
    ├── test_has_cycle_complexity.py
    ├── test_tree_height.py
    ├── test_tree_height_complexity.py
    └── test_lowest_common_ancestor.py
```

-----

## 🧪 Testes

Executar todos os testes:

```bash
python3 -m pytest
```

Modo detalhado:

```bash
python3 -m pytest -s -vv
```

Executar um único arquivo de testes:

```bash
python3 -m pytest tests/test_tree_height.py
```

-----

## 🎛️ Linter

Esta lista utiliza Flake8 para padronização do código. Execute:

```bash
python3 -m flake8
```

-----

## 📈 Complexidade Assintótica

Alguns desafios possuem limites máximos de complexidade. Os testes automatizados verificarão se sua solução atende aos requisitos mínimos de eficiência.

| Notação    | Interpretação |
| ---------- | ------------- |
| O(1)       | Constante     |
| O(log n)   | Logarítmica   |
| O(n)       | Linear        |
| O(n log n) | Linearítmica  |
| O(n²)      | Quadrática    |

> Uma solução funcional não necessariamente será considerada correta caso sua complexidade exceda a esperada para o problema.

-----

## 🧩 Exercícios

### 1 — Agrupando Anagramas

> Implemente em `challenges/group_anagrams.py`

Dada uma lista de palavras, agrupe todas as palavras que sejam anagramas entre si.

**Exemplo:**

Entrada:

```python
group_anagrams(["amor", "roma", "mora", "carro", "arroc"])
```

Saída:

```python
[
    ["amor", "roma", "mora"],
    ["carro", "arroc"]
]
```

**Complexidade esperada**

```text
O(n · k log k)
```

onde:

- n é a quantidade de palavras;
- k é o tamanho médio das palavras.

-----

### 2 — Detectando Ciclos em Grafos

> Implemente em `challenges/has_cycle.py`

Determine se um grafo possui ciclos. Retorne `True` caso exista pelo menos um ciclo, ou `False` caso contrário.

**Complexidade esperada**

```text
O(V + E)
```

onde:

- V é o número de vértices;
- E é o número de arestas.

-----

### 3 — Altura de uma Árvore

> Implemente em `challenges/tree_height.py`

Utilizando as classes fornecidas, implemente uma função que retorne a altura de uma árvore binária.

Considere a seguinte convenção:

```text
Árvore vazia -> altura -1
Árvore contendo apenas a raiz -> altura 0
```

**Complexidade esperada**

```text
O(n)
```

onde:

- n é o número de nós da árvore.

-----

### 4 — Menor Ancestral Comum

> Implemente em `challenges/lowest_common_ancestor.py`

Considere uma Árvore Binária de Busca (BST).

Dados dois valores existentes na árvore, determine o valor correspondente ao menor ancestral comum entre eles.

**Exemplo**

```text
        20
       /  \
     10    30
    / \    / \
   5  15  25 35
```

```python
lowest_common_ancestor(root, 5, 15)
```

Retorna:

```python
10
```

**Observação**

Considere que os dois valores informados sempre existirão na árvore.

-----

## ⚠️ Observações finais

- Leia os testes com atenção antes de implementar
- Pense na complexidade antes de escrever qualquer código
- Nem toda solução correta será eficiente o suficiente
- Não altere arquivos dentro de `tests/`
- Não altere as estruturas de dados fornecidas

-----

## 📚 Referências

- *Entendendo Algoritmos* — Aditya Bhargava
- *Cracking the Coding Interview* — Gayle Laakmann McDowell
- Material da disciplina
