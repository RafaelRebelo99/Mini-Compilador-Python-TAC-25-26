parser grammar fase_3_parser;

options { tokenVocab = fase_2_lexer; }

code : (NEWLINE | stat | condicional | func | func_call NEWLINE | loop_while | loop_for)* EOF ;

stat : assign NEWLINE
     | (expr | query) NEWLINE
     | BREAK NEWLINE
     | CONTINUE NEWLINE
     | RETURN expr? NEWLINE
     ;

assign : ID (ASSIGN) expr ;

expr : expr OP expr
     | OP expr
     | LPAREN expr RPAREN
     | func_call
     | ids
     | numeros
     | STRING
     | lista                                                   
     | tupla
     | set_lit
     | dicionario
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
                                                           //fase 7
loop_while : WHILE query COLON NEWLINE corpo+ ;
                                                           
loop_for : FOR for_vars IN expr COLON NEWLINE corpo+
           (ELSE COLON NEWLINE corpo+)? ;

for_vars : ID (COMMA ID)* ;
                                                           //fase 8
lista      : LBRACKET (expr (COMMA expr)*)? RBRACKET ;

tupla      : LPAREN expr COMMA (expr (COMMA expr)*)? RPAREN ;

set_lit    : LBRACE expr (COMMA expr)+ RBRACE ;

dicionario : LBRACE (expr COLON expr (COMMA expr COLON expr)*)? RBRACE ;

