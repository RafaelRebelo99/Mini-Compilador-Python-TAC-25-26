# Generated from fase_3_parser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,102,328,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,5,0,58,8,0,10,0,12,0,61,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,3,1,70,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,80,8,1,1,1,3,1,
        83,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,3,3,104,8,3,1,3,1,3,1,3,5,3,109,8,3,10,3,12,3,
        112,9,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,3,6,130,8,6,1,6,1,6,1,6,5,6,135,8,6,10,6,12,6,138,9,6,1,
        7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,151,8,9,1,10,1,10,
        1,10,1,10,1,10,4,10,158,8,10,11,10,12,10,159,1,10,1,10,1,10,1,10,
        1,10,4,10,167,8,10,11,10,12,10,168,5,10,171,8,10,10,10,12,10,174,
        9,10,1,10,1,10,1,10,1,10,4,10,180,8,10,11,10,12,10,181,3,10,184,
        8,10,1,11,1,11,1,12,1,12,1,12,1,12,3,12,192,8,12,1,12,1,12,1,12,
        3,12,197,8,12,1,12,1,12,1,12,4,12,202,8,12,11,12,12,12,203,1,13,
        1,13,1,13,5,13,209,8,13,10,13,12,13,212,9,13,1,14,1,14,1,14,3,14,
        217,8,14,1,15,1,15,1,15,3,15,222,8,15,1,15,1,15,1,16,1,16,1,16,5,
        16,229,8,16,10,16,12,16,232,9,16,1,17,1,17,1,17,1,17,1,17,4,17,239,
        8,17,11,17,12,17,240,1,18,1,18,1,18,1,18,1,18,1,18,1,18,4,18,250,
        8,18,11,18,12,18,251,1,18,1,18,1,18,1,18,4,18,258,8,18,11,18,12,
        18,259,3,18,262,8,18,1,19,1,19,1,19,5,19,267,8,19,10,19,12,19,270,
        9,19,1,20,1,20,1,20,1,20,5,20,276,8,20,10,20,12,20,279,9,20,3,20,
        281,8,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,5,21,291,8,21,10,
        21,12,21,294,9,21,3,21,296,8,21,1,21,1,21,1,22,1,22,1,22,1,22,4,
        22,304,8,22,11,22,12,22,305,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,
        23,1,23,1,23,1,23,5,23,319,8,23,10,23,12,23,322,9,23,3,23,324,8,
        23,1,23,1,23,1,23,0,2,6,12,24,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,0,5,1,0,93,98,2,0,28,29,61,63,1,
        0,47,48,1,0,53,58,2,0,14,17,100,100,360,0,59,1,0,0,0,2,82,1,0,0,
        0,4,84,1,0,0,0,6,103,1,0,0,0,8,113,1,0,0,0,10,115,1,0,0,0,12,129,
        1,0,0,0,14,139,1,0,0,0,16,141,1,0,0,0,18,150,1,0,0,0,20,152,1,0,
        0,0,22,185,1,0,0,0,24,187,1,0,0,0,26,205,1,0,0,0,28,213,1,0,0,0,
        30,218,1,0,0,0,32,225,1,0,0,0,34,233,1,0,0,0,36,242,1,0,0,0,38,263,
        1,0,0,0,40,271,1,0,0,0,42,284,1,0,0,0,44,299,1,0,0,0,46,309,1,0,
        0,0,48,58,5,101,0,0,49,58,3,2,1,0,50,58,3,20,10,0,51,58,3,24,12,
        0,52,53,3,30,15,0,53,54,5,101,0,0,54,58,1,0,0,0,55,58,3,34,17,0,
        56,58,3,36,18,0,57,48,1,0,0,0,57,49,1,0,0,0,57,50,1,0,0,0,57,51,
        1,0,0,0,57,52,1,0,0,0,57,55,1,0,0,0,57,56,1,0,0,0,58,61,1,0,0,0,
        59,57,1,0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,62,63,5,
        0,0,1,63,1,1,0,0,0,64,65,3,4,2,0,65,66,5,101,0,0,66,83,1,0,0,0,67,
        70,3,6,3,0,68,70,3,12,6,0,69,67,1,0,0,0,69,68,1,0,0,0,70,71,1,0,
        0,0,71,72,5,101,0,0,72,83,1,0,0,0,73,74,5,39,0,0,74,83,5,101,0,0,
        75,76,5,40,0,0,76,83,5,101,0,0,77,79,5,36,0,0,78,80,3,6,3,0,79,78,
        1,0,0,0,79,80,1,0,0,0,80,81,1,0,0,0,81,83,5,101,0,0,82,64,1,0,0,
        0,82,69,1,0,0,0,82,73,1,0,0,0,82,75,1,0,0,0,82,77,1,0,0,0,83,3,1,
        0,0,0,84,85,5,100,0,0,85,86,5,78,0,0,86,87,3,6,3,0,87,5,1,0,0,0,
        88,89,6,3,-1,0,89,90,5,52,0,0,90,104,3,6,3,10,91,92,5,86,0,0,92,
        93,3,6,3,0,93,94,5,87,0,0,94,104,1,0,0,0,95,104,3,30,15,0,96,104,
        3,8,4,0,97,104,3,10,5,0,98,104,5,92,0,0,99,104,3,40,20,0,100,104,
        3,42,21,0,101,104,3,44,22,0,102,104,3,46,23,0,103,88,1,0,0,0,103,
        91,1,0,0,0,103,95,1,0,0,0,103,96,1,0,0,0,103,97,1,0,0,0,103,98,1,
        0,0,0,103,99,1,0,0,0,103,100,1,0,0,0,103,101,1,0,0,0,103,102,1,0,
        0,0,104,110,1,0,0,0,105,106,10,11,0,0,106,107,5,52,0,0,107,109,3,
        6,3,12,108,105,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,110,111,1,
        0,0,0,111,7,1,0,0,0,112,110,1,0,0,0,113,114,5,100,0,0,114,9,1,0,
        0,0,115,116,7,0,0,0,116,11,1,0,0,0,117,118,6,6,-1,0,118,119,5,30,
        0,0,119,130,3,12,6,6,120,121,5,64,0,0,121,130,3,12,6,5,122,123,5,
        86,0,0,123,124,3,12,6,0,124,125,5,87,0,0,125,130,1,0,0,0,126,130,
        3,14,7,0,127,130,3,16,8,0,128,130,3,30,15,0,129,117,1,0,0,0,129,
        120,1,0,0,0,129,122,1,0,0,0,129,126,1,0,0,0,129,127,1,0,0,0,129,
        128,1,0,0,0,130,136,1,0,0,0,131,132,10,7,0,0,132,133,7,1,0,0,133,
        135,3,12,6,8,134,131,1,0,0,0,135,138,1,0,0,0,136,134,1,0,0,0,136,
        137,1,0,0,0,137,13,1,0,0,0,138,136,1,0,0,0,139,140,7,2,0,0,140,15,
        1,0,0,0,141,142,3,6,3,0,142,143,7,3,0,0,143,144,3,6,3,0,144,17,1,
        0,0,0,145,151,3,2,1,0,146,151,3,24,12,0,147,151,3,20,10,0,148,151,
        3,34,17,0,149,151,3,36,18,0,150,145,1,0,0,0,150,146,1,0,0,0,150,
        147,1,0,0,0,150,148,1,0,0,0,150,149,1,0,0,0,151,19,1,0,0,0,152,153,
        5,1,0,0,153,154,3,12,6,0,154,155,5,81,0,0,155,157,5,101,0,0,156,
        158,3,18,9,0,157,156,1,0,0,0,158,159,1,0,0,0,159,157,1,0,0,0,159,
        160,1,0,0,0,160,172,1,0,0,0,161,162,5,2,0,0,162,163,3,12,6,0,163,
        164,5,81,0,0,164,166,5,101,0,0,165,167,3,18,9,0,166,165,1,0,0,0,
        167,168,1,0,0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,171,1,0,0,0,
        170,161,1,0,0,0,171,174,1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,
        173,183,1,0,0,0,174,172,1,0,0,0,175,176,5,3,0,0,176,177,5,81,0,0,
        177,179,5,101,0,0,178,180,3,18,9,0,179,178,1,0,0,0,180,181,1,0,0,
        0,181,179,1,0,0,0,181,182,1,0,0,0,182,184,1,0,0,0,183,175,1,0,0,
        0,183,184,1,0,0,0,184,21,1,0,0,0,185,186,7,4,0,0,186,23,1,0,0,0,
        187,188,5,6,0,0,188,189,5,100,0,0,189,191,5,86,0,0,190,192,3,26,
        13,0,191,190,1,0,0,0,191,192,1,0,0,0,192,193,1,0,0,0,193,196,5,87,
        0,0,194,195,5,79,0,0,195,197,3,22,11,0,196,194,1,0,0,0,196,197,1,
        0,0,0,197,198,1,0,0,0,198,199,5,81,0,0,199,201,5,101,0,0,200,202,
        3,18,9,0,201,200,1,0,0,0,202,203,1,0,0,0,203,201,1,0,0,0,203,204,
        1,0,0,0,204,25,1,0,0,0,205,210,3,28,14,0,206,207,5,82,0,0,207,209,
        3,28,14,0,208,206,1,0,0,0,209,212,1,0,0,0,210,208,1,0,0,0,210,211,
        1,0,0,0,211,27,1,0,0,0,212,210,1,0,0,0,213,216,5,100,0,0,214,215,
        5,81,0,0,215,217,3,22,11,0,216,214,1,0,0,0,216,217,1,0,0,0,217,29,
        1,0,0,0,218,219,5,100,0,0,219,221,5,86,0,0,220,222,3,32,16,0,221,
        220,1,0,0,0,221,222,1,0,0,0,222,223,1,0,0,0,223,224,5,87,0,0,224,
        31,1,0,0,0,225,230,3,6,3,0,226,227,5,82,0,0,227,229,3,6,3,0,228,
        226,1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,230,231,1,0,0,0,231,
        33,1,0,0,0,232,230,1,0,0,0,233,234,5,5,0,0,234,235,3,12,6,0,235,
        236,5,81,0,0,236,238,5,101,0,0,237,239,3,18,9,0,238,237,1,0,0,0,
        239,240,1,0,0,0,240,238,1,0,0,0,240,241,1,0,0,0,241,35,1,0,0,0,242,
        243,5,4,0,0,243,244,3,38,19,0,244,245,5,31,0,0,245,246,3,6,3,0,246,
        247,5,81,0,0,247,249,5,101,0,0,248,250,3,18,9,0,249,248,1,0,0,0,
        250,251,1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,252,261,1,0,0,0,
        253,254,5,3,0,0,254,255,5,81,0,0,255,257,5,101,0,0,256,258,3,18,
        9,0,257,256,1,0,0,0,258,259,1,0,0,0,259,257,1,0,0,0,259,260,1,0,
        0,0,260,262,1,0,0,0,261,253,1,0,0,0,261,262,1,0,0,0,262,37,1,0,0,
        0,263,268,5,100,0,0,264,265,5,82,0,0,265,267,5,100,0,0,266,264,1,
        0,0,0,267,270,1,0,0,0,268,266,1,0,0,0,268,269,1,0,0,0,269,39,1,0,
        0,0,270,268,1,0,0,0,271,280,5,88,0,0,272,277,3,6,3,0,273,274,5,82,
        0,0,274,276,3,6,3,0,275,273,1,0,0,0,276,279,1,0,0,0,277,275,1,0,
        0,0,277,278,1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,0,280,272,1,0,
        0,0,280,281,1,0,0,0,281,282,1,0,0,0,282,283,5,89,0,0,283,41,1,0,
        0,0,284,285,5,86,0,0,285,286,3,6,3,0,286,295,5,82,0,0,287,292,3,
        6,3,0,288,289,5,82,0,0,289,291,3,6,3,0,290,288,1,0,0,0,291,294,1,
        0,0,0,292,290,1,0,0,0,292,293,1,0,0,0,293,296,1,0,0,0,294,292,1,
        0,0,0,295,287,1,0,0,0,295,296,1,0,0,0,296,297,1,0,0,0,297,298,5,
        87,0,0,298,43,1,0,0,0,299,300,5,90,0,0,300,303,3,6,3,0,301,302,5,
        82,0,0,302,304,3,6,3,0,303,301,1,0,0,0,304,305,1,0,0,0,305,303,1,
        0,0,0,305,306,1,0,0,0,306,307,1,0,0,0,307,308,5,91,0,0,308,45,1,
        0,0,0,309,323,5,90,0,0,310,311,3,6,3,0,311,312,5,81,0,0,312,320,
        3,6,3,0,313,314,5,82,0,0,314,315,3,6,3,0,315,316,5,81,0,0,316,317,
        3,6,3,0,317,319,1,0,0,0,318,313,1,0,0,0,319,322,1,0,0,0,320,318,
        1,0,0,0,320,321,1,0,0,0,321,324,1,0,0,0,322,320,1,0,0,0,323,310,
        1,0,0,0,323,324,1,0,0,0,324,325,1,0,0,0,325,326,5,91,0,0,326,47,
        1,0,0,0,34,57,59,69,79,82,103,110,129,136,150,159,168,172,181,183,
        191,196,203,210,216,221,230,240,251,259,261,268,277,280,292,295,
        305,320,323
    ]

