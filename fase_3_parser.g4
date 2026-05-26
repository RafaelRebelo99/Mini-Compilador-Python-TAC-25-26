parser grammar fase_3_parser;

options { tokenVocab = fase_2_lexer; }

code : (stat | condicional | func | func_call NEWLINE | loop_while | loop_for)* EOF ;

stat : (expr | query) NEWLINE
     | BREAK NEWLINE
     | CONTINUE NEWLINE
     | RETURN expr? NEWLINE
     ;

expr : expr OP expr         
     | OP expr              
     | LPAREN expr RPAREN   
     | func_call
     | ids
     | numeros
     ;

ids : ID ;

numeros : INT_LIT
        | FLOAT_LIT
        | HEX_LIT
        | OCT_LIT
        | BIN_LIT
        | COMPLEX_LIT
        ;

query : query (AND | OR | AMPERSAND | PIPE | CARET) query
      | NOT query
      | TILDE query
      | LPAREN query RPAREN
      | valoresBooleanos
      | relacoesEntreExpressoes
      | func_call
      ;

valoresBooleanos : TRUE | FALSE ;

relacoesEntreExpressoes : expr (EQ | NEQ | LT | GT | LTE | GTE) expr ;

corpo : stat | func | condicional | loop_while | loop_for ;

condicional : IF query COLON NEWLINE corpo+
              (ELIF query COLON NEWLINE corpo+)* //fase 5
              (ELSE COLON NEWLINE corpo+)?
            ;

tipo : INT_TYPE | FLOAT_TYPE | STR_TYPE | BOOL_TYPE | ID ;
                                                           //fase 6
func : DEF ID LPAREN params? RPAREN (ARROW tipo)? COLON NEWLINE corpo+ ;

params : param (COMMA param)* ;

param : ID (COLON tipo)? ;

func_call : ID LPAREN args? RPAREN ;

args : expr (COMMA expr)* ;
                                                           //fase 6.5
loop_while : WHILE query COLON NEWLINE corpo+ ;
                                                           //fase 6.75
loop_for : FOR ID IN expr COLON NEWLINE corpo+ ;


/* Exercício Fase 6.5:

while (True & g(x)):
    def f(x: int) -> float:
        if x > h(x):
            break
        else:
            continue
        return x
    -x + 1. * (0j)
    x
    */

/*Exercício Fase 6.75:
if __name__ == "__main__":
    for i in range(10):
        range(10, 20)
        range(1, 10, 3)
        for i, j in zip(range(1, 11, 2), range(2, 11, 2)):
            print(i, j)
    else:
        print("não deu certo") */