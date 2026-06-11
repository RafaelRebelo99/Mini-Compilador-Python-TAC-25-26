if "." in __name__:
    from .fase_3_parser import fase_3_parser
    from .fase_3_parserVisitor import fase_3_parserVisitor
else:
    from fase_3_parser import fase_3_parser
    from fase_3_parserVisitor import fase_3_parserVisitor

class Compiler(fase_3_parserVisitor):

    def __init__(self):
        super(Compiler, self).__init__()
        self.vars = {}
        return None

    def visitCode(self, ctx:fase_3_parser.CodeContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitStat(self, ctx:fase_3_parser.StatContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitExpr(self, ctx:fase_3_parser.ExprContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitIds(self, ctx:fase_3_parser.IdsContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitNumeros(self, ctx:fase_3_parser.NumerosContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitQuery(self, ctx:fase_3_parser.QueryContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitValoresBooleanos(self, ctx:fase_3_parser.ValoresBooleanosContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitRelacoesEntreExpressoes(self, ctx:fase_3_parser.RelacoesEntreExpressoesContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitCorpo(self, ctx:fase_3_parser.CorpoContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitCondicional(self, ctx:fase_3_parser.CondicionalContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitTipo(self, ctx:fase_3_parser.TipoContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitFunc(self, ctx:fase_3_parser.FuncContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitParams(self, ctx:fase_3_parser.ParamsContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitParam(self, ctx:fase_3_parser.ParamContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitFunc_call(self, ctx:fase_3_parser.Func_callContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitArgs(self, ctx:fase_3_parser.ArgsContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitLoop_while(self, ctx:fase_3_parser.Loop_whileContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitLoop_for(self, ctx:fase_3_parser.Loop_forContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitFor_vars(self, ctx:fase_3_parser.For_varsContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitLista(self, ctx:fase_3_parser.ListaContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitTupla(self, ctx:fase_3_parser.TuplaContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitSet_lit(self, ctx:fase_3_parser.Set_litContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

    def visitDicionario(self, ctx:fase_3_parser.DicionarioContext):
        print(('Here', ctx.getText(), type(ctx)))
        return self.visitChildren(ctx)

del (fase_3_parser, fase_3_parserVisitor)
