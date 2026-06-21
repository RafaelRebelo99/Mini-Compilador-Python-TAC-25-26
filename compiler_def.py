if "." in __name__:
    from .fase_3_parser import fase_3_parser
    from .fase_3_parserVisitor import fase_3_parserVisitor
else:
    from fase_3_parser import fase_3_parser
    from fase_3_parserVisitor import fase_3_parserVisitor

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class Compiler(fase_3_parserVisitor):

    def __init__(self):
        super(Compiler, self).__init__()
        self.vars = {}
        self.funcs = {}
        return None

    def visitCode(self, ctx:fase_3_parser.CodeContext):
        return self.visitChildren(ctx)

    def visitStat(self, ctx:fase_3_parser.StatContext):
        if ctx.getChild(0).getText() == 'return':
            value = self.visit(ctx.expr()) if ctx.expr() else None
            raise ReturnException(value)
        return self.visitChildren(ctx)

# 10.3 Atribuição de variáveis
    def visitAssign(self, ctx:fase_3_parser.AssignContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.vars[name] = value
        return value

# 10.2 Avaliar expressões 
    def visitExpr(self, ctx:fase_3_parser.ExprContext):
        count = ctx.getChildCount()

        if count == 1:
            if ctx.STRING():
                text = ctx.STRING().getText()
                return text[1:-1]
            return self.visit(ctx.getChild(0))

        elif count == 2:
            op = ctx.getChild(0).getText()
            val = self.visit(ctx.getChild(1))
            return -val if op == '-' else val

        elif count == 3:
            if ctx.getChild(0).getText() == '(':
                return self.visit(ctx.getChild(1))
            left  = self.visit(ctx.getChild(0))
            op    = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))
            ops = {'+': lambda a,b: a+b, '-': lambda a,b: a-b,
                   '*': lambda a,b: a*b, '/': lambda a,b: a/b,
                   '//': lambda a,b: a//b, '%': lambda a,b: a%b,
                   '**': lambda a,b: a**b}
            return ops[op](left, right)

        return self.visitChildren(ctx)

    def visitIds(self, ctx:fase_3_parser.IdsContext):
        return self.vars.get(ctx.getText())

    def visitNumeros(self, ctx:fase_3_parser.NumerosContext):
        text = ctx.getText()
        if ctx.INT_LIT():     return int(text)
        if ctx.FLOAT_LIT():   return float(text)
        if ctx.HEX_LIT():     return int(text, 16)
        if ctx.OCT_LIT():     return int(text, 8)
        if ctx.BIN_LIT():     return int(text, 2)
        if ctx.COMPLEX_LIT(): return complex(text)
        return int(text)

    def visitQuery(self, ctx:fase_3_parser.QueryContext):
        count = ctx.getChildCount()
        if count == 1:
            return self.visit(ctx.getChild(0))
        elif count == 2:
            op  = ctx.getChild(0).getText()
            val = self.visit(ctx.getChild(1))
            if op == 'not': return not val
            if op == '~':   return ~val
            return val
        elif count == 3:
            if ctx.getChild(0).getText() == '(':
                return self.visit(ctx.getChild(1))
            left  = self.visit(ctx.getChild(0))
            op    = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))
            if op == 'and': return left and right
            if op == 'or':  return left or right
            if op == '&':   return left & right
            if op == '|':   return left | right
            if op == '^':   return left ^ right
        return self.visitChildren(ctx)

    def visitValoresBooleanos(self, ctx:fase_3_parser.ValoresBooleanosContext):
        return ctx.getText() == 'True'

    def visitRelacoesEntreExpressoes(self, ctx:fase_3_parser.RelacoesEntreExpressoesContext):
        left  = self.visit(ctx.getChild(0))
        op    = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))
        ops = {'==': lambda a,b: a==b, '!=': lambda a,b: a!=b,
               '<':  lambda a,b: a<b,  '>':  lambda a,b: a>b,
               '<=': lambda a,b: a<=b, '>=': lambda a,b: a>=b}
        return ops[op](left, right)

    def visitCorpo(self, ctx:fase_3_parser.CorpoContext):
        return self.visitChildren(ctx)

