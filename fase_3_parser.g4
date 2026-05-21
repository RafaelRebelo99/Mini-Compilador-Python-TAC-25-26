parser grammar fase_3_parser;

options { tokenVocab = fase_2_lexer; }

code : (stat | condicional)* EOF ;

stat : (expr | query) NEWLINE ;

expr : expr OP expr         // operacoesComExpressoes
     | LPAREN expr RPAREN   // expressoesEntreParenteses
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

query : query (AND | OR) query
      | NOT query
      | LPAREN query RPAREN
      | valoresBooleanos
      | relacoesEntreExpressoes
      ;

valoresBooleanos : TRUE | FALSE ;

relacoesEntreExpressoes : expr (EQ | NEQ | LT | GT | LTE | GTE) expr ;

condicional : IF query COLON NEWLINE stat+
              (ELIF query COLON NEWLINE stat+)*
              (ELSE COLON NEWLINE stat+)?
            ;
