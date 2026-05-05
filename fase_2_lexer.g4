lexer grammar PythonLexer;


// PALAVRAS-CHAVE - IDENTIFICADORES DE BLOCOS

IF          : 'if' ;
ELIF        : 'elif' ;
ELSE        : 'else' ;
FOR         : 'for' ;
WHILE       : 'while' ;
DEF         : 'def' ;
CLASS       : 'class' ;
TRY         : 'try' ;
EXCEPT      : 'except' ;
FINALLY     : 'finally' ;
WITH        : 'with' ;
MATCH       : 'match' ;
CASE        : 'case' ;


// PALAVRAS-CHAVE - TIPOS DE DADOS

INT_TYPE        : 'int' ;
FLOAT_TYPE      : 'float' ;
STR_TYPE        : 'str' ;
BOOL_TYPE       : 'bool' ;
LIST_TYPE       : 'list' ;
TUPLE_TYPE      : 'tuple' ;
DICT_TYPE       : 'dict' ;
SET_TYPE        : 'set' ;
FROZENSET_TYPE  : 'frozenset' ;
COMPLEX_TYPE    : 'complex' ;
BYTES_TYPE      : 'bytes' ;
BYTEARRAY_TYPE  : 'bytearray' ;
MEMORYVIEW_TYPE : 'memoryview' ;
NONETYPE        : 'NoneType' ;

// PALAVRAS-CHAVE - OPERADORES BOOLEANOS

AND         : 'and' ;
OR          : 'or' ;
NOT         : 'not' ;
IN          : 'in' ;
IS          : 'is' ;

// DEMAIS PALAVRAS-CHAVE

IMPORT      : 'import' ;
FROM        : 'from' ;
AS          : 'as' ;
RETURN      : 'return' ;
YIELD       : 'yield' ;
PASS        : 'pass' ;
BREAK       : 'break' ;
CONTINUE    : 'continue' ;
DEL         : 'del' ;
GLOBAL      : 'global' ;
NONLOCAL    : 'nonlocal' ;
RAISE       : 'raise' ;
ASSERT      : 'assert' ;
LAMBDA      : 'lambda' ;
TRUE        : 'True' ;
FALSE       : 'False' ;
NONE        : 'None' ;
ASYNC       : 'async' ;
AWAIT       : 'await' ;


// OPERADORES ARITMÉTICOS (tokens mais longos primeiro)

DOUBLE_STAR : '**' ;
DOUBLE_SLASH: '//' ;
PLUS        : '+' ;
MINUS       : '-' ;
STAR        : '*' ;
SLASH       : '/' ;
PERCENT     : '%' ;


// OPERADORES RELACIONAIS (tokens mais longos primeiro)

EQ          : '==' ;
NEQ         : '!=' ;
LTE         : '<=' ;
GTE         : '>=' ;
LT          : '<' ;
GT          : '>' ;


// OPERADORES BITWISE (tokens mais longos primeiro)

LSHIFT      : '<<' ;
RSHIFT      : '>>' ;
AMPERSAND   : '&' ;
PIPE        : '|' ;
CARET       : '^' ;
TILDE       : '~' ;

// OPERADORES DE ATRIBUIÇÃO (tokens mais longos primeiro)

DOUBLE_SLASH_EQ : '//=' ;
DOUBLE_STAR_EQ  : '**=' ;
LSHIFT_EQ       : '<<=' ;
RSHIFT_EQ       : '>>=' ;
WALRUS          : ':=' ;
PLUS_EQ         : '+=' ;
MINUS_EQ        : '-=' ;
STAR_EQ         : '*=' ;
SLASH_EQ        : '/=' ;
PERCENT_EQ      : '%=' ;
AMPERSAND_EQ    : '&=' ;
PIPE_EQ         : '|=' ;
CARET_EQ        : '^=' ;
ASSIGN          : '=' ;


// DELIMITADORES E PONTUAÇÃO

ARROW       : '->' ;
ELLIPSIS    : '...' ;
COLON       : ':' ;
COMMA       : ',' ;
DOT         : '.' ;
SEMICOLON   : ';' ;
AT          : '@' ;

LPAREN      : '(' ;
RPAREN      : ')' ;
LBRACKET    : '[' ;
RBRACKET    : ']' ;
LBRACE      : '{' ;
RBRACE      : '}' ;

// LITERAIS


// Strings (triple-quoted antes de single-quoted para maximal munch)
STRING      : '"""' .*? '"""'
            | '\'\'\'' .*? '\'\'\''
            | '"' (~["\\\r\n] | '\\' .)* '"'
            | '\'' (~['\\\r\n] | '\\' .)* '\''
            ;

// Números complexos, floats e inteiros com prefixo (mais específicos primeiro)
COMPLEX_LIT : ([0-9]+ ('.' [0-9]*)? | '.' [0-9]+) [jJ] ;

FLOAT_LIT   : [0-9]+ '.' [0-9]*
            | '.' [0-9]+
            | [0-9]+ ('.' [0-9]*)? [eE] [+-]? [0-9]+
            ;

HEX_LIT     : '0' [xX] [0-9a-fA-F]+ ;
OCT_LIT     : '0' [oO] [0-7]+ ;
BIN_LIT     : '0' [bB] [01]+ ;
INT_LIT     : [0-9]+ ;

// Comentários (ignorados)
COMMENT     : '#' ~[\r\n]* -> skip ;


// IDENTIFICADORES, LETRAS, DÍGITOS E WS (nesta ordem, no final)

ID          : LETTER (LETTER | DIGIT)* ;
fragment LETTER : [a-zA-Z_] ;
fragment DIGIT  : [0-9] ;
WS          : [ \t\r\n]+ -> skip ;