# 10.5 Condicional if-elif-else
    def visitCondicional(self, ctx:fase_3_parser.CondicionalContext):
        i = 0
        n = ctx.getChildCount()
        while i < n:
            text = ctx.getChild(i).getText()
            if text in ('if', 'elif'):
                i += 1
                query = ctx.getChild(i); i += 1
                i += 2  
                corpos = []
                while i < n and type(ctx.getChild(i)).__name__ == 'CorpoContext':
                    corpos.append(ctx.getChild(i)); i += 1
                if self.visit(query):
                    for c in corpos: self.visit(c)
                    return None
            elif text == 'else':
                i += 3  
                while i < n and type(ctx.getChild(i)).__name__ == 'CorpoContext':
                    self.visit(ctx.getChild(i)); i += 1
                return None
            else:
                i += 1
        return None

    def visitTipo(self, ctx:fase_3_parser.TipoContext):
        return self.visitChildren(ctx)

# 10.4 Definição de funções
    def visitFunc(self, ctx:fase_3_parser.FuncContext):
        func_name = ctx.ID().getText()
        self.funcs[func_name] = ctx
        return None

    def visitParams(self, ctx:fase_3_parser.ParamsContext):
        return self.visitChildren(ctx)

    def visitParam(self, ctx:fase_3_parser.ParamContext):
        return self.visitChildren(ctx)

 # 10.8 Chamada de funções
    def visitFunc_call(self, ctx:fase_3_parser.Func_callContext):
        func_name = ctx.ID().getText()
        args = [self.visit(a) for a in ctx.args().expr()] if ctx.args() else []

        if func_name in self.funcs:
            func_ctx = self.funcs[func_name]
            param_names = [p.ID().getText() for p in func_ctx.params().param()] if func_ctx.params() else []
            saved = dict(self.vars)
            for name, val in zip(param_names, args):
                self.vars[name] = val
            result = None
            try:
                for c in func_ctx.corpo():
                    self.visit(c)
            except ReturnException as r:
                result = r.value
            self.vars = saved
            return result

        builtin = __builtins__.get(func_name) if isinstance(__builtins__, dict) else getattr(__builtins__, func_name, None)
        if builtin:
            return builtin(*args)
        raise NameError(f"Função '{func_name}' não definida")

    def visitArgs(self, ctx:fase_3_parser.ArgsContext):
        return self.visitChildren(ctx)
 
 # 10.6 Loop while
    def visitLoop_while(self, ctx:fase_3_parser.Loop_whileContext):
        while self.visit(ctx.query()):
            for c in ctx.corpo():
                self.visit(c)
        return None

 # 10.7 Loop for
    def visitLoop_for(self, ctx:fase_3_parser.Loop_forContext):
        var_names = [t.getText() for t in ctx.for_vars().ID()]
        iterable  = self.visit(ctx.expr())

        loop_corpos, else_corpos, in_else = [], [], False
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if child.getText() == 'else':
                in_else = True
            elif type(child).__name__ == 'CorpoContext':
                (else_corpos if in_else else loop_corpos).append(child)

        for item in iterable:
            if len(var_names) == 1:
                self.vars[var_names[0]] = item
            else:
                for i, name in enumerate(var_names):
                    self.vars[name] = item[i]
            for c in loop_corpos:
                self.visit(c)

        for c in else_corpos:
            self.visit(c)

        return None

    def visitFor_vars(self, ctx:fase_3_parser.For_varsContext):
        return self.visitChildren(ctx)

    def visitLista(self, ctx:fase_3_parser.ListaContext):
        return [self.visit(e) for e in ctx.expr()]

    def visitTupla(self, ctx:fase_3_parser.TuplaContext):
        return tuple(self.visit(e) for e in ctx.expr())

    def visitSet_lit(self, ctx:fase_3_parser.Set_litContext):
        return {self.visit(e) for e in ctx.expr()}

    def visitDicionario(self, ctx:fase_3_parser.DicionarioContext):
        exprs = ctx.expr()
        return {self.visit(exprs[i]): self.visit(exprs[i+1]) for i in range(0, len(exprs), 2)}

del (fase_3_parser, fase_3_parserVisitor)
