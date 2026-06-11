# Generated from fase_3_parser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .fase_3_parser import fase_3_parser
else:
    from fase_3_parser import fase_3_parser

# This class defines a complete generic visitor for a parse tree produced by fase_3_parser.

class fase_3_parserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by fase_3_parser#code.
    def visitCode(self, ctx:fase_3_parser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#stat.
    def visitStat(self, ctx:fase_3_parser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#expr.
    def visitExpr(self, ctx:fase_3_parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#ids.
    def visitIds(self, ctx:fase_3_parser.IdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#numeros.
    def visitNumeros(self, ctx:fase_3_parser.NumerosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#query.
    def visitQuery(self, ctx:fase_3_parser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#valoresBooleanos.
    def visitValoresBooleanos(self, ctx:fase_3_parser.ValoresBooleanosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#relacoesEntreExpressoes.
    def visitRelacoesEntreExpressoes(self, ctx:fase_3_parser.RelacoesEntreExpressoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#corpo.
    def visitCorpo(self, ctx:fase_3_parser.CorpoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#condicional.
    def visitCondicional(self, ctx:fase_3_parser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#tipo.
    def visitTipo(self, ctx:fase_3_parser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#func.
    def visitFunc(self, ctx:fase_3_parser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#params.
    def visitParams(self, ctx:fase_3_parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#param.
    def visitParam(self, ctx:fase_3_parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#func_call.
    def visitFunc_call(self, ctx:fase_3_parser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#args.
    def visitArgs(self, ctx:fase_3_parser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#loop_while.
    def visitLoop_while(self, ctx:fase_3_parser.Loop_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#loop_for.
    def visitLoop_for(self, ctx:fase_3_parser.Loop_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#for_vars.
    def visitFor_vars(self, ctx:fase_3_parser.For_varsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#lista.
    def visitLista(self, ctx:fase_3_parser.ListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#tupla.
    def visitTupla(self, ctx:fase_3_parser.TuplaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#set_lit.
    def visitSet_lit(self, ctx:fase_3_parser.Set_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by fase_3_parser#dicionario.
    def visitDicionario(self, ctx:fase_3_parser.DicionarioContext):
        return self.visitChildren(ctx)



del fase_3_parser