class fase_3_parser ( Parser ):

    grammarFileName = "fase_3_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'elif'", "'else'", "'for'", "'while'", 
                     "'def'", "'class'", "'try'", "'except'", "'finally'", 
                     "'with'", "'match'", "'case'", "'int'", "'float'", 
                     "'str'", "'bool'", "'list'", "'tuple'", "'dict'", "'set'", 
                     "'frozenset'", "'complex'", "'bytes'", "'bytearray'", 
                     "'memoryview'", "'NoneType'", "'and'", "'or'", "'not'", 
                     "'in'", "'is'", "'import'", "'from'", "'as'", "'return'", 
                     "'yield'", "'pass'", "'break'", "'continue'", "'del'", 
                     "'global'", "'nonlocal'", "'raise'", "'assert'", "'lambda'", 
                     "'True'", "'False'", "'None'", "'async'", "'await'", 
                     "<INVALID>", "'=='", "'!='", "'<='", "'>='", "'<'", 
                     "'>'", "'<<'", "'>>'", "'&'", "'|'", "'^'", "'~'", 
                     "'//='", "'**='", "'<<='", "'>>='", "':='", "'+='", 
                     "'-='", "'*='", "'/='", "'%='", "'&='", "'|='", "'^='", 
                     "'='", "'->'", "'...'", "':'", "','", "'.'", "';'", 
                     "'@'", "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELIF", "ELSE", "FOR", "WHILE", 
                      "DEF", "CLASS", "TRY", "EXCEPT", "FINALLY", "WITH", 
                      "MATCH", "CASE", "INT_TYPE", "FLOAT_TYPE", "STR_TYPE", 
                      "BOOL_TYPE", "LIST_TYPE", "TUPLE_TYPE", "DICT_TYPE", 
                      "SET_TYPE", "FROZENSET_TYPE", "COMPLEX_TYPE", "BYTES_TYPE", 
                      "BYTEARRAY_TYPE", "MEMORYVIEW_TYPE", "NONETYPE", "AND", 
                      "OR", "NOT", "IN", "IS", "IMPORT", "FROM", "AS", "RETURN", 
                      "YIELD", "PASS", "BREAK", "CONTINUE", "DEL", "GLOBAL", 
                      "NONLOCAL", "RAISE", "ASSERT", "LAMBDA", "TRUE", "FALSE", 
                      "NONE", "ASYNC", "AWAIT", "OP", "EQ", "NEQ", "LTE", 
                      "GTE", "LT", "GT", "LSHIFT", "RSHIFT", "AMPERSAND", 
                      "PIPE", "CARET", "TILDE", "DOUBLE_SLASH_EQ", "DOUBLE_STAR_EQ", 
                      "LSHIFT_EQ", "RSHIFT_EQ", "WALRUS", "PLUS_EQ", "MINUS_EQ", 
                      "STAR_EQ", "SLASH_EQ", "PERCENT_EQ", "AMPERSAND_EQ", 
                      "PIPE_EQ", "CARET_EQ", "ASSIGN", "ARROW", "ELLIPSIS", 
                      "COLON", "COMMA", "DOT", "SEMICOLON", "AT", "LPAREN", 
                      "RPAREN", "LBRACKET", "RBRACKET", "LBRACE", "RBRACE", 
                      "STRING", "COMPLEX_LIT", "FLOAT_LIT", "HEX_LIT", "OCT_LIT", 
                      "BIN_LIT", "INT_LIT", "COMMENT", "ID", "NEWLINE", 
                      "WS" ]

    RULE_code = 0
    RULE_stat = 1
    RULE_assign = 2
    RULE_expr = 3
    RULE_ids = 4
    RULE_numeros = 5
    RULE_query = 6
    RULE_valoresBooleanos = 7
    RULE_relacoesEntreExpressoes = 8
    RULE_corpo = 9
    RULE_condicional = 10
    RULE_tipo = 11
    RULE_func = 12
    RULE_params = 13
    RULE_param = 14
    RULE_func_call = 15
    RULE_args = 16
    RULE_loop_while = 17
    RULE_loop_for = 18
    RULE_for_vars = 19
    RULE_lista = 20
    RULE_tupla = 21
    RULE_set_lit = 22
    RULE_dicionario = 23

    ruleNames =  [ "code", "stat", "assign", "expr", "ids", "numeros", "query", 
                   "valoresBooleanos", "relacoesEntreExpressoes", "corpo", 
                   "condicional", "tipo", "func", "params", "param", "func_call", 
                   "args", "loop_while", "loop_for", "for_vars", "lista", 
                   "tupla", "set_lit", "dicionario" ]

    EOF = Token.EOF
    IF=1
    ELIF=2
    ELSE=3
    FOR=4
    WHILE=5
    DEF=6
    CLASS=7
    TRY=8
    EXCEPT=9
    FINALLY=10
    WITH=11
    MATCH=12
    CASE=13
    INT_TYPE=14
    FLOAT_TYPE=15
    STR_TYPE=16
    BOOL_TYPE=17
    LIST_TYPE=18
    TUPLE_TYPE=19
    DICT_TYPE=20
    SET_TYPE=21
    FROZENSET_TYPE=22
    COMPLEX_TYPE=23
    BYTES_TYPE=24
    BYTEARRAY_TYPE=25
    MEMORYVIEW_TYPE=26
    NONETYPE=27
    AND=28
    OR=29
    NOT=30
    IN=31
    IS=32
    IMPORT=33
    FROM=34
    AS=35
    RETURN=36
    YIELD=37
    PASS=38
    BREAK=39
    CONTINUE=40
    DEL=41
    GLOBAL=42
    NONLOCAL=43
    RAISE=44
    ASSERT=45
    LAMBDA=46
    TRUE=47
    FALSE=48
    NONE=49
    ASYNC=50
    AWAIT=51
    OP=52
    EQ=53
    NEQ=54
    LTE=55
    GTE=56
    LT=57
    GT=58
    LSHIFT=59
    RSHIFT=60
    AMPERSAND=61
    PIPE=62
    CARET=63
    TILDE=64
    DOUBLE_SLASH_EQ=65
    DOUBLE_STAR_EQ=66
    LSHIFT_EQ=67
    RSHIFT_EQ=68
    WALRUS=69
    PLUS_EQ=70
    MINUS_EQ=71
    STAR_EQ=72
    SLASH_EQ=73
    PERCENT_EQ=74
    AMPERSAND_EQ=75
    PIPE_EQ=76
    CARET_EQ=77
    ASSIGN=78
    ARROW=79
    ELLIPSIS=80
    COLON=81
    COMMA=82
    DOT=83
    SEMICOLON=84
    AT=85
    LPAREN=86
    RPAREN=87
    LBRACKET=88
    RBRACKET=89
    LBRACE=90
    RBRACE=91
    STRING=92
    COMPLEX_LIT=93
    FLOAT_LIT=94
    HEX_LIT=95
    OCT_LIT=96
    BIN_LIT=97
    INT_LIT=98
    COMMENT=99
    ID=100
    NEWLINE=101
    WS=102

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(fase_3_parser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(fase_3_parser.NEWLINE)
            else:
                return self.getToken(fase_3_parser.NEWLINE, i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.StatContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.StatContext,i)


        def condicional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.CondicionalContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.CondicionalContext,i)


        def func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.FuncContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.FuncContext,i)


        def func_call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.Func_callContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.Func_callContext,i)


        def loop_while(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.Loop_whileContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.Loop_whileContext,i)


        def loop_for(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.Loop_forContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.Loop_forContext,i)


        def getRuleIndex(self):
            return fase_3_parser.RULE_code

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode" ):
                return visitor.visitCode(self)
            else:
                return visitor.visitChildren(self)




    def code(self):

        localctx = fase_3_parser.CodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_code)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4927531153096818) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 240337813505) != 0):
                self.state = 57
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 48
                    self.match(fase_3_parser.NEWLINE)
                    pass

                elif la_ == 2:
                    self.state = 49
                    self.stat()
                    pass

                elif la_ == 3:
                    self.state = 50
                    self.condicional()
                    pass

                elif la_ == 4:
                    self.state = 51
                    self.func()
                    pass

                elif la_ == 5:
                    self.state = 52
                    self.func_call()
                    self.state = 53
                    self.match(fase_3_parser.NEWLINE)
                    pass

                elif la_ == 6:
                    self.state = 55
                    self.loop_while()
                    pass

                elif la_ == 7:
                    self.state = 56
                    self.loop_for()
                    pass


                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(fase_3_parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(fase_3_parser.AssignContext,0)


        def NEWLINE(self):
            return self.getToken(fase_3_parser.NEWLINE, 0)

        def expr(self):
            return self.getTypedRuleContext(fase_3_parser.ExprContext,0)


        def query(self):
            return self.getTypedRuleContext(fase_3_parser.QueryContext,0)


        def BREAK(self):
            return self.getToken(fase_3_parser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(fase_3_parser.CONTINUE, 0)

        def RETURN(self):
            return self.getToken(fase_3_parser.RETURN, 0)

        def getRuleIndex(self):
            return fase_3_parser.RULE_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = fase_3_parser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.assign()
                self.state = 65
                self.match(fase_3_parser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 67
                    self.expr(0)
                    pass

                elif la_ == 2:
                    self.state = 68
                    self.query(0)
                    pass


                self.state = 71
                self.match(fase_3_parser.NEWLINE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.match(fase_3_parser.BREAK)
                self.state = 74
                self.match(fase_3_parser.NEWLINE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.match(fase_3_parser.CONTINUE)
                self.state = 76
                self.match(fase_3_parser.NEWLINE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 77
                self.match(fase_3_parser.RETURN)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 52)) & ~0x3f) == 0 and ((1 << (_la - 52)) & 421473730691073) != 0):
                    self.state = 78
                    self.expr(0)


                self.state = 81
                self.match(fase_3_parser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(fase_3_parser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(fase_3_parser.ExprContext,0)


        def ASSIGN(self):
            return self.getToken(fase_3_parser.ASSIGN, 0)

        def getRuleIndex(self):
            return fase_3_parser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = fase_3_parser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(fase_3_parser.ID)

            self.state = 85
            self.match(fase_3_parser.ASSIGN)
            self.state = 86
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP(self):
            return self.getToken(fase_3_parser.OP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.ExprContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.ExprContext,i)


        def LPAREN(self):
            return self.getToken(fase_3_parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(fase_3_parser.RPAREN, 0)

        def func_call(self):
            return self.getTypedRuleContext(fase_3_parser.Func_callContext,0)


        def ids(self):
            return self.getTypedRuleContext(fase_3_parser.IdsContext,0)


        def numeros(self):
            return self.getTypedRuleContext(fase_3_parser.NumerosContext,0)


        def STRING(self):
            return self.getToken(fase_3_parser.STRING, 0)

        def lista(self):
            return self.getTypedRuleContext(fase_3_parser.ListaContext,0)


        def tupla(self):
            return self.getTypedRuleContext(fase_3_parser.TuplaContext,0)


        def set_lit(self):
            return self.getTypedRuleContext(fase_3_parser.Set_litContext,0)


        def dicionario(self):
            return self.getTypedRuleContext(fase_3_parser.DicionarioContext,0)


        def getRuleIndex(self):
            return fase_3_parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = fase_3_parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 89
                self.match(fase_3_parser.OP)
                self.state = 90
                self.expr(10)
                pass

            elif la_ == 2:
                self.state = 91
                self.match(fase_3_parser.LPAREN)
                self.state = 92
                self.expr(0)
                self.state = 93
                self.match(fase_3_parser.RPAREN)
                pass

            elif la_ == 3:
                self.state = 95
                self.func_call()
                pass

            elif la_ == 4:
                self.state = 96
                self.ids()
                pass

            elif la_ == 5:
                self.state = 97
                self.numeros()
                pass

            elif la_ == 6:
                self.state = 98
                self.match(fase_3_parser.STRING)
                pass

            elif la_ == 7:
                self.state = 99
                self.lista()
                pass

            elif la_ == 8:
                self.state = 100
                self.tupla()
                pass

            elif la_ == 9:
                self.state = 101
                self.set_lit()
                pass

            elif la_ == 10:
                self.state = 102
                self.dicionario()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 110
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = fase_3_parser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 105
                    if not self.precpred(self._ctx, 11):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                    self.state = 106
                    self.match(fase_3_parser.OP)
                    self.state = 107
                    self.expr(12) 
                self.state = 112
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IdsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(fase_3_parser.ID, 0)

        def getRuleIndex(self):
            return fase_3_parser.RULE_ids

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIds" ):
                return visitor.visitIds(self)
            else:
                return visitor.visitChildren(self)




    def ids(self):

        localctx = fase_3_parser.IdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ids)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(fase_3_parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumerosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(fase_3_parser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(fase_3_parser.FLOAT_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(fase_3_parser.HEX_LIT, 0)

        def OCT_LIT(self):
            return self.getToken(fase_3_parser.OCT_LIT, 0)

        def BIN_LIT(self):
            return self.getToken(fase_3_parser.BIN_LIT, 0)

        def COMPLEX_LIT(self):
            return self.getToken(fase_3_parser.COMPLEX_LIT, 0)

        def getRuleIndex(self):
            return fase_3_parser.RULE_numeros

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumeros" ):
                return visitor.visitNumeros(self)
            else:
                return visitor.visitChildren(self)




    def numeros(self):

        localctx = fase_3_parser.NumerosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_numeros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            _la = self._input.LA(1)
            if not(((((_la - 93)) & ~0x3f) == 0 and ((1 << (_la - 93)) & 63) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(fase_3_parser.NOT, 0)

        def query(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.QueryContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.QueryContext,i)


        def TILDE(self):
            return self.getToken(fase_3_parser.TILDE, 0)

        def LPAREN(self):
            return self.getToken(fase_3_parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(fase_3_parser.RPAREN, 0)

        def valoresBooleanos(self):
            return self.getTypedRuleContext(fase_3_parser.ValoresBooleanosContext,0)


        def relacoesEntreExpressoes(self):
            return self.getTypedRuleContext(fase_3_parser.RelacoesEntreExpressoesContext,0)


        def func_call(self):
            return self.getTypedRuleContext(fase_3_parser.Func_callContext,0)


        def AND(self):
            return self.getToken(fase_3_parser.AND, 0)

        def OR(self):
            return self.getToken(fase_3_parser.OR, 0)

        def AMPERSAND(self):
            return self.getToken(fase_3_parser.AMPERSAND, 0)

        def PIPE(self):
            return self.getToken(fase_3_parser.PIPE, 0)

        def CARET(self):
            return self.getToken(fase_3_parser.CARET, 0)

        def getRuleIndex(self):
            return fase_3_parser.RULE_query

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)



    def query(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = fase_3_parser.QueryContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_query, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 118
                self.match(fase_3_parser.NOT)
                self.state = 119
                self.query(6)
                pass

            elif la_ == 2:
                self.state = 120
                self.match(fase_3_parser.TILDE)
                self.state = 121
                self.query(5)
                pass

            elif la_ == 3:
                self.state = 122
                self.match(fase_3_parser.LPAREN)
                self.state = 123
                self.query(0)
                self.state = 124
                self.match(fase_3_parser.RPAREN)
                pass

            elif la_ == 4:
                self.state = 126
                self.valoresBooleanos()
                pass

            elif la_ == 5:
                self.state = 127
                self.relacoesEntreExpressoes()
                pass

            elif la_ == 6:
                self.state = 128
                self.func_call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 136
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = fase_3_parser.QueryContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_query)
                    self.state = 131
                    if not self.precpred(self._ctx, 7):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                    self.state = 132
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & -2305843008408387584) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 133
                    self.query(8) 
                self.state = 138
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ValoresBooleanosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(fase_3_parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(fase_3_parser.FALSE, 0)

        def getRuleIndex(self):
            return fase_3_parser.RULE_valoresBooleanos

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValoresBooleanos" ):
                return visitor.visitValoresBooleanos(self)
            else:
                return visitor.visitChildren(self)




    def valoresBooleanos(self):

        localctx = fase_3_parser.ValoresBooleanosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_valoresBooleanos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            _la = self._input.LA(1)
            if not(_la==47 or _la==48):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelacoesEntreExpressoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.ExprContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.ExprContext,i)


        def EQ(self):
            return self.getToken(fase_3_parser.EQ, 0)

        def NEQ(self):
            return self.getToken(fase_3_parser.NEQ, 0)

        def LT(self):
            return self.getToken(fase_3_parser.LT, 0)

        def GT(self):
            return self.getToken(fase_3_parser.GT, 0)

        def LTE(self):
            return self.getToken(fase_3_parser.LTE, 0)

        def GTE(self):
            return self.getToken(fase_3_parser.GTE, 0)

        def getRuleIndex(self):
            return fase_3_parser.RULE_relacoesEntreExpressoes

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelacoesEntreExpressoes" ):
                return visitor.visitRelacoesEntreExpressoes(self)
            else:
                return visitor.visitChildren(self)




    def relacoesEntreExpressoes(self):

        localctx = fase_3_parser.RelacoesEntreExpressoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_relacoesEntreExpressoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.expr(0)
            self.state = 142
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 567453553048682496) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 143
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CorpoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self):
            return self.getTypedRuleContext(fase_3_parser.StatContext,0)


        def func(self):
            return self.getTypedRuleContext(fase_3_parser.FuncContext,0)


        def condicional(self):
            return self.getTypedRuleContext(fase_3_parser.CondicionalContext,0)


        def loop_while(self):
            return self.getTypedRuleContext(fase_3_parser.Loop_whileContext,0)


        def loop_for(self):
            return self.getTypedRuleContext(fase_3_parser.Loop_forContext,0)


        def getRuleIndex(self):
            return fase_3_parser.RULE_corpo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCorpo" ):
                return visitor.visitCorpo(self)
            else:
                return visitor.visitChildren(self)




    def corpo(self):

        localctx = fase_3_parser.CorpoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_corpo)
        try:
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30, 36, 39, 40, 47, 48, 52, 64, 86, 88, 90, 92, 93, 94, 95, 96, 97, 98, 100]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.stat()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.func()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.condicional()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                self.loop_while()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 149
                self.loop_for()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(fase_3_parser.IF, 0)

        def query(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.QueryContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.QueryContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(fase_3_parser.COLON)
            else:
                return self.getToken(fase_3_parser.COLON, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(fase_3_parser.NEWLINE)
            else:
                return self.getToken(fase_3_parser.NEWLINE, i)

        def corpo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.CorpoContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.CorpoContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(fase_3_parser.ELIF)
            else:
                return self.getToken(fase_3_parser.ELIF, i)

        def ELSE(self):
            return self.getToken(fase_3_parser.ELSE, 0)

        def getRuleIndex(self):
            return fase_3_parser.RULE_condicional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = fase_3_parser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_condicional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(fase_3_parser.IF)
            self.state = 153
            self.query(0)
            self.state = 154
            self.match(fase_3_parser.COLON)
            self.state = 155
            self.match(fase_3_parser.NEWLINE)
            self.state = 157 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 156
                    self.corpo()

                else:
                    raise NoViableAltException(self)
                self.state = 159 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 172
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 161
                    self.match(fase_3_parser.ELIF)
                    self.state = 162
                    self.query(0)
                    self.state = 163
                    self.match(fase_3_parser.COLON)
                    self.state = 164
                    self.match(fase_3_parser.NEWLINE)
                    self.state = 166 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 165
                            self.corpo()

                        else:
                            raise NoViableAltException(self)
                        self.state = 168 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
             
                self.state = 174
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 175
                self.match(fase_3_parser.ELSE)
                self.state = 176
                self.match(fase_3_parser.COLON)
                self.state = 177
                self.match(fase_3_parser.NEWLINE)
                self.state = 179 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 178
                        self.corpo()

                    else:
                        raise NoViableAltException(self)
                    self.state = 181 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(fase_3_parser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(fase_3_parser.FLOAT_TYPE, 0)

        def STR_TYPE(self):
            return self.getToken(fase_3_parser.STR_TYPE, 0)

        def BOOL_TYPE(self):
            return self.getToken(fase_3_parser.BOOL_TYPE, 0)

        def ID(self):
            return self.getToken(fase_3_parser.ID, 0)

        def getRuleIndex(self):
            return fase_3_parser.RULE_tipo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = fase_3_parser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0) or _la==100):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(fase_3_parser.DEF, 0)

        def ID(self):
            return self.getToken(fase_3_parser.ID, 0)

        def LPAREN(self):
            return self.getToken(fase_3_parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(fase_3_parser.RPAREN, 0)

        def COLON(self):
            return self.getToken(fase_3_parser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(fase_3_parser.NEWLINE, 0)

        def params(self):
            return self.getTypedRuleContext(fase_3_parser.ParamsContext,0)


        def ARROW(self):
            return self.getToken(fase_3_parser.ARROW, 0)

        def tipo(self):
            return self.getTypedRuleContext(fase_3_parser.TipoContext,0)


        def corpo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.CorpoContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.CorpoContext,i)


        def getRuleIndex(self):
            return fase_3_parser.RULE_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = fase_3_parser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(fase_3_parser.DEF)
            self.state = 188
            self.match(fase_3_parser.ID)
            self.state = 189
            self.match(fase_3_parser.LPAREN)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==100:
                self.state = 190
                self.params()


            self.state = 193
            self.match(fase_3_parser.RPAREN)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==79:
                self.state = 194
                self.match(fase_3_parser.ARROW)
                self.state = 195
                self.tipo()


            self.state = 198
            self.match(fase_3_parser.COLON)
            self.state = 199
            self.match(fase_3_parser.NEWLINE)
            self.state = 201 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 200
                    self.corpo()

                else:
                    raise NoViableAltException(self)
                self.state = 203 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.ParamContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(fase_3_parser.COMMA)
            else:
                return self.getToken(fase_3_parser.COMMA, i)

        def getRuleIndex(self):
            return fase_3_parser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = fase_3_parser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.param()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==82:
                self.state = 206
                self.match(fase_3_parser.COMMA)
                self.state = 207
                self.param()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(fase_3_parser.ID, 0)

        def COLON(self):
            return self.getToken(fase_3_parser.COLON, 0)

        def tipo(self):
            return self.getTypedRuleContext(fase_3_parser.TipoContext,0)


        def getRuleIndex(self):
            return fase_3_parser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = fase_3_parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(fase_3_parser.ID)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==81:
                self.state = 214
                self.match(fase_3_parser.COLON)
                self.state = 215
                self.tipo()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(fase_3_parser.ID, 0)

        def LPAREN(self):
            return self.getToken(fase_3_parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(fase_3_parser.RPAREN, 0)

        def args(self):
            return self.getTypedRuleContext(fase_3_parser.ArgsContext,0)


        def getRuleIndex(self):
            return fase_3_parser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = fase_3_parser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(fase_3_parser.ID)
            self.state = 219
            self.match(fase_3_parser.LPAREN)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 52)) & ~0x3f) == 0 and ((1 << (_la - 52)) & 421473730691073) != 0):
                self.state = 220
                self.args()


            self.state = 223
            self.match(fase_3_parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.ExprContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(fase_3_parser.COMMA)
            else:
                return self.getToken(fase_3_parser.COMMA, i)

        def getRuleIndex(self):
            return fase_3_parser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = fase_3_parser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.expr(0)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==82:
                self.state = 226
                self.match(fase_3_parser.COMMA)
                self.state = 227
                self.expr(0)
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_whileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(fase_3_parser.WHILE, 0)

        def query(self):
            return self.getTypedRuleContext(fase_3_parser.QueryContext,0)


        def COLON(self):
            return self.getToken(fase_3_parser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(fase_3_parser.NEWLINE, 0)

        def corpo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.CorpoContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.CorpoContext,i)


        def getRuleIndex(self):
            return fase_3_parser.RULE_loop_while

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_while" ):
                return visitor.visitLoop_while(self)
            else:
                return visitor.visitChildren(self)




    def loop_while(self):

        localctx = fase_3_parser.Loop_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_loop_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(fase_3_parser.WHILE)
            self.state = 234
            self.query(0)
            self.state = 235
            self.match(fase_3_parser.COLON)
            self.state = 236
            self.match(fase_3_parser.NEWLINE)
            self.state = 238 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 237
                    self.corpo()

                else:
                    raise NoViableAltException(self)
                self.state = 240 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(fase_3_parser.FOR, 0)

        def for_vars(self):
            return self.getTypedRuleContext(fase_3_parser.For_varsContext,0)


        def IN(self):
            return self.getToken(fase_3_parser.IN, 0)

        def expr(self):
            return self.getTypedRuleContext(fase_3_parser.ExprContext,0)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(fase_3_parser.COLON)
            else:
                return self.getToken(fase_3_parser.COLON, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(fase_3_parser.NEWLINE)
            else:
                return self.getToken(fase_3_parser.NEWLINE, i)

        def corpo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.CorpoContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.CorpoContext,i)


        def ELSE(self):
            return self.getToken(fase_3_parser.ELSE, 0)

        def getRuleIndex(self):
            return fase_3_parser.RULE_loop_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_for" ):
                return visitor.visitLoop_for(self)
            else:
                return visitor.visitChildren(self)




    def loop_for(self):

        localctx = fase_3_parser.Loop_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_loop_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(fase_3_parser.FOR)
            self.state = 243
            self.for_vars()
            self.state = 244
            self.match(fase_3_parser.IN)
            self.state = 245
            self.expr(0)
            self.state = 246
            self.match(fase_3_parser.COLON)
            self.state = 247
            self.match(fase_3_parser.NEWLINE)
            self.state = 249 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 248
                    self.corpo()

                else:
                    raise NoViableAltException(self)
                self.state = 251 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 253
                self.match(fase_3_parser.ELSE)
                self.state = 254
                self.match(fase_3_parser.COLON)
                self.state = 255
                self.match(fase_3_parser.NEWLINE)
                self.state = 257 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 256
                        self.corpo()

                    else:
                        raise NoViableAltException(self)
                    self.state = 259 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_varsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(fase_3_parser.ID)
            else:
                return self.getToken(fase_3_parser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(fase_3_parser.COMMA)
            else:
                return self.getToken(fase_3_parser.COMMA, i)

        def getRuleIndex(self):
            return fase_3_parser.RULE_for_vars

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_vars" ):
                return visitor.visitFor_vars(self)
            else:
                return visitor.visitChildren(self)




    def for_vars(self):

        localctx = fase_3_parser.For_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_for_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(fase_3_parser.ID)
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==82:
                self.state = 264
                self.match(fase_3_parser.COMMA)
                self.state = 265
                self.match(fase_3_parser.ID)
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(fase_3_parser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(fase_3_parser.RBRACKET, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.ExprContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(fase_3_parser.COMMA)
            else:
                return self.getToken(fase_3_parser.COMMA, i)

        def getRuleIndex(self):
            return fase_3_parser.RULE_lista

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista" ):
                return visitor.visitLista(self)
            else:
                return visitor.visitChildren(self)




    def lista(self):

        localctx = fase_3_parser.ListaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(fase_3_parser.LBRACKET)
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 52)) & ~0x3f) == 0 and ((1 << (_la - 52)) & 421473730691073) != 0):
                self.state = 272
                self.expr(0)
                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==82:
                    self.state = 273
                    self.match(fase_3_parser.COMMA)
                    self.state = 274
                    self.expr(0)
                    self.state = 279
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 282
            self.match(fase_3_parser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TuplaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(fase_3_parser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.ExprContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(fase_3_parser.COMMA)
            else:
                return self.getToken(fase_3_parser.COMMA, i)

        def RPAREN(self):
            return self.getToken(fase_3_parser.RPAREN, 0)

        def getRuleIndex(self):
            return fase_3_parser.RULE_tupla

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTupla" ):
                return visitor.visitTupla(self)
            else:
                return visitor.visitChildren(self)




    def tupla(self):

        localctx = fase_3_parser.TuplaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_tupla)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(fase_3_parser.LPAREN)
            self.state = 285
            self.expr(0)
            self.state = 286
            self.match(fase_3_parser.COMMA)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 52)) & ~0x3f) == 0 and ((1 << (_la - 52)) & 421473730691073) != 0):
                self.state = 287
                self.expr(0)
                self.state = 292
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==82:
                    self.state = 288
                    self.match(fase_3_parser.COMMA)
                    self.state = 289
                    self.expr(0)
                    self.state = 294
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 297
            self.match(fase_3_parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Set_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(fase_3_parser.LBRACE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.ExprContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.ExprContext,i)


        def RBRACE(self):
            return self.getToken(fase_3_parser.RBRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(fase_3_parser.COMMA)
            else:
                return self.getToken(fase_3_parser.COMMA, i)

        def getRuleIndex(self):
            return fase_3_parser.RULE_set_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSet_lit" ):
                return visitor.visitSet_lit(self)
            else:
                return visitor.visitChildren(self)




    def set_lit(self):

        localctx = fase_3_parser.Set_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_set_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(fase_3_parser.LBRACE)
            self.state = 300
            self.expr(0)
            self.state = 303 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 301
                self.match(fase_3_parser.COMMA)
                self.state = 302
                self.expr(0)
                self.state = 305 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==82):
                    break

            self.state = 307
            self.match(fase_3_parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DicionarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(fase_3_parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(fase_3_parser.RBRACE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(fase_3_parser.ExprContext)
            else:
                return self.getTypedRuleContext(fase_3_parser.ExprContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(fase_3_parser.COLON)
            else:
                return self.getToken(fase_3_parser.COLON, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(fase_3_parser.COMMA)
            else:
                return self.getToken(fase_3_parser.COMMA, i)

        def getRuleIndex(self):
            return fase_3_parser.RULE_dicionario

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDicionario" ):
                return visitor.visitDicionario(self)
            else:
                return visitor.visitChildren(self)




    def dicionario(self):

        localctx = fase_3_parser.DicionarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_dicionario)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(fase_3_parser.LBRACE)
            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 52)) & ~0x3f) == 0 and ((1 << (_la - 52)) & 421473730691073) != 0):
                self.state = 310
                self.expr(0)
                self.state = 311
                self.match(fase_3_parser.COLON)
                self.state = 312
                self.expr(0)
                self.state = 320
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==82:
                    self.state = 313
                    self.match(fase_3_parser.COMMA)
                    self.state = 314
                    self.expr(0)
                    self.state = 315
                    self.match(fase_3_parser.COLON)
                    self.state = 316
                    self.expr(0)
                    self.state = 322
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 325
            self.match(fase_3_parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        self._predicates[6] = self.query_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

    def query_sempred(self, localctx:QueryContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         




