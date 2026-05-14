parser grammar fase_3_parser;

options { tokenVocab = fase_2_lexer; }

code : stat* EOF ;

stat : expr NEWLINE ;

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
