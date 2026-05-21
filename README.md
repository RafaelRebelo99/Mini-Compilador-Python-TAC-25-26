# Mini-Compilador-Python-TAC-25-26

# Mini Compilador em Python

Um mini compilador pedagógico desenvolvido em Python para transformar uma linguagem de programação customizada em [código alvo, ex: Python Bytecode / C / Assembly / Resultado Executável]. 

O objetivo principal deste projeto é entender os fundamentos da teoria dos compiladores, aplicando conceitos de análise léxica, sintática e geração de código.

---

## 🚀 O Pipeline do Compilador

O projeto foi estruturado seguindo as etapas clássicas de construção de um compilador:

1. **Análise Léxica (Lexer):** Lê o código-fonte (string) e o quebra em uma sequência de unidades significativas chamadas *Tokens*.
2. **Análise Sintática (Parser):** Consome os tokens e verifica se eles seguem as regras gramaticais da linguagem, construindo uma **Árvore de Sintaxe Abstrata (AST)**.
3. **Análise Semântica:** Garante que o código faz sentido lógico (ex: checagem de tipos e se as variáveis foram declaradas).
4. **Geração de Código:** Percorre a AST e gera o resultado final esperado.

---

## 🛠️ Tecnologias Utilizadas:


---

## 📐 Sintaxe da Linguagem

A linguagem suporta as seguintes operações básicas (exemplo):

```[nome_da_linguagem]
# Exemplo de código na nova linguagem
x = 10
y = 5
resultado = (x + y) * 2
print resultado
