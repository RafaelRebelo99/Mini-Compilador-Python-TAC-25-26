parser grammar fase_3_parser;

options { tokenVocab = fase_2_lexer; }

code : stat* EOF ;

stat : expr NEWLINE ;

expr : ids
     | numeros
     | operacoesComExpressoes
     | expressoesEntreParenteses
     ;

ids : ID ;

numeros : INT_LIT
        | FLOAT_LIT
        | HEX_LIT
        | OCT_LIT
        | BIN_LIT
        | COMPLEX_LIT
        ;

operacoesComExpressoes : expr (PLUS | MINUS | STAR | SLASH | DOUBLE_SLASH | PERCENT | DOUBLE_STAR) expr ;

expressoesEntreParenteses : LPAREN expr RPAREN ;
