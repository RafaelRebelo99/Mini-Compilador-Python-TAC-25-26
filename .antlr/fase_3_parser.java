// Generated from /Users/rafaelrebelo/Mini-Compilador-Python-TAC-25-26/fase_3_parser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class fase_3_parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		IF=1, ELIF=2, ELSE=3, FOR=4, WHILE=5, DEF=6, CLASS=7, TRY=8, EXCEPT=9, 
		FINALLY=10, WITH=11, MATCH=12, CASE=13, INT_TYPE=14, FLOAT_TYPE=15, STR_TYPE=16, 
		BOOL_TYPE=17, LIST_TYPE=18, TUPLE_TYPE=19, DICT_TYPE=20, SET_TYPE=21, 
		FROZENSET_TYPE=22, COMPLEX_TYPE=23, BYTES_TYPE=24, BYTEARRAY_TYPE=25, 
		MEMORYVIEW_TYPE=26, NONETYPE=27, AND=28, OR=29, NOT=30, IN=31, IS=32, 
		IMPORT=33, FROM=34, AS=35, RETURN=36, YIELD=37, PASS=38, BREAK=39, CONTINUE=40, 
		DEL=41, GLOBAL=42, NONLOCAL=43, RAISE=44, ASSERT=45, LAMBDA=46, TRUE=47, 
		FALSE=48, NONE=49, ASYNC=50, AWAIT=51, OP=52, EQ=53, NEQ=54, LTE=55, GTE=56, 
		LT=57, GT=58, LSHIFT=59, RSHIFT=60, AMPERSAND=61, PIPE=62, CARET=63, TILDE=64, 
		DOUBLE_SLASH_EQ=65, DOUBLE_STAR_EQ=66, LSHIFT_EQ=67, RSHIFT_EQ=68, WALRUS=69, 
		PLUS_EQ=70, MINUS_EQ=71, STAR_EQ=72, SLASH_EQ=73, PERCENT_EQ=74, AMPERSAND_EQ=75, 
		PIPE_EQ=76, CARET_EQ=77, ASSIGN=78, ARROW=79, ELLIPSIS=80, COLON=81, COMMA=82, 
		DOT=83, SEMICOLON=84, AT=85, LPAREN=86, RPAREN=87, LBRACKET=88, RBRACKET=89, 
		LBRACE=90, RBRACE=91, STRING=92, COMPLEX_LIT=93, FLOAT_LIT=94, HEX_LIT=95, 
		OCT_LIT=96, BIN_LIT=97, INT_LIT=98, COMMENT=99, ID=100, NEWLINE=101, WS=102;
	public static final int
		RULE_code = 0, RULE_stat = 1, RULE_assign = 2, RULE_expr = 3, RULE_ids = 4, 
		RULE_numeros = 5, RULE_query = 6, RULE_valoresBooleanos = 7, RULE_relacoesEntreExpressoes = 8, 
		RULE_corpo = 9, RULE_condicional = 10, RULE_tipo = 11, RULE_func = 12, 
		RULE_params = 13, RULE_param = 14, RULE_func_call = 15, RULE_args = 16, 
		RULE_loop_while = 17, RULE_loop_for = 18, RULE_for_vars = 19, RULE_lista = 20, 
		RULE_tupla = 21, RULE_set_lit = 22, RULE_dicionario = 23;
	private static String[] makeRuleNames() {
		return new String[] {
			"code", "stat", "assign", "expr", "ids", "numeros", "query", "valoresBooleanos", 
			"relacoesEntreExpressoes", "corpo", "condicional", "tipo", "func", "params", 
			"param", "func_call", "args", "loop_while", "loop_for", "for_vars", "lista", 
			"tupla", "set_lit", "dicionario"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'if'", "'elif'", "'else'", "'for'", "'while'", "'def'", "'class'", 
			"'try'", "'except'", "'finally'", "'with'", "'match'", "'case'", "'int'", 
			"'float'", "'str'", "'bool'", "'list'", "'tuple'", "'dict'", "'set'", 
			"'frozenset'", "'complex'", "'bytes'", "'bytearray'", "'memoryview'", 
			"'NoneType'", "'and'", "'or'", "'not'", "'in'", "'is'", "'import'", "'from'", 
			"'as'", "'return'", "'yield'", "'pass'", "'break'", "'continue'", "'del'", 
			"'global'", "'nonlocal'", "'raise'", "'assert'", "'lambda'", "'True'", 
			"'False'", "'None'", "'async'", "'await'", null, "'=='", "'!='", "'<='", 
			"'>='", "'<'", "'>'", "'<<'", "'>>'", "'&'", "'|'", "'^'", "'~'", "'//='", 
			"'**='", "'<<='", "'>>='", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", 
			"'&='", "'|='", "'^='", "'='", "'->'", "'...'", "':'", "','", "'.'", 
			"';'", "'@'", "'('", "')'", "'['", "']'", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "IF", "ELIF", "ELSE", "FOR", "WHILE", "DEF", "CLASS", "TRY", "EXCEPT", 
			"FINALLY", "WITH", "MATCH", "CASE", "INT_TYPE", "FLOAT_TYPE", "STR_TYPE", 
			"BOOL_TYPE", "LIST_TYPE", "TUPLE_TYPE", "DICT_TYPE", "SET_TYPE", "FROZENSET_TYPE", 
			"COMPLEX_TYPE", "BYTES_TYPE", "BYTEARRAY_TYPE", "MEMORYVIEW_TYPE", "NONETYPE", 
			"AND", "OR", "NOT", "IN", "IS", "IMPORT", "FROM", "AS", "RETURN", "YIELD", 
			"PASS", "BREAK", "CONTINUE", "DEL", "GLOBAL", "NONLOCAL", "RAISE", "ASSERT", 
			"LAMBDA", "TRUE", "FALSE", "NONE", "ASYNC", "AWAIT", "OP", "EQ", "NEQ", 
			"LTE", "GTE", "LT", "GT", "LSHIFT", "RSHIFT", "AMPERSAND", "PIPE", "CARET", 
			"TILDE", "DOUBLE_SLASH_EQ", "DOUBLE_STAR_EQ", "LSHIFT_EQ", "RSHIFT_EQ", 
			"WALRUS", "PLUS_EQ", "MINUS_EQ", "STAR_EQ", "SLASH_EQ", "PERCENT_EQ", 
			"AMPERSAND_EQ", "PIPE_EQ", "CARET_EQ", "ASSIGN", "ARROW", "ELLIPSIS", 
			"COLON", "COMMA", "DOT", "SEMICOLON", "AT", "LPAREN", "RPAREN", "LBRACKET", 
			"RBRACKET", "LBRACE", "RBRACE", "STRING", "COMPLEX_LIT", "FLOAT_LIT", 
			"HEX_LIT", "OCT_LIT", "BIN_LIT", "INT_LIT", "COMMENT", "ID", "NEWLINE", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "fase_3_parser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public fase_3_parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CodeContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(fase_3_parser.EOF, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(fase_3_parser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(fase_3_parser.NEWLINE, i);
		}
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public List<CondicionalContext> condicional() {
			return getRuleContexts(CondicionalContext.class);
		}
		public CondicionalContext condicional(int i) {
			return getRuleContext(CondicionalContext.class,i);
		}
		public List<FuncContext> func() {
			return getRuleContexts(FuncContext.class);
		}
		public FuncContext func(int i) {
			return getRuleContext(FuncContext.class,i);
		}
		public List<Func_callContext> func_call() {
			return getRuleContexts(Func_callContext.class);
		}
		public Func_callContext func_call(int i) {
			return getRuleContext(Func_callContext.class,i);
		}
		public List<Loop_whileContext> loop_while() {
			return getRuleContexts(Loop_whileContext.class);
		}
		public Loop_whileContext loop_while(int i) {
			return getRuleContext(Loop_whileContext.class,i);
		}
		public List<Loop_forContext> loop_for() {
			return getRuleContexts(Loop_forContext.class);
		}
		public Loop_forContext loop_for(int i) {
			return getRuleContext(Loop_forContext.class,i);
		}
		public CodeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_code; }
	}

	public final CodeContext code() throws RecognitionException {
		CodeContext _localctx = new CodeContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_code);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4927531153096818L) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & 240337813505L) != 0)) {
				{
				setState(57);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(48);
					match(NEWLINE);
					}
					break;
				case 2:
					{
					setState(49);
					stat();
					}
					break;
				case 3:
					{
					setState(50);
					condicional();
					}
					break;
				case 4:
					{
					setState(51);
					func();
					}
					break;
				case 5:
					{
					setState(52);
					func_call();
					setState(53);
					match(NEWLINE);
					}
					break;
				case 6:
					{
					setState(55);
					loop_while();
					}
					break;
				case 7:
					{
					setState(56);
					loop_for();
					}
					break;
				}
				}
				setState(61);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(62);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatContext extends ParserRuleContext {
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(fase_3_parser.NEWLINE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public QueryContext query() {
			return getRuleContext(QueryContext.class,0);
		}
		public TerminalNode BREAK() { return getToken(fase_3_parser.BREAK, 0); }
		public TerminalNode CONTINUE() { return getToken(fase_3_parser.CONTINUE, 0); }
		public TerminalNode RETURN() { return getToken(fase_3_parser.RETURN, 0); }
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stat);
		int _la;
		try {
			setState(82);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(64);
				assign();
				setState(65);
				match(NEWLINE);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(69);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
				case 1:
					{
					setState(67);
					expr(0);
					}
					break;
				case 2:
					{
					setState(68);
					query(0);
					}
					break;
				}
				setState(71);
				match(NEWLINE);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(73);
				match(BREAK);
				setState(74);
				match(NEWLINE);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(75);
				match(CONTINUE);
				setState(76);
				match(NEWLINE);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(77);
				match(RETURN);
				setState(79);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (((((_la - 52)) & ~0x3f) == 0 && ((1L << (_la - 52)) & 421473730691073L) != 0)) {
					{
					setState(78);
					expr(0);
					}
				}

				setState(81);
				match(NEWLINE);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(fase_3_parser.ID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(fase_3_parser.ASSIGN, 0); }
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			match(ID);
			{
			setState(85);
			match(ASSIGN);
			}
			setState(86);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public TerminalNode OP() { return getToken(fase_3_parser.OP, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode LPAREN() { return getToken(fase_3_parser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(fase_3_parser.RPAREN, 0); }
		public Func_callContext func_call() {
			return getRuleContext(Func_callContext.class,0);
		}
		public IdsContext ids() {
			return getRuleContext(IdsContext.class,0);
		}
		public NumerosContext numeros() {
			return getRuleContext(NumerosContext.class,0);
		}
		public TerminalNode STRING() { return getToken(fase_3_parser.STRING, 0); }
		public ListaContext lista() {
			return getRuleContext(ListaContext.class,0);
		}
		public TuplaContext tupla() {
			return getRuleContext(TuplaContext.class,0);
		}
		public Set_litContext set_lit() {
			return getRuleContext(Set_litContext.class,0);
		}
		public DicionarioContext dicionario() {
			return getRuleContext(DicionarioContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 6;
		enterRecursionRule(_localctx, 6, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(89);
				match(OP);
				setState(90);
				expr(10);
				}
				break;
			case 2:
				{
				setState(91);
				match(LPAREN);
				setState(92);
				expr(0);
				setState(93);
				match(RPAREN);
				}
				break;
			case 3:
				{
				setState(95);
				func_call();
				}
				break;
			case 4:
				{
				setState(96);
				ids();
				}
				break;
			case 5:
				{
				setState(97);
				numeros();
				}
				break;
			case 6:
				{
				setState(98);
				match(STRING);
				}
				break;
			case 7:
				{
				setState(99);
				lista();
				}
				break;
			case 8:
				{
				setState(100);
				tupla();
				}
				break;
			case 9:
				{
				setState(101);
				set_lit();
				}
				break;
			case 10:
				{
				setState(102);
				dicionario();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(110);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr);
					setState(105);
					if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
					setState(106);
					match(OP);
					setState(107);
					expr(12);
					}
					} 
				}
				setState(112);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdsContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(fase_3_parser.ID, 0); }
		public IdsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ids; }
	}

	public final IdsContext ids() throws RecognitionException {
		IdsContext _localctx = new IdsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_ids);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NumerosContext extends ParserRuleContext {
		public TerminalNode INT_LIT() { return getToken(fase_3_parser.INT_LIT, 0); }
		public TerminalNode FLOAT_LIT() { return getToken(fase_3_parser.FLOAT_LIT, 0); }
		public TerminalNode HEX_LIT() { return getToken(fase_3_parser.HEX_LIT, 0); }
		public TerminalNode OCT_LIT() { return getToken(fase_3_parser.OCT_LIT, 0); }
		public TerminalNode BIN_LIT() { return getToken(fase_3_parser.BIN_LIT, 0); }
		public TerminalNode COMPLEX_LIT() { return getToken(fase_3_parser.COMPLEX_LIT, 0); }
		public NumerosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_numeros; }
	}

	public final NumerosContext numeros() throws RecognitionException {
		NumerosContext _localctx = new NumerosContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_numeros);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			_la = _input.LA(1);
			if ( !(((((_la - 93)) & ~0x3f) == 0 && ((1L << (_la - 93)) & 63L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QueryContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(fase_3_parser.NOT, 0); }
		public List<QueryContext> query() {
			return getRuleContexts(QueryContext.class);
		}
		public QueryContext query(int i) {
			return getRuleContext(QueryContext.class,i);
		}
		public TerminalNode TILDE() { return getToken(fase_3_parser.TILDE, 0); }
		public TerminalNode LPAREN() { return getToken(fase_3_parser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(fase_3_parser.RPAREN, 0); }
		public ValoresBooleanosContext valoresBooleanos() {
			return getRuleContext(ValoresBooleanosContext.class,0);
		}
		public RelacoesEntreExpressoesContext relacoesEntreExpressoes() {
			return getRuleContext(RelacoesEntreExpressoesContext.class,0);
		}
		public Func_callContext func_call() {
			return getRuleContext(Func_callContext.class,0);
		}
		public TerminalNode AND() { return getToken(fase_3_parser.AND, 0); }
		public TerminalNode OR() { return getToken(fase_3_parser.OR, 0); }
		public TerminalNode AMPERSAND() { return getToken(fase_3_parser.AMPERSAND, 0); }
		public TerminalNode PIPE() { return getToken(fase_3_parser.PIPE, 0); }
		public TerminalNode CARET() { return getToken(fase_3_parser.CARET, 0); }
		public QueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_query; }
	}

	public final QueryContext query() throws RecognitionException {
		return query(0);
	}

	private QueryContext query(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		QueryContext _localctx = new QueryContext(_ctx, _parentState);
		QueryContext _prevctx = _localctx;
		int _startState = 12;
		enterRecursionRule(_localctx, 12, RULE_query, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				setState(118);
				match(NOT);
				setState(119);
				query(6);
				}
				break;
			case 2:
				{
				setState(120);
				match(TILDE);
				setState(121);
				query(5);
				}
				break;
			case 3:
				{
				setState(122);
				match(LPAREN);
				setState(123);
				query(0);
				setState(124);
				match(RPAREN);
				}
				break;
			case 4:
				{
				setState(126);
				valoresBooleanos();
				}
				break;
			case 5:
				{
				setState(127);
				relacoesEntreExpressoes();
				}
				break;
			case 6:
				{
				setState(128);
				func_call();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(136);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new QueryContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_query);
					setState(131);
					if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
					setState(132);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & -2305843008408387584L) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(133);
					query(8);
					}
					} 
				}
				setState(138);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValoresBooleanosContext extends ParserRuleContext {
		public TerminalNode TRUE() { return getToken(fase_3_parser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(fase_3_parser.FALSE, 0); }
		public ValoresBooleanosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_valoresBooleanos; }
	}

	public final ValoresBooleanosContext valoresBooleanos() throws RecognitionException {
		ValoresBooleanosContext _localctx = new ValoresBooleanosContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_valoresBooleanos);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			_la = _input.LA(1);
			if ( !(_la==TRUE || _la==FALSE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RelacoesEntreExpressoesContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode EQ() { return getToken(fase_3_parser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(fase_3_parser.NEQ, 0); }
		public TerminalNode LT() { return getToken(fase_3_parser.LT, 0); }
		public TerminalNode GT() { return getToken(fase_3_parser.GT, 0); }
		public TerminalNode LTE() { return getToken(fase_3_parser.LTE, 0); }
		public TerminalNode GTE() { return getToken(fase_3_parser.GTE, 0); }
		public RelacoesEntreExpressoesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relacoesEntreExpressoes; }
	}

	public final RelacoesEntreExpressoesContext relacoesEntreExpressoes() throws RecognitionException {
		RelacoesEntreExpressoesContext _localctx = new RelacoesEntreExpressoesContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_relacoesEntreExpressoes);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			expr(0);
			setState(142);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 567453553048682496L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(143);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CorpoContext extends ParserRuleContext {
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public FuncContext func() {
			return getRuleContext(FuncContext.class,0);
		}
		public CondicionalContext condicional() {
			return getRuleContext(CondicionalContext.class,0);
		}
		public Loop_whileContext loop_while() {
			return getRuleContext(Loop_whileContext.class,0);
		}
		public Loop_forContext loop_for() {
			return getRuleContext(Loop_forContext.class,0);
		}
		public CorpoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_corpo; }
	}

	public final CorpoContext corpo() throws RecognitionException {
		CorpoContext _localctx = new CorpoContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_corpo);
		try {
			setState(150);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
			case RETURN:
			case BREAK:
			case CONTINUE:
			case TRUE:
			case FALSE:
			case OP:
			case TILDE:
			case LPAREN:
			case LBRACKET:
			case LBRACE:
			case STRING:
			case COMPLEX_LIT:
			case FLOAT_LIT:
			case HEX_LIT:
			case OCT_LIT:
			case BIN_LIT:
			case INT_LIT:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(145);
				stat();
				}
				break;
			case DEF:
				enterOuterAlt(_localctx, 2);
				{
				setState(146);
				func();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 3);
				{
				setState(147);
				condicional();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 4);
				{
				setState(148);
				loop_while();
				}
				break;
			case FOR:
				enterOuterAlt(_localctx, 5);
				{
				setState(149);
				loop_for();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondicionalContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(fase_3_parser.IF, 0); }
		public List<QueryContext> query() {
			return getRuleContexts(QueryContext.class);
		}
		public QueryContext query(int i) {
			return getRuleContext(QueryContext.class,i);
		}
		public List<TerminalNode> COLON() { return getTokens(fase_3_parser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(fase_3_parser.COLON, i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(fase_3_parser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(fase_3_parser.NEWLINE, i);
		}
		public List<CorpoContext> corpo() {
			return getRuleContexts(CorpoContext.class);
		}
		public CorpoContext corpo(int i) {
			return getRuleContext(CorpoContext.class,i);
		}
		public List<TerminalNode> ELIF() { return getTokens(fase_3_parser.ELIF); }
		public TerminalNode ELIF(int i) {
			return getToken(fase_3_parser.ELIF, i);
		}
		public TerminalNode ELSE() { return getToken(fase_3_parser.ELSE, 0); }
		public CondicionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicional; }
	}

	public final CondicionalContext condicional() throws RecognitionException {
		CondicionalContext _localctx = new CondicionalContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_condicional);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(152);
			match(IF);
			setState(153);
			query(0);
			setState(154);
			match(COLON);
			setState(155);
			match(NEWLINE);
			setState(157); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(156);
					corpo();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(159); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(172);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(161);
					match(ELIF);
					setState(162);
					query(0);
					setState(163);
					match(COLON);
					setState(164);
					match(NEWLINE);
					setState(166); 
					_errHandler.sync(this);
					_alt = 1;
					do {
						switch (_alt) {
						case 1:
							{
							{
							setState(165);
							corpo();
							}
							}
							break;
						default:
							throw new NoViableAltException(this);
						}
						setState(168); 
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
					} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
					}
					} 
				}
				setState(174);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			setState(183);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				setState(175);
				match(ELSE);
				setState(176);
				match(COLON);
				setState(177);
				match(NEWLINE);
				setState(179); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(178);
						corpo();
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(181); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TipoContext extends ParserRuleContext {
		public TerminalNode INT_TYPE() { return getToken(fase_3_parser.INT_TYPE, 0); }
		public TerminalNode FLOAT_TYPE() { return getToken(fase_3_parser.FLOAT_TYPE, 0); }
		public TerminalNode STR_TYPE() { return getToken(fase_3_parser.STR_TYPE, 0); }
		public TerminalNode BOOL_TYPE() { return getToken(fase_3_parser.BOOL_TYPE, 0); }
		public TerminalNode ID() { return getToken(fase_3_parser.ID, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(185);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 245760L) != 0) || _la==ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncContext extends ParserRuleContext {
		public TerminalNode DEF() { return getToken(fase_3_parser.DEF, 0); }
		public TerminalNode ID() { return getToken(fase_3_parser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(fase_3_parser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(fase_3_parser.RPAREN, 0); }
		public TerminalNode COLON() { return getToken(fase_3_parser.COLON, 0); }
		public TerminalNode NEWLINE() { return getToken(fase_3_parser.NEWLINE, 0); }
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public TerminalNode ARROW() { return getToken(fase_3_parser.ARROW, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public List<CorpoContext> corpo() {
			return getRuleContexts(CorpoContext.class);
		}
		public CorpoContext corpo(int i) {
			return getRuleContext(CorpoContext.class,i);
		}
		public FuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func; }
	}

	public final FuncContext func() throws RecognitionException {
		FuncContext _localctx = new FuncContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_func);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(187);
			match(DEF);
			setState(188);
			match(ID);
			setState(189);
			match(LPAREN);
			setState(191);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(190);
				params();
				}
			}

			setState(193);
			match(RPAREN);
			setState(196);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ARROW) {
				{
				setState(194);
				match(ARROW);
				setState(195);
				tipo();
				}
			}

			setState(198);
			match(COLON);
			setState(199);
			match(NEWLINE);
			setState(201); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(200);
					corpo();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(203); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamsContext extends ParserRuleContext {
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(fase_3_parser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(fase_3_parser.COMMA, i);
		}
		public ParamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params; }
	}

	public final ParamsContext params() throws RecognitionException {
		ParamsContext _localctx = new ParamsContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_params);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(205);
			param();
			setState(210);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(206);
				match(COMMA);
				setState(207);
				param();
				}
				}
				setState(212);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(fase_3_parser.ID, 0); }
		public TerminalNode COLON() { return getToken(fase_3_parser.COLON, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_param);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			match(ID);
			setState(216);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COLON) {
				{
				setState(214);
				match(COLON);
				setState(215);
				tipo();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Func_callContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(fase_3_parser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(fase_3_parser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(fase_3_parser.RPAREN, 0); }
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public Func_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_call; }
	}

	public final Func_callContext func_call() throws RecognitionException {
		Func_callContext _localctx = new Func_callContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_func_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(218);
			match(ID);
			setState(219);
			match(LPAREN);
			setState(221);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 52)) & ~0x3f) == 0 && ((1L << (_la - 52)) & 421473730691073L) != 0)) {
				{
				setState(220);
				args();
				}
			}

			setState(223);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgsContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(fase_3_parser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(fase_3_parser.COMMA, i);
		}
		public ArgsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_args; }
	}

	public final ArgsContext args() throws RecognitionException {
		ArgsContext _localctx = new ArgsContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_args);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(225);
			expr(0);
			setState(230);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(226);
				match(COMMA);
				setState(227);
				expr(0);
				}
				}
				setState(232);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Loop_whileContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(fase_3_parser.WHILE, 0); }
		public QueryContext query() {
			return getRuleContext(QueryContext.class,0);
		}
		public TerminalNode COLON() { return getToken(fase_3_parser.COLON, 0); }
		public TerminalNode NEWLINE() { return getToken(fase_3_parser.NEWLINE, 0); }
		public List<CorpoContext> corpo() {
			return getRuleContexts(CorpoContext.class);
		}
		public CorpoContext corpo(int i) {
			return getRuleContext(CorpoContext.class,i);
		}
		public Loop_whileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loop_while; }
	}

	public final Loop_whileContext loop_while() throws RecognitionException {
		Loop_whileContext _localctx = new Loop_whileContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_loop_while);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(233);
			match(WHILE);
			setState(234);
			query(0);
			setState(235);
			match(COLON);
			setState(236);
			match(NEWLINE);
			setState(238); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(237);
					corpo();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(240); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Loop_forContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(fase_3_parser.FOR, 0); }
		public For_varsContext for_vars() {
			return getRuleContext(For_varsContext.class,0);
		}
		public TerminalNode IN() { return getToken(fase_3_parser.IN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<TerminalNode> COLON() { return getTokens(fase_3_parser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(fase_3_parser.COLON, i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(fase_3_parser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(fase_3_parser.NEWLINE, i);
		}
		public List<CorpoContext> corpo() {
			return getRuleContexts(CorpoContext.class);
		}
		public CorpoContext corpo(int i) {
			return getRuleContext(CorpoContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(fase_3_parser.ELSE, 0); }
		public Loop_forContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loop_for; }
	}

	public final Loop_forContext loop_for() throws RecognitionException {
		Loop_forContext _localctx = new Loop_forContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_loop_for);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(242);
			match(FOR);
			setState(243);
			for_vars();
			setState(244);
			match(IN);
			setState(245);
			expr(0);
			setState(246);
			match(COLON);
			setState(247);
			match(NEWLINE);
			setState(249); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(248);
					corpo();
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(251); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(261);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				{
				setState(253);
				match(ELSE);
				setState(254);
				match(COLON);
				setState(255);
				match(NEWLINE);
				setState(257); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(256);
						corpo();
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(259); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_varsContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(fase_3_parser.ID); }
		public TerminalNode ID(int i) {
			return getToken(fase_3_parser.ID, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(fase_3_parser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(fase_3_parser.COMMA, i);
		}
		public For_varsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_vars; }
	}

	public final For_varsContext for_vars() throws RecognitionException {
		For_varsContext _localctx = new For_varsContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_for_vars);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(263);
			match(ID);
			setState(268);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(264);
				match(COMMA);
				setState(265);
				match(ID);
				}
				}
				setState(270);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListaContext extends ParserRuleContext {
		public TerminalNode LBRACKET() { return getToken(fase_3_parser.LBRACKET, 0); }
		public TerminalNode RBRACKET() { return getToken(fase_3_parser.RBRACKET, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(fase_3_parser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(fase_3_parser.COMMA, i);
		}
		public ListaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista; }
	}

	public final ListaContext lista() throws RecognitionException {
		ListaContext _localctx = new ListaContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_lista);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(271);
			match(LBRACKET);
			setState(280);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 52)) & ~0x3f) == 0 && ((1L << (_la - 52)) & 421473730691073L) != 0)) {
				{
				setState(272);
				expr(0);
				setState(277);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(273);
					match(COMMA);
					setState(274);
					expr(0);
					}
					}
					setState(279);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(282);
			match(RBRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TuplaContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(fase_3_parser.LPAREN, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(fase_3_parser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(fase_3_parser.COMMA, i);
		}
		public TerminalNode RPAREN() { return getToken(fase_3_parser.RPAREN, 0); }
		public TuplaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tupla; }
	}

	public final TuplaContext tupla() throws RecognitionException {
		TuplaContext _localctx = new TuplaContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_tupla);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(284);
			match(LPAREN);
			setState(285);
			expr(0);
			setState(286);
			match(COMMA);
			setState(295);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 52)) & ~0x3f) == 0 && ((1L << (_la - 52)) & 421473730691073L) != 0)) {
				{
				setState(287);
				expr(0);
				setState(292);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(288);
					match(COMMA);
					setState(289);
					expr(0);
					}
					}
					setState(294);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(297);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Set_litContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(fase_3_parser.LBRACE, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode RBRACE() { return getToken(fase_3_parser.RBRACE, 0); }
		public List<TerminalNode> COMMA() { return getTokens(fase_3_parser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(fase_3_parser.COMMA, i);
		}
		public Set_litContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_set_lit; }
	}

	public final Set_litContext set_lit() throws RecognitionException {
		Set_litContext _localctx = new Set_litContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_set_lit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(299);
			match(LBRACE);
			setState(300);
			expr(0);
			setState(303); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(301);
				match(COMMA);
				setState(302);
				expr(0);
				}
				}
				setState(305); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==COMMA );
			setState(307);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DicionarioContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(fase_3_parser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(fase_3_parser.RBRACE, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COLON() { return getTokens(fase_3_parser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(fase_3_parser.COLON, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(fase_3_parser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(fase_3_parser.COMMA, i);
		}
		public DicionarioContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dicionario; }
	}

	public final DicionarioContext dicionario() throws RecognitionException {
		DicionarioContext _localctx = new DicionarioContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_dicionario);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(309);
			match(LBRACE);
			setState(323);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 52)) & ~0x3f) == 0 && ((1L << (_la - 52)) & 421473730691073L) != 0)) {
				{
				setState(310);
				expr(0);
				setState(311);
				match(COLON);
				setState(312);
				expr(0);
				setState(320);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(313);
					match(COMMA);
					setState(314);
					expr(0);
					setState(315);
					match(COLON);
					setState(316);
					expr(0);
					}
					}
					setState(322);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(325);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 3:
			return expr_sempred((ExprContext)_localctx, predIndex);
		case 6:
			return query_sempred((QueryContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 11);
		}
		return true;
	}
	private boolean query_sempred(QueryContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 7);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001f\u0148\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0005\u0000:\b\u0000\n\u0000\f\u0000=\t\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0003\u0001F\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001P\b\u0001"+
		"\u0001\u0001\u0003\u0001S\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003h\b\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0005\u0003m\b\u0003\n\u0003\f\u0003"+
		"p\t\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006"+
		"\u0082\b\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0005\u0006\u0087\b"+
		"\u0006\n\u0006\f\u0006\u008a\t\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003\t\u0097"+
		"\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0004\n\u009e\b\n\u000b\n"+
		"\f\n\u009f\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0004\n\u00a7\b\n\u000b"+
		"\n\f\n\u00a8\u0005\n\u00ab\b\n\n\n\f\n\u00ae\t\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0004\n\u00b4\b\n\u000b\n\f\n\u00b5\u0003\n\u00b8\b\n\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0003\f\u00c0\b\f\u0001"+
		"\f\u0001\f\u0001\f\u0003\f\u00c5\b\f\u0001\f\u0001\f\u0001\f\u0004\f\u00ca"+
		"\b\f\u000b\f\f\f\u00cb\u0001\r\u0001\r\u0001\r\u0005\r\u00d1\b\r\n\r\f"+
		"\r\u00d4\t\r\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u00d9\b\u000e"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u00de\b\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u00e5\b\u0010"+
		"\n\u0010\f\u0010\u00e8\t\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0004\u0011\u00ef\b\u0011\u000b\u0011\f\u0011\u00f0"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0004\u0012\u00fa\b\u0012\u000b\u0012\f\u0012\u00fb\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0004\u0012\u0102\b\u0012\u000b"+
		"\u0012\f\u0012\u0103\u0003\u0012\u0106\b\u0012\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0005\u0013\u010b\b\u0013\n\u0013\f\u0013\u010e\t\u0013\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0005\u0014\u0114\b\u0014\n"+
		"\u0014\f\u0014\u0117\t\u0014\u0003\u0014\u0119\b\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0005\u0015\u0123\b\u0015\n\u0015\f\u0015\u0126\t\u0015\u0003\u0015"+
		"\u0128\b\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0004\u0016\u0130\b\u0016\u000b\u0016\f\u0016\u0131\u0001"+
		"\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0005\u0017\u013f"+
		"\b\u0017\n\u0017\f\u0017\u0142\t\u0017\u0003\u0017\u0144\b\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0017\u0000\u0002\u0006\f\u0018\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \""+
		"$&(*,.\u0000\u0005\u0001\u0000]b\u0002\u0000\u001c\u001d=?\u0001\u0000"+
		"/0\u0001\u00005:\u0002\u0000\u000e\u0011dd\u0168\u0000;\u0001\u0000\u0000"+
		"\u0000\u0002R\u0001\u0000\u0000\u0000\u0004T\u0001\u0000\u0000\u0000\u0006"+
		"g\u0001\u0000\u0000\u0000\bq\u0001\u0000\u0000\u0000\ns\u0001\u0000\u0000"+
		"\u0000\f\u0081\u0001\u0000\u0000\u0000\u000e\u008b\u0001\u0000\u0000\u0000"+
		"\u0010\u008d\u0001\u0000\u0000\u0000\u0012\u0096\u0001\u0000\u0000\u0000"+
		"\u0014\u0098\u0001\u0000\u0000\u0000\u0016\u00b9\u0001\u0000\u0000\u0000"+
		"\u0018\u00bb\u0001\u0000\u0000\u0000\u001a\u00cd\u0001\u0000\u0000\u0000"+
		"\u001c\u00d5\u0001\u0000\u0000\u0000\u001e\u00da\u0001\u0000\u0000\u0000"+
		" \u00e1\u0001\u0000\u0000\u0000\"\u00e9\u0001\u0000\u0000\u0000$\u00f2"+
		"\u0001\u0000\u0000\u0000&\u0107\u0001\u0000\u0000\u0000(\u010f\u0001\u0000"+
		"\u0000\u0000*\u011c\u0001\u0000\u0000\u0000,\u012b\u0001\u0000\u0000\u0000"+
		".\u0135\u0001\u0000\u0000\u00000:\u0005e\u0000\u00001:\u0003\u0002\u0001"+
		"\u00002:\u0003\u0014\n\u00003:\u0003\u0018\f\u000045\u0003\u001e\u000f"+
		"\u000056\u0005e\u0000\u00006:\u0001\u0000\u0000\u00007:\u0003\"\u0011"+
		"\u00008:\u0003$\u0012\u000090\u0001\u0000\u0000\u000091\u0001\u0000\u0000"+
		"\u000092\u0001\u0000\u0000\u000093\u0001\u0000\u0000\u000094\u0001\u0000"+
		"\u0000\u000097\u0001\u0000\u0000\u000098\u0001\u0000\u0000\u0000:=\u0001"+
		"\u0000\u0000\u0000;9\u0001\u0000\u0000\u0000;<\u0001\u0000\u0000\u0000"+
		"<>\u0001\u0000\u0000\u0000=;\u0001\u0000\u0000\u0000>?\u0005\u0000\u0000"+
		"\u0001?\u0001\u0001\u0000\u0000\u0000@A\u0003\u0004\u0002\u0000AB\u0005"+
		"e\u0000\u0000BS\u0001\u0000\u0000\u0000CF\u0003\u0006\u0003\u0000DF\u0003"+
		"\f\u0006\u0000EC\u0001\u0000\u0000\u0000ED\u0001\u0000\u0000\u0000FG\u0001"+
		"\u0000\u0000\u0000GH\u0005e\u0000\u0000HS\u0001\u0000\u0000\u0000IJ\u0005"+
		"\'\u0000\u0000JS\u0005e\u0000\u0000KL\u0005(\u0000\u0000LS\u0005e\u0000"+
		"\u0000MO\u0005$\u0000\u0000NP\u0003\u0006\u0003\u0000ON\u0001\u0000\u0000"+
		"\u0000OP\u0001\u0000\u0000\u0000PQ\u0001\u0000\u0000\u0000QS\u0005e\u0000"+
		"\u0000R@\u0001\u0000\u0000\u0000RE\u0001\u0000\u0000\u0000RI\u0001\u0000"+
		"\u0000\u0000RK\u0001\u0000\u0000\u0000RM\u0001\u0000\u0000\u0000S\u0003"+
		"\u0001\u0000\u0000\u0000TU\u0005d\u0000\u0000UV\u0005N\u0000\u0000VW\u0003"+
		"\u0006\u0003\u0000W\u0005\u0001\u0000\u0000\u0000XY\u0006\u0003\uffff"+
		"\uffff\u0000YZ\u00054\u0000\u0000Zh\u0003\u0006\u0003\n[\\\u0005V\u0000"+
		"\u0000\\]\u0003\u0006\u0003\u0000]^\u0005W\u0000\u0000^h\u0001\u0000\u0000"+
		"\u0000_h\u0003\u001e\u000f\u0000`h\u0003\b\u0004\u0000ah\u0003\n\u0005"+
		"\u0000bh\u0005\\\u0000\u0000ch\u0003(\u0014\u0000dh\u0003*\u0015\u0000"+
		"eh\u0003,\u0016\u0000fh\u0003.\u0017\u0000gX\u0001\u0000\u0000\u0000g"+
		"[\u0001\u0000\u0000\u0000g_\u0001\u0000\u0000\u0000g`\u0001\u0000\u0000"+
		"\u0000ga\u0001\u0000\u0000\u0000gb\u0001\u0000\u0000\u0000gc\u0001\u0000"+
		"\u0000\u0000gd\u0001\u0000\u0000\u0000ge\u0001\u0000\u0000\u0000gf\u0001"+
		"\u0000\u0000\u0000hn\u0001\u0000\u0000\u0000ij\n\u000b\u0000\u0000jk\u0005"+
		"4\u0000\u0000km\u0003\u0006\u0003\fli\u0001\u0000\u0000\u0000mp\u0001"+
		"\u0000\u0000\u0000nl\u0001\u0000\u0000\u0000no\u0001\u0000\u0000\u0000"+
		"o\u0007\u0001\u0000\u0000\u0000pn\u0001\u0000\u0000\u0000qr\u0005d\u0000"+
		"\u0000r\t\u0001\u0000\u0000\u0000st\u0007\u0000\u0000\u0000t\u000b\u0001"+
		"\u0000\u0000\u0000uv\u0006\u0006\uffff\uffff\u0000vw\u0005\u001e\u0000"+
		"\u0000w\u0082\u0003\f\u0006\u0006xy\u0005@\u0000\u0000y\u0082\u0003\f"+
		"\u0006\u0005z{\u0005V\u0000\u0000{|\u0003\f\u0006\u0000|}\u0005W\u0000"+
		"\u0000}\u0082\u0001\u0000\u0000\u0000~\u0082\u0003\u000e\u0007\u0000\u007f"+
		"\u0082\u0003\u0010\b\u0000\u0080\u0082\u0003\u001e\u000f\u0000\u0081u"+
		"\u0001\u0000\u0000\u0000\u0081x\u0001\u0000\u0000\u0000\u0081z\u0001\u0000"+
		"\u0000\u0000\u0081~\u0001\u0000\u0000\u0000\u0081\u007f\u0001\u0000\u0000"+
		"\u0000\u0081\u0080\u0001\u0000\u0000\u0000\u0082\u0088\u0001\u0000\u0000"+
		"\u0000\u0083\u0084\n\u0007\u0000\u0000\u0084\u0085\u0007\u0001\u0000\u0000"+
		"\u0085\u0087\u0003\f\u0006\b\u0086\u0083\u0001\u0000\u0000\u0000\u0087"+
		"\u008a\u0001\u0000\u0000\u0000\u0088\u0086\u0001\u0000\u0000\u0000\u0088"+
		"\u0089\u0001\u0000\u0000\u0000\u0089\r\u0001\u0000\u0000\u0000\u008a\u0088"+
		"\u0001\u0000\u0000\u0000\u008b\u008c\u0007\u0002\u0000\u0000\u008c\u000f"+
		"\u0001\u0000\u0000\u0000\u008d\u008e\u0003\u0006\u0003\u0000\u008e\u008f"+
		"\u0007\u0003\u0000\u0000\u008f\u0090\u0003\u0006\u0003\u0000\u0090\u0011"+
		"\u0001\u0000\u0000\u0000\u0091\u0097\u0003\u0002\u0001\u0000\u0092\u0097"+
		"\u0003\u0018\f\u0000\u0093\u0097\u0003\u0014\n\u0000\u0094\u0097\u0003"+
		"\"\u0011\u0000\u0095\u0097\u0003$\u0012\u0000\u0096\u0091\u0001\u0000"+
		"\u0000\u0000\u0096\u0092\u0001\u0000\u0000\u0000\u0096\u0093\u0001\u0000"+
		"\u0000\u0000\u0096\u0094\u0001\u0000\u0000\u0000\u0096\u0095\u0001\u0000"+
		"\u0000\u0000\u0097\u0013\u0001\u0000\u0000\u0000\u0098\u0099\u0005\u0001"+
		"\u0000\u0000\u0099\u009a\u0003\f\u0006\u0000\u009a\u009b\u0005Q\u0000"+
		"\u0000\u009b\u009d\u0005e\u0000\u0000\u009c\u009e\u0003\u0012\t\u0000"+
		"\u009d\u009c\u0001\u0000\u0000\u0000\u009e\u009f\u0001\u0000\u0000\u0000"+
		"\u009f\u009d\u0001\u0000\u0000\u0000\u009f\u00a0\u0001\u0000\u0000\u0000"+
		"\u00a0\u00ac\u0001\u0000\u0000\u0000\u00a1\u00a2\u0005\u0002\u0000\u0000"+
		"\u00a2\u00a3\u0003\f\u0006\u0000\u00a3\u00a4\u0005Q\u0000\u0000\u00a4"+
		"\u00a6\u0005e\u0000\u0000\u00a5\u00a7\u0003\u0012\t\u0000\u00a6\u00a5"+
		"\u0001\u0000\u0000\u0000\u00a7\u00a8\u0001\u0000\u0000\u0000\u00a8\u00a6"+
		"\u0001\u0000\u0000\u0000\u00a8\u00a9\u0001\u0000\u0000\u0000\u00a9\u00ab"+
		"\u0001\u0000\u0000\u0000\u00aa\u00a1\u0001\u0000\u0000\u0000\u00ab\u00ae"+
		"\u0001\u0000\u0000\u0000\u00ac\u00aa\u0001\u0000\u0000\u0000\u00ac\u00ad"+
		"\u0001\u0000\u0000\u0000\u00ad\u00b7\u0001\u0000\u0000\u0000\u00ae\u00ac"+
		"\u0001\u0000\u0000\u0000\u00af\u00b0\u0005\u0003\u0000\u0000\u00b0\u00b1"+
		"\u0005Q\u0000\u0000\u00b1\u00b3\u0005e\u0000\u0000\u00b2\u00b4\u0003\u0012"+
		"\t\u0000\u00b3\u00b2\u0001\u0000\u0000\u0000\u00b4\u00b5\u0001\u0000\u0000"+
		"\u0000\u00b5\u00b3\u0001\u0000\u0000\u0000\u00b5\u00b6\u0001\u0000\u0000"+
		"\u0000\u00b6\u00b8\u0001\u0000\u0000\u0000\u00b7\u00af\u0001\u0000\u0000"+
		"\u0000\u00b7\u00b8\u0001\u0000\u0000\u0000\u00b8\u0015\u0001\u0000\u0000"+
		"\u0000\u00b9\u00ba\u0007\u0004\u0000\u0000\u00ba\u0017\u0001\u0000\u0000"+
		"\u0000\u00bb\u00bc\u0005\u0006\u0000\u0000\u00bc\u00bd\u0005d\u0000\u0000"+
		"\u00bd\u00bf\u0005V\u0000\u0000\u00be\u00c0\u0003\u001a\r\u0000\u00bf"+
		"\u00be\u0001\u0000\u0000\u0000\u00bf\u00c0\u0001\u0000\u0000\u0000\u00c0"+
		"\u00c1\u0001\u0000\u0000\u0000\u00c1\u00c4\u0005W\u0000\u0000\u00c2\u00c3"+
		"\u0005O\u0000\u0000\u00c3\u00c5\u0003\u0016\u000b\u0000\u00c4\u00c2\u0001"+
		"\u0000\u0000\u0000\u00c4\u00c5\u0001\u0000\u0000\u0000\u00c5\u00c6\u0001"+
		"\u0000\u0000\u0000\u00c6\u00c7\u0005Q\u0000\u0000\u00c7\u00c9\u0005e\u0000"+
		"\u0000\u00c8\u00ca\u0003\u0012\t\u0000\u00c9\u00c8\u0001\u0000\u0000\u0000"+
		"\u00ca\u00cb\u0001\u0000\u0000\u0000\u00cb\u00c9\u0001\u0000\u0000\u0000"+
		"\u00cb\u00cc\u0001\u0000\u0000\u0000\u00cc\u0019\u0001\u0000\u0000\u0000"+
		"\u00cd\u00d2\u0003\u001c\u000e\u0000\u00ce\u00cf\u0005R\u0000\u0000\u00cf"+
		"\u00d1\u0003\u001c\u000e\u0000\u00d0\u00ce\u0001\u0000\u0000\u0000\u00d1"+
		"\u00d4\u0001\u0000\u0000\u0000\u00d2\u00d0\u0001\u0000\u0000\u0000\u00d2"+
		"\u00d3\u0001\u0000\u0000\u0000\u00d3\u001b\u0001\u0000\u0000\u0000\u00d4"+
		"\u00d2\u0001\u0000\u0000\u0000\u00d5\u00d8\u0005d\u0000\u0000\u00d6\u00d7"+
		"\u0005Q\u0000\u0000\u00d7\u00d9\u0003\u0016\u000b\u0000\u00d8\u00d6\u0001"+
		"\u0000\u0000\u0000\u00d8\u00d9\u0001\u0000\u0000\u0000\u00d9\u001d\u0001"+
		"\u0000\u0000\u0000\u00da\u00db\u0005d\u0000\u0000\u00db\u00dd\u0005V\u0000"+
		"\u0000\u00dc\u00de\u0003 \u0010\u0000\u00dd\u00dc\u0001\u0000\u0000\u0000"+
		"\u00dd\u00de\u0001\u0000\u0000\u0000\u00de\u00df\u0001\u0000\u0000\u0000"+
		"\u00df\u00e0\u0005W\u0000\u0000\u00e0\u001f\u0001\u0000\u0000\u0000\u00e1"+
		"\u00e6\u0003\u0006\u0003\u0000\u00e2\u00e3\u0005R\u0000\u0000\u00e3\u00e5"+
		"\u0003\u0006\u0003\u0000\u00e4\u00e2\u0001\u0000\u0000\u0000\u00e5\u00e8"+
		"\u0001\u0000\u0000\u0000\u00e6\u00e4\u0001\u0000\u0000\u0000\u00e6\u00e7"+
		"\u0001\u0000\u0000\u0000\u00e7!\u0001\u0000\u0000\u0000\u00e8\u00e6\u0001"+
		"\u0000\u0000\u0000\u00e9\u00ea\u0005\u0005\u0000\u0000\u00ea\u00eb\u0003"+
		"\f\u0006\u0000\u00eb\u00ec\u0005Q\u0000\u0000\u00ec\u00ee\u0005e\u0000"+
		"\u0000\u00ed\u00ef\u0003\u0012\t\u0000\u00ee\u00ed\u0001\u0000\u0000\u0000"+
		"\u00ef\u00f0\u0001\u0000\u0000\u0000\u00f0\u00ee\u0001\u0000\u0000\u0000"+
		"\u00f0\u00f1\u0001\u0000\u0000\u0000\u00f1#\u0001\u0000\u0000\u0000\u00f2"+
		"\u00f3\u0005\u0004\u0000\u0000\u00f3\u00f4\u0003&\u0013\u0000\u00f4\u00f5"+
		"\u0005\u001f\u0000\u0000\u00f5\u00f6\u0003\u0006\u0003\u0000\u00f6\u00f7"+
		"\u0005Q\u0000\u0000\u00f7\u00f9\u0005e\u0000\u0000\u00f8\u00fa\u0003\u0012"+
		"\t\u0000\u00f9\u00f8\u0001\u0000\u0000\u0000\u00fa\u00fb\u0001\u0000\u0000"+
		"\u0000\u00fb\u00f9\u0001\u0000\u0000\u0000\u00fb\u00fc\u0001\u0000\u0000"+
		"\u0000\u00fc\u0105\u0001\u0000\u0000\u0000\u00fd\u00fe\u0005\u0003\u0000"+
		"\u0000\u00fe\u00ff\u0005Q\u0000\u0000\u00ff\u0101\u0005e\u0000\u0000\u0100"+
		"\u0102\u0003\u0012\t\u0000\u0101\u0100\u0001\u0000\u0000\u0000\u0102\u0103"+
		"\u0001\u0000\u0000\u0000\u0103\u0101\u0001\u0000\u0000\u0000\u0103\u0104"+
		"\u0001\u0000\u0000\u0000\u0104\u0106\u0001\u0000\u0000\u0000\u0105\u00fd"+
		"\u0001\u0000\u0000\u0000\u0105\u0106\u0001\u0000\u0000\u0000\u0106%\u0001"+
		"\u0000\u0000\u0000\u0107\u010c\u0005d\u0000\u0000\u0108\u0109\u0005R\u0000"+
		"\u0000\u0109\u010b\u0005d\u0000\u0000\u010a\u0108\u0001\u0000\u0000\u0000"+
		"\u010b\u010e\u0001\u0000\u0000\u0000\u010c\u010a\u0001\u0000\u0000\u0000"+
		"\u010c\u010d\u0001\u0000\u0000\u0000\u010d\'\u0001\u0000\u0000\u0000\u010e"+
		"\u010c\u0001\u0000\u0000\u0000\u010f\u0118\u0005X\u0000\u0000\u0110\u0115"+
		"\u0003\u0006\u0003\u0000\u0111\u0112\u0005R\u0000\u0000\u0112\u0114\u0003"+
		"\u0006\u0003\u0000\u0113\u0111\u0001\u0000\u0000\u0000\u0114\u0117\u0001"+
		"\u0000\u0000\u0000\u0115\u0113\u0001\u0000\u0000\u0000\u0115\u0116\u0001"+
		"\u0000\u0000\u0000\u0116\u0119\u0001\u0000\u0000\u0000\u0117\u0115\u0001"+
		"\u0000\u0000\u0000\u0118\u0110\u0001\u0000\u0000\u0000\u0118\u0119\u0001"+
		"\u0000\u0000\u0000\u0119\u011a\u0001\u0000\u0000\u0000\u011a\u011b\u0005"+
		"Y\u0000\u0000\u011b)\u0001\u0000\u0000\u0000\u011c\u011d\u0005V\u0000"+
		"\u0000\u011d\u011e\u0003\u0006\u0003\u0000\u011e\u0127\u0005R\u0000\u0000"+
		"\u011f\u0124\u0003\u0006\u0003\u0000\u0120\u0121\u0005R\u0000\u0000\u0121"+
		"\u0123\u0003\u0006\u0003\u0000\u0122\u0120\u0001\u0000\u0000\u0000\u0123"+
		"\u0126\u0001\u0000\u0000\u0000\u0124\u0122\u0001\u0000\u0000\u0000\u0124"+
		"\u0125\u0001\u0000\u0000\u0000\u0125\u0128\u0001\u0000\u0000\u0000\u0126"+
		"\u0124\u0001\u0000\u0000\u0000\u0127\u011f\u0001\u0000\u0000\u0000\u0127"+
		"\u0128\u0001\u0000\u0000\u0000\u0128\u0129\u0001\u0000\u0000\u0000\u0129"+
		"\u012a\u0005W\u0000\u0000\u012a+\u0001\u0000\u0000\u0000\u012b\u012c\u0005"+
		"Z\u0000\u0000\u012c\u012f\u0003\u0006\u0003\u0000\u012d\u012e\u0005R\u0000"+
		"\u0000\u012e\u0130\u0003\u0006\u0003\u0000\u012f\u012d\u0001\u0000\u0000"+
		"\u0000\u0130\u0131\u0001\u0000\u0000\u0000\u0131\u012f\u0001\u0000\u0000"+
		"\u0000\u0131\u0132\u0001\u0000\u0000\u0000\u0132\u0133\u0001\u0000\u0000"+
		"\u0000\u0133\u0134\u0005[\u0000\u0000\u0134-\u0001\u0000\u0000\u0000\u0135"+
		"\u0143\u0005Z\u0000\u0000\u0136\u0137\u0003\u0006\u0003\u0000\u0137\u0138"+
		"\u0005Q\u0000\u0000\u0138\u0140\u0003\u0006\u0003\u0000\u0139\u013a\u0005"+
		"R\u0000\u0000\u013a\u013b\u0003\u0006\u0003\u0000\u013b\u013c\u0005Q\u0000"+
		"\u0000\u013c\u013d\u0003\u0006\u0003\u0000\u013d\u013f\u0001\u0000\u0000"+
		"\u0000\u013e\u0139\u0001\u0000\u0000\u0000\u013f\u0142\u0001\u0000\u0000"+
		"\u0000\u0140\u013e\u0001\u0000\u0000\u0000\u0140\u0141\u0001\u0000\u0000"+
		"\u0000\u0141\u0144\u0001\u0000\u0000\u0000\u0142\u0140\u0001\u0000\u0000"+
		"\u0000\u0143\u0136\u0001\u0000\u0000\u0000\u0143\u0144\u0001\u0000\u0000"+
		"\u0000\u0144\u0145\u0001\u0000\u0000\u0000\u0145\u0146\u0005[\u0000\u0000"+
		"\u0146/\u0001\u0000\u0000\u0000\"9;EORgn\u0081\u0088\u0096\u009f\u00a8"+
		"\u00ac\u00b5\u00b7\u00bf\u00c4\u00cb\u00d2\u00d8\u00dd\u00e6\u00f0\u00fb"+
		"\u0103\u0105\u010c\u0115\u0118\u0124\u0127\u0131\u0140\u0143";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}