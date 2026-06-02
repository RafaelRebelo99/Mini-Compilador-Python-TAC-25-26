# 🤖 Mini-Compilador-Python-TAC-25-26

Um mini compilador pedagógico que utiliza o **ANTLR4** (ANother Tool for Language Recognition) para o parsing da gramática e **Python** para a lógica de geração de código/execução.

O objetivo deste projeto é entender o funcionamento de um compilador moderno, automatizando a criação do Lexer e do Parser por meio de uma gramática formal.

---


## 🏗️ O Pipeline do Compilador 

O projeto foi estruturado seguindo as etapas clássicas de construção de um compilador:

1. **Análise Léxica (Lexer):** Definimos as regras léxicas e sintáticas em um único arquivo.
2. **Análise Sintática (Parser):** Consome os tokens e verifica se eles seguem as regras gramaticais da linguagem, construindo uma **Árvore de Sintaxe Abstrata (AST)**.  O ANTLR lê o `.g4` e gera os arquivos, segundo a árvore de análise sintática (Parse Tree).
3. **Análise Semântica:** Garante que o código faz sentido lógico.
4. **Geração de Código:** Em Python, estendemos a classe gerada pelo ANTLR para "visitar" cada nó da árvore e realizar a análise semântica ou a geração do código alvo.

---

## 🛠️ Tecnologias Utilizadas: 

 **ANTLR4 🧬** (ANother Tool for Language Recognition) para o parsing da gramática.

**Python ⚙️** para a lógica de geração de código/execução.

---

## 📐 Sintaxe da Linguagem

Lista de "checkboxes" com coisas que o compilador consegue fazer:

```[check_list]
- [x] Declaração e atribuição de variáveis (`x = 10;`)
- [x] Operações aritméticas básicas (`+`, `-`, `*`, `/`)
- [x] Estruturas de decisão (`if` / `else`)
- [x] Loops e repetições (`while`)
- [x] Função interna de output (`print()`)

A linguagem suporta este codigo (exemplo):

```[nome_da_linguagem]
# Exemplo de código na nova linguagem
x = 10
y = 5
resultado = (x + y) * 2
print resultado
