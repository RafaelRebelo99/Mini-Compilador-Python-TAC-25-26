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
        4,1,102,325,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,
        55,8,0,10,0,12,0,58,9,0,1,0,1,0,1,1,1,1,3,1,64,8,1,1,1,3,1,67,8,
        1,1,1,1,1,3,1,71,8,1,1,1,1,1,3,1,75,8,1,1,1,1,1,3,1,79,8,1,1,1,3,
        1,82,8,1,3,1,84,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,101,8,2,1,2,1,2,1,2,5,2,106,8,2,10,2,12,2,109,
        9,2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,3,5,127,8,5,1,5,1,5,1,5,5,5,132,8,5,10,5,12,5,135,9,5,1,6,1,
        6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,3,8,148,8,8,1,9,1,9,1,9,1,
        9,1,9,4,9,155,8,9,11,9,12,9,156,1,9,1,9,1,9,1,9,1,9,4,9,164,8,9,
        11,9,12,9,165,5,9,168,8,9,10,9,12,9,171,9,9,1,9,1,9,1,9,1,9,4,9,
        177,8,9,11,9,12,9,178,3,9,181,8,9,1,10,1,10,1,11,1,11,1,11,1,11,
        3,11,189,8,11,1,11,1,11,1,11,3,11,194,8,11,1,11,1,11,1,11,4,11,199,
        8,11,11,11,12,11,200,1,12,1,12,1,12,5,12,206,8,12,10,12,12,12,209,
        9,12,1,13,1,13,1,13,3,13,214,8,13,1,14,1,14,1,14,3,14,219,8,14,1,
        14,1,14,1,15,1,15,1,15,5,15,226,8,15,10,15,12,15,229,9,15,1,16,1,
        16,1,16,1,16,1,16,4,16,236,8,16,11,16,12,16,237,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,4,17,247,8,17,11,17,12,17,248,1,17,1,17,1,17,1,
        17,4,17,255,8,17,11,17,12,17,256,3,17,259,8,17,1,18,1,18,1,18,5,
        18,264,8,18,10,18,12,18,267,9,18,1,19,1,19,1,19,1,19,5,19,273,8,
        19,10,19,12,19,276,9,19,3,19,278,8,19,1,19,1,19,1,20,1,20,1,20,1,
        20,1,20,1,20,5,20,288,8,20,10,20,12,20,291,9,20,3,20,293,8,20,1,
        20,1,20,1,21,1,21,1,21,1,21,4,21,301,8,21,11,21,12,21,302,1,21,1,
        21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,5,22,316,8,22,10,
        22,12,22,319,9,22,3,22,321,8,22,1,22,1,22,1,22,0,2,4,10,23,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,0,5,1,
        0,93,98,2,0,28,29,61,63,1,0,47,48,1,0,53,58,2,0,14,17,100,100,360,
        0,56,1,0,0,0,2,83,1,0,0,0,4,100,1,0,0,0,6,110,1,0,0,0,8,112,1,0,
        0,0,10,126,1,0,0,0,12,136,1,0,0,0,14,138,1,0,0,0,16,147,1,0,0,0,
        18,149,1,0,0,0,20,182,1,0,0,0,22,184,1,0,0,0,24,202,1,0,0,0,26,210,
        1,0,0,0,28,215,1,0,0,0,30,222,1,0,0,0,32,230,1,0,0,0,34,239,1,0,
        0,0,36,260,1,0,0,0,38,268,1,0,0,0,40,281,1,0,0,0,42,296,1,0,0,0,
        44,306,1,0,0,0,46,55,3,2,1,0,47,55,3,18,9,0,48,55,3,22,11,0,49,50,
        3,28,14,0,50,51,5,101,0,0,51,55,1,0,0,0,52,55,3,32,16,0,53,55,3,
        34,17,0,54,46,1,0,0,0,54,47,1,0,0,0,54,48,1,0,0,0,54,49,1,0,0,0,
        54,52,1,0,0,0,54,53,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,
        0,0,0,57,59,1,0,0,0,58,56,1,0,0,0,59,60,5,0,0,1,60,1,1,0,0,0,61,
        64,3,4,2,0,62,64,3,10,5,0,63,61,1,0,0,0,63,62,1,0,0,0,64,66,1,0,
        0,0,65,67,5,101,0,0,66,65,1,0,0,0,66,67,1,0,0,0,67,84,1,0,0,0,68,
        70,5,39,0,0,69,71,5,101,0,0,70,69,1,0,0,0,70,71,1,0,0,0,71,84,1,
        0,0,0,72,74,5,40,0,0,73,75,5,101,0,0,74,73,1,0,0,0,74,75,1,0,0,0,
        75,84,1,0,0,0,76,78,5,36,0,0,77,79,3,4,2,0,78,77,1,0,0,0,78,79,1,
        0,0,0,79,81,1,0,0,0,80,82,5,101,0,0,81,80,1,0,0,0,81,82,1,0,0,0,
        82,84,1,0,0,0,83,63,1,0,0,0,83,68,1,0,0,0,83,72,1,0,0,0,83,76,1,
        0,0,0,84,3,1,0,0,0,85,86,6,2,-1,0,86,87,5,52,0,0,87,101,3,4,2,10,
        88,89,5,86,0,0,89,90,3,4,2,0,90,91,5,87,0,0,91,101,1,0,0,0,92,101,
        3,28,14,0,93,101,3,6,3,0,94,101,3,8,4,0,95,101,5,92,0,0,96,101,3,
        38,19,0,97,101,3,40,20,0,98,101,3,42,21,0,99,101,3,44,22,0,100,85,
        1,0,0,0,100,88,1,0,0,0,100,92,1,0,0,0,100,93,1,0,0,0,100,94,1,0,
        0,0,100,95,1,0,0,0,100,96,1,0,0,0,100,97,1,0,0,0,100,98,1,0,0,0,
        100,99,1,0,0,0,101,107,1,0,0,0,102,103,10,11,0,0,103,104,5,52,0,
        0,104,106,3,4,2,12,105,102,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,
        0,107,108,1,0,0,0,108,5,1,0,0,0,109,107,1,0,0,0,110,111,5,100,0,
        0,111,7,1,0,0,0,112,113,7,0,0,0,113,9,1,0,0,0,114,115,6,5,-1,0,115,
        116,5,30,0,0,116,127,3,10,5,6,117,118,5,64,0,0,118,127,3,10,5,5,
        119,120,5,86,0,0,120,121,3,10,5,0,121,122,5,87,0,0,122,127,1,0,0,
        0,123,127,3,12,6,0,124,127,3,14,7,0,125,127,3,28,14,0,126,114,1,
        0,0,0,126,117,1,0,0,0,126,119,1,0,0,0,126,123,1,0,0,0,126,124,1,
        0,0,0,126,125,1,0,0,0,127,133,1,0,0,0,128,129,10,7,0,0,129,130,7,
        1,0,0,130,132,3,10,5,8,131,128,1,0,0,0,132,135,1,0,0,0,133,131,1,
        0,0,0,133,134,1,0,0,0,134,11,1,0,0,0,135,133,1,0,0,0,136,137,7,2,
        0,0,137,13,1,0,0,0,138,139,3,4,2,0,139,140,7,3,0,0,140,141,3,4,2,
        0,141,15,1,0,0,0,142,148,3,2,1,0,143,148,3,22,11,0,144,148,3,18,
        9,0,145,148,3,32,16,0,146,148,3,34,17,0,147,142,1,0,0,0,147,143,
        1,0,0,0,147,144,1,0,0,0,147,145,1,0,0,0,147,146,1,0,0,0,148,17,1,
        0,0,0,149,150,5,1,0,0,150,151,3,10,5,0,151,152,5,81,0,0,152,154,
        5,101,0,0,153,155,3,16,8,0,154,153,1,0,0,0,155,156,1,0,0,0,156,154,
        1,0,0,0,156,157,1,0,0,0,157,169,1,0,0,0,158,159,5,2,0,0,159,160,
        3,10,5,0,160,161,5,81,0,0,161,163,5,101,0,0,162,164,3,16,8,0,163,
        162,1,0,0,0,164,165,1,0,0,0,165,163,1,0,0,0,165,166,1,0,0,0,166,
        168,1,0,0,0,167,158,1,0,0,0,168,171,1,0,0,0,169,167,1,0,0,0,169,
        170,1,0,0,0,170,180,1,0,0,0,171,169,1,0,0,0,172,173,5,3,0,0,173,
        174,5,81,0,0,174,176,5,101,0,0,175,177,3,16,8,0,176,175,1,0,0,0,
        177,178,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,181,1,0,0,0,
        180,172,1,0,0,0,180,181,1,0,0,0,181,19,1,0,0,0,182,183,7,4,0,0,183,
        21,1,0,0,0,184,185,5,6,0,0,185,186,5,100,0,0,186,188,5,86,0,0,187,
        189,3,24,12,0,188,187,1,0,0,0,188,189,1,0,0,0,189,190,1,0,0,0,190,
        193,5,87,0,0,191,192,5,79,0,0,192,194,3,20,10,0,193,191,1,0,0,0,
        193,194,1,0,0,0,194,195,1,0,0,0,195,196,5,81,0,0,196,198,5,101,0,
        0,197,199,3,16,8,0,198,197,1,0,0,0,199,200,1,0,0,0,200,198,1,0,0,
        0,200,201,1,0,0,0,201,23,1,0,0,0,202,207,3,26,13,0,203,204,5,82,
        0,0,204,206,3,26,13,0,205,203,1,0,0,0,206,209,1,0,0,0,207,205,1,
        0,0,0,207,208,1,0,0,0,208,25,1,0,0,0,209,207,1,0,0,0,210,213,5,100,
        0,0,211,212,5,81,0,0,212,214,3,20,10,0,213,211,1,0,0,0,213,214,1,
        0,0,0,214,27,1,0,0,0,215,216,5,100,0,0,216,218,5,86,0,0,217,219,
        3,30,15,0,218,217,1,0,0,0,218,219,1,0,0,0,219,220,1,0,0,0,220,221,
        5,87,0,0,221,29,1,0,0,0,222,227,3,4,2,0,223,224,5,82,0,0,224,226,
        3,4,2,0,225,223,1,0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,228,
        1,0,0,0,228,31,1,0,0,0,229,227,1,0,0,0,230,231,5,5,0,0,231,232,3,
        10,5,0,232,233,5,81,0,0,233,235,5,101,0,0,234,236,3,16,8,0,235,234,
        1,0,0,0,236,237,1,0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,33,1,
        0,0,0,239,240,5,4,0,0,240,241,3,36,18,0,241,242,5,31,0,0,242,243,
        3,4,2,0,243,244,5,81,0,0,244,246,5,101,0,0,245,247,3,16,8,0,246,
        245,1,0,0,0,247,248,1,0,0,0,248,246,1,0,0,0,248,249,1,0,0,0,249,
        258,1,0,0,0,250,251,5,3,0,0,251,252,5,81,0,0,252,254,5,101,0,0,253,
        255,3,16,8,0,254,253,1,0,0,0,255,256,1,0,0,0,256,254,1,0,0,0,256,
        257,1,0,0,0,257,259,1,0,0,0,258,250,1,0,0,0,258,259,1,0,0,0,259,
        35,1,0,0,0,260,265,5,100,0,0,261,262,5,82,0,0,262,264,5,100,0,0,
        263,261,1,0,0,0,264,267,1,0,0,0,265,263,1,0,0,0,265,266,1,0,0,0,
        266,37,1,0,0,0,267,265,1,0,0,0,268,277,5,88,0,0,269,274,3,4,2,0,
        270,271,5,82,0,0,271,273,3,4,2,0,272,270,1,0,0,0,273,276,1,0,0,0,
        274,272,1,0,0,0,274,275,1,0,0,0,275,278,1,0,0,0,276,274,1,0,0,0,
        277,269,1,0,0,0,277,278,1,0,0,0,278,279,1,0,0,0,279,280,5,89,0,0,
        280,39,1,0,0,0,281,282,5,86,0,0,282,283,3,4,2,0,283,292,5,82,0,0,
        284,289,3,4,2,0,285,286,5,82,0,0,286,288,3,4,2,0,287,285,1,0,0,0,
        288,291,1,0,0,0,289,287,1,0,0,0,289,290,1,0,0,0,290,293,1,0,0,0,
        291,289,1,0,0,0,292,284,1,0,0,0,292,293,1,0,0,0,293,294,1,0,0,0,
        294,295,5,87,0,0,295,41,1,0,0,0,296,297,5,90,0,0,297,300,3,4,2,0,
        298,299,5,82,0,0,299,301,3,4,2,0,300,298,1,0,0,0,301,302,1,0,0,0,
        302,300,1,0,0,0,302,303,1,0,0,0,303,304,1,0,0,0,304,305,5,91,0,0,
        305,43,1,0,0,0,306,320,5,90,0,0,307,308,3,4,2,0,308,309,5,81,0,0,
        309,317,3,4,2,0,310,311,5,82,0,0,311,312,3,4,2,0,312,313,5,81,0,
        0,313,314,3,4,2,0,314,316,1,0,0,0,315,310,1,0,0,0,316,319,1,0,0,
        0,317,315,1,0,0,0,317,318,1,0,0,0,318,321,1,0,0,0,319,317,1,0,0,
        0,320,307,1,0,0,0,320,321,1,0,0,0,321,322,1,0,0,0,322,323,5,91,0,
        0,323,45,1,0,0,0,38,54,56,63,66,70,74,78,81,83,100,107,126,133,147,
        156,165,169,178,180,188,193,200,207,213,218,227,237,248,256,258,
        265,274,277,289,292,302,317,320
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
    RULE_expr = 2
    RULE_ids = 3
    RULE_numeros = 4
    RULE_query = 5
    RULE_valoresBooleanos = 6
    RULE_relacoesEntreExpressoes = 7
    RULE_corpo = 8
    RULE_condicional = 9
    RULE_tipo = 10
    RULE_func = 11
    RULE_params = 12
    RULE_param = 13
    RULE_func_call = 14
    RULE_args = 15
    RULE_loop_while = 16
    RULE_loop_for = 17
    RULE_for_vars = 18
    RULE_lista = 19
    RULE_tupla = 20
    RULE_set_lit = 21
    RULE_dicionario = 22

    ruleNames =  [ "code", "stat", "expr", "ids", "numeros", "query", "valoresBooleanos", 
                   "relacoesEntreExpressoes", "corpo", "condicional", "tipo", 
                   "func", "params", "param", "func_call", "args", "loop_while", 
                   "loop_for", "for_vars", "lista", "tupla", "set_lit", 
                   "dicionario" ]

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


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(fase_3_parser.NEWLINE)
            else:
                return self.getToken(fase_3_parser.NEWLINE, i)

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
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4927531153096818) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 102898860033) != 0):
                self.state = 54
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 46
                    self.stat()
                    pass

                elif la_ == 2:
                    self.state = 47
                    self.condicional()
                    pass

                elif la_ == 3:
                    self.state = 48
                    self.func()
                    pass

                elif la_ == 4:
                    self.state = 49
                    self.func_call()
                    self.state = 50
                    self.match(fase_3_parser.NEWLINE)
                    pass

                elif la_ == 5:
                    self.state = 52
                    self.loop_while()
                    pass

                elif la_ == 6:
                    self.state = 53
                    self.loop_for()
                    pass


                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
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

        def expr(self):
            return self.getTypedRuleContext(fase_3_parser.ExprContext,0)


        def query(self):
            return self.getTypedRuleContext(fase_3_parser.QueryContext,0)


        def NEWLINE(self):
            return self.getToken(fase_3_parser.NEWLINE, 0)

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
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30, 47, 48, 52, 64, 86, 88, 90, 92, 93, 94, 95, 96, 97, 98, 100]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 61
                    self.expr(0)
                    pass

                elif la_ == 2:
                    self.state = 62
                    self.query(0)
                    pass


                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==101:
                    self.state = 65
                    self.match(fase_3_parser.NEWLINE)


                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.match(fase_3_parser.BREAK)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==101:
                    self.state = 69
                    self.match(fase_3_parser.NEWLINE)


                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.match(fase_3_parser.CONTINUE)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==101:
                    self.state = 73
                    self.match(fase_3_parser.NEWLINE)


                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.match(fase_3_parser.RETURN)
                self.state = 78
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 77
                    self.expr(0)


                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==101:
                    self.state = 80
                    self.match(fase_3_parser.NEWLINE)


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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 86
                self.match(fase_3_parser.OP)
                self.state = 87
                self.expr(10)
                pass

            elif la_ == 2:
                self.state = 88
                self.match(fase_3_parser.LPAREN)
                self.state = 89
                self.expr(0)
                self.state = 90
                self.match(fase_3_parser.RPAREN)
                pass

            elif la_ == 3:
                self.state = 92
                self.func_call()
                pass

            elif la_ == 4:
                self.state = 93
                self.ids()
                pass

            elif la_ == 5:
                self.state = 94
                self.numeros()
                pass

            elif la_ == 6:
                self.state = 95
                self.match(fase_3_parser.STRING)
                pass

            elif la_ == 7:
                self.state = 96
                self.lista()
                pass

            elif la_ == 8:
                self.state = 97
                self.tupla()
                pass

            elif la_ == 9:
                self.state = 98
                self.set_lit()
                pass

            elif la_ == 10:
                self.state = 99
                self.dicionario()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = fase_3_parser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 102
                    if not self.precpred(self._ctx, 11):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                    self.state = 103
                    self.match(fase_3_parser.OP)
                    self.state = 104
                    self.expr(12) 
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        self.enterRule(localctx, 6, self.RULE_ids)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
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
        self.enterRule(localctx, 8, self.RULE_numeros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_query, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 115
                self.match(fase_3_parser.NOT)
                self.state = 116
                self.query(6)
                pass

            elif la_ == 2:
                self.state = 117
                self.match(fase_3_parser.TILDE)
                self.state = 118
                self.query(5)
                pass

            elif la_ == 3:
                self.state = 119
                self.match(fase_3_parser.LPAREN)
                self.state = 120
                self.query(0)
                self.state = 121
                self.match(fase_3_parser.RPAREN)
                pass

            elif la_ == 4:
                self.state = 123
                self.valoresBooleanos()
                pass

            elif la_ == 5:
                self.state = 124
                self.relacoesEntreExpressoes()
                pass

            elif la_ == 6:
                self.state = 125
                self.func_call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 133
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = fase_3_parser.QueryContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_query)
                    self.state = 128
                    if not self.precpred(self._ctx, 7):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                    self.state = 129
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & -2305843008408387584) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 130
                    self.query(8) 
                self.state = 135
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self.enterRule(localctx, 12, self.RULE_valoresBooleanos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
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
        self.enterRule(localctx, 14, self.RULE_relacoesEntreExpressoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.expr(0)
            self.state = 139
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 567453553048682496) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 140
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
        self.enterRule(localctx, 16, self.RULE_corpo)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30, 36, 39, 40, 47, 48, 52, 64, 86, 88, 90, 92, 93, 94, 95, 96, 97, 98, 100]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.stat()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.func()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 144
                self.condicional()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 145
                self.loop_while()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 146
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
        self.enterRule(localctx, 18, self.RULE_condicional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(fase_3_parser.IF)
            self.state = 150
            self.query(0)
            self.state = 151
            self.match(fase_3_parser.COLON)
            self.state = 152
            self.match(fase_3_parser.NEWLINE)
            self.state = 154 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 153
                    self.corpo()

                else:
                    raise NoViableAltException(self)
                self.state = 156 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 169
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 158
                    self.match(fase_3_parser.ELIF)
                    self.state = 159
                    self.query(0)
                    self.state = 160
                    self.match(fase_3_parser.COLON)
                    self.state = 161
                    self.match(fase_3_parser.NEWLINE)
                    self.state = 163 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 162
                            self.corpo()

                        else:
                            raise NoViableAltException(self)
                        self.state = 165 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
             
                self.state = 171
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 172
                self.match(fase_3_parser.ELSE)
                self.state = 173
                self.match(fase_3_parser.COLON)
                self.state = 174
                self.match(fase_3_parser.NEWLINE)
                self.state = 176 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 175
                        self.corpo()

                    else:
                        raise NoViableAltException(self)
                    self.state = 178 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)



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
        self.enterRule(localctx, 20, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
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
        self.enterRule(localctx, 22, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(fase_3_parser.DEF)
            self.state = 185
            self.match(fase_3_parser.ID)
            self.state = 186
            self.match(fase_3_parser.LPAREN)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==100:
                self.state = 187
                self.params()


            self.state = 190
            self.match(fase_3_parser.RPAREN)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==79:
                self.state = 191
                self.match(fase_3_parser.ARROW)
                self.state = 192
                self.tipo()


            self.state = 195
            self.match(fase_3_parser.COLON)
            self.state = 196
            self.match(fase_3_parser.NEWLINE)
            self.state = 198 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 197
                    self.corpo()

                else:
                    raise NoViableAltException(self)
                self.state = 200 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 24, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.param()
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==82:
                self.state = 203
                self.match(fase_3_parser.COMMA)
                self.state = 204
                self.param()
                self.state = 209
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
        self.enterRule(localctx, 26, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(fase_3_parser.ID)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==81:
                self.state = 211
                self.match(fase_3_parser.COLON)
                self.state = 212
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
        self.enterRule(localctx, 28, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(fase_3_parser.ID)
            self.state = 216
            self.match(fase_3_parser.LPAREN)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 52)) & ~0x3f) == 0 and ((1 << (_la - 52)) & 421473730691073) != 0):
                self.state = 217
                self.args()


            self.state = 220
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
        self.enterRule(localctx, 30, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.expr(0)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==82:
                self.state = 223
                self.match(fase_3_parser.COMMA)
                self.state = 224
                self.expr(0)
                self.state = 229
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
        self.enterRule(localctx, 32, self.RULE_loop_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(fase_3_parser.WHILE)
            self.state = 231
            self.query(0)
            self.state = 232
            self.match(fase_3_parser.COLON)
            self.state = 233
            self.match(fase_3_parser.NEWLINE)
            self.state = 235 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 234
                    self.corpo()

                else:
                    raise NoViableAltException(self)
                self.state = 237 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        self.enterRule(localctx, 34, self.RULE_loop_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(fase_3_parser.FOR)
            self.state = 240
            self.for_vars()
            self.state = 241
            self.match(fase_3_parser.IN)
            self.state = 242
            self.expr(0)
            self.state = 243
            self.match(fase_3_parser.COLON)
            self.state = 244
            self.match(fase_3_parser.NEWLINE)
            self.state = 246 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 245
                    self.corpo()

                else:
                    raise NoViableAltException(self)
                self.state = 248 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 250
                self.match(fase_3_parser.ELSE)
                self.state = 251
                self.match(fase_3_parser.COLON)
                self.state = 252
                self.match(fase_3_parser.NEWLINE)
                self.state = 254 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 253
                        self.corpo()

                    else:
                        raise NoViableAltException(self)
                    self.state = 256 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,28,self._ctx)



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
        self.enterRule(localctx, 36, self.RULE_for_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(fase_3_parser.ID)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==82:
                self.state = 261
                self.match(fase_3_parser.COMMA)
                self.state = 262
                self.match(fase_3_parser.ID)
                self.state = 267
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
        self.enterRule(localctx, 38, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(fase_3_parser.LBRACKET)
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 52)) & ~0x3f) == 0 and ((1 << (_la - 52)) & 421473730691073) != 0):
                self.state = 269
                self.expr(0)
                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==82:
                    self.state = 270
                    self.match(fase_3_parser.COMMA)
                    self.state = 271
                    self.expr(0)
                    self.state = 276
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 279
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
        self.enterRule(localctx, 40, self.RULE_tupla)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(fase_3_parser.LPAREN)
            self.state = 282
            self.expr(0)
            self.state = 283
            self.match(fase_3_parser.COMMA)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 52)) & ~0x3f) == 0 and ((1 << (_la - 52)) & 421473730691073) != 0):
                self.state = 284
                self.expr(0)
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==82:
                    self.state = 285
                    self.match(fase_3_parser.COMMA)
                    self.state = 286
                    self.expr(0)
                    self.state = 291
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 294
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
        self.enterRule(localctx, 42, self.RULE_set_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(fase_3_parser.LBRACE)
            self.state = 297
            self.expr(0)
            self.state = 300 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 298
                self.match(fase_3_parser.COMMA)
                self.state = 299
                self.expr(0)
                self.state = 302 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==82):
                    break

            self.state = 304
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
        self.enterRule(localctx, 44, self.RULE_dicionario)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(fase_3_parser.LBRACE)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 52)) & ~0x3f) == 0 and ((1 << (_la - 52)) & 421473730691073) != 0):
                self.state = 307
                self.expr(0)
                self.state = 308
                self.match(fase_3_parser.COLON)
                self.state = 309
                self.expr(0)
                self.state = 317
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==82:
                    self.state = 310
                    self.match(fase_3_parser.COMMA)
                    self.state = 311
                    self.expr(0)
                    self.state = 312
                    self.match(fase_3_parser.COLON)
                    self.state = 313
                    self.expr(0)
                    self.state = 319
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 322
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
        self._predicates[2] = self.expr_sempred
        self._predicates[5] = self.query_sempred
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
         




