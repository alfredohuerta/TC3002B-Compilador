# Generated from patito.g4 by ANTLR 4.13.2
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
        4,1,34,339,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,0,1,0,3,0,
        55,8,0,1,0,5,0,58,8,0,10,0,12,0,61,9,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,78,8,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,5,0,88,8,0,10,0,12,0,91,9,0,1,0,1,0,5,0,95,8,0,10,0,
        12,0,98,9,0,1,0,1,0,1,0,1,0,1,0,5,0,105,8,0,10,0,12,0,108,9,0,1,
        0,3,0,111,8,0,1,1,1,1,1,1,1,2,1,2,1,2,5,2,119,8,2,10,2,12,2,122,
        9,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,130,8,2,10,2,12,2,133,9,2,1,2,1,
        2,1,2,1,2,1,2,3,2,140,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,
        3,167,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,176,8,4,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,3,5,186,8,5,1,6,1,6,1,6,1,6,3,6,192,8,6,1,7,1,
        7,1,7,1,7,1,7,3,7,199,8,7,1,8,1,8,1,9,1,9,1,9,1,9,3,9,207,8,9,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,219,8,10,1,
        11,1,11,1,11,1,11,5,11,225,8,11,10,11,12,11,228,9,11,3,11,230,8,
        11,1,12,1,12,1,12,3,12,235,8,12,1,13,1,13,1,13,1,14,1,14,1,14,1,
        14,1,14,3,14,245,8,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,3,15,257,8,15,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,3,17,273,8,17,1,18,1,18,1,18,5,18,278,
        8,18,10,18,12,18,281,9,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,298,8,19,1,20,1,20,1,20,
        1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,
        315,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,
        1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,337,8,24,1,24,
        0,0,25,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,0,2,1,0,28,29,1,0,32,33,356,0,110,1,0,0,0,2,112,1,0,
        0,0,4,115,1,0,0,0,6,166,1,0,0,0,8,175,1,0,0,0,10,185,1,0,0,0,12,
        191,1,0,0,0,14,198,1,0,0,0,16,200,1,0,0,0,18,206,1,0,0,0,20,218,
        1,0,0,0,22,229,1,0,0,0,24,234,1,0,0,0,26,236,1,0,0,0,28,244,1,0,
        0,0,30,256,1,0,0,0,32,258,1,0,0,0,34,272,1,0,0,0,36,274,1,0,0,0,
        38,297,1,0,0,0,40,299,1,0,0,0,42,314,1,0,0,0,44,316,1,0,0,0,46,324,
        1,0,0,0,48,336,1,0,0,0,50,51,5,22,0,0,51,52,5,30,0,0,52,54,5,1,0,
        0,53,55,3,2,1,0,54,53,1,0,0,0,54,55,1,0,0,0,55,59,1,0,0,0,56,58,
        3,6,3,0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,
        60,62,1,0,0,0,61,59,1,0,0,0,62,63,5,18,0,0,63,64,3,10,5,0,64,65,
        5,19,0,0,65,111,1,0,0,0,66,67,5,22,0,0,67,68,5,30,0,0,68,69,5,1,
        0,0,69,70,5,18,0,0,70,71,3,10,5,0,71,72,5,19,0,0,72,111,1,0,0,0,
        73,74,5,22,0,0,74,75,5,30,0,0,75,77,5,1,0,0,76,78,3,2,1,0,77,76,
        1,0,0,0,77,78,1,0,0,0,78,79,1,0,0,0,79,80,5,18,0,0,80,81,3,10,5,
        0,81,82,5,19,0,0,82,111,1,0,0,0,83,84,5,22,0,0,84,85,5,30,0,0,85,
        89,5,1,0,0,86,88,3,6,3,0,87,86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,
        0,89,90,1,0,0,0,90,92,1,0,0,0,91,89,1,0,0,0,92,96,5,18,0,0,93,95,
        3,10,5,0,94,93,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,
        97,99,1,0,0,0,98,96,1,0,0,0,99,111,5,19,0,0,100,101,5,22,0,0,101,
        102,5,30,0,0,102,106,5,1,0,0,103,105,3,6,3,0,104,103,1,0,0,0,105,
        108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,109,1,0,0,0,108,
        106,1,0,0,0,109,111,3,8,4,0,110,50,1,0,0,0,110,66,1,0,0,0,110,73,
        1,0,0,0,110,83,1,0,0,0,110,100,1,0,0,0,111,1,1,0,0,0,112,113,5,27,
        0,0,113,114,3,4,2,0,114,3,1,0,0,0,115,120,5,30,0,0,116,117,5,2,0,
        0,117,119,5,30,0,0,118,116,1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,
        0,120,121,1,0,0,0,121,123,1,0,0,0,122,120,1,0,0,0,123,124,5,3,0,
        0,124,125,3,16,8,0,125,126,5,1,0,0,126,131,5,30,0,0,127,128,5,2,
        0,0,128,130,5,30,0,0,129,127,1,0,0,0,130,133,1,0,0,0,131,129,1,0,
        0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,131,1,0,0,0,134,135,5,3,
        0,0,135,136,3,16,8,0,136,137,5,1,0,0,137,139,1,0,0,0,138,140,3,4,
        2,0,139,138,1,0,0,0,139,140,1,0,0,0,140,5,1,0,0,0,141,142,5,21,0,
        0,142,143,5,30,0,0,143,144,5,4,0,0,144,145,5,30,0,0,145,146,5,3,
        0,0,146,147,3,16,8,0,147,148,5,5,0,0,148,149,5,6,0,0,149,150,3,2,
        1,0,150,151,3,10,5,0,151,152,5,7,0,0,152,153,5,1,0,0,153,167,1,0,
        0,0,154,155,5,21,0,0,155,156,5,30,0,0,156,157,5,4,0,0,157,158,5,
        30,0,0,158,159,5,3,0,0,159,160,3,16,8,0,160,161,5,5,0,0,161,162,
        5,6,0,0,162,163,3,10,5,0,163,164,5,7,0,0,164,165,5,1,0,0,165,167,
        1,0,0,0,166,141,1,0,0,0,166,154,1,0,0,0,167,7,1,0,0,0,168,169,3,
        6,3,0,169,170,3,8,4,0,170,176,1,0,0,0,171,172,5,18,0,0,172,173,3,
        10,5,0,173,174,5,19,0,0,174,176,1,0,0,0,175,168,1,0,0,0,175,171,
        1,0,0,0,176,9,1,0,0,0,177,178,5,6,0,0,178,179,3,14,7,0,179,180,5,
        7,0,0,180,186,1,0,0,0,181,182,5,6,0,0,182,183,3,12,6,0,183,184,5,
        7,0,0,184,186,1,0,0,0,185,177,1,0,0,0,185,181,1,0,0,0,186,11,1,0,
        0,0,187,188,3,14,7,0,188,189,3,12,6,0,189,192,1,0,0,0,190,192,3,
        14,7,0,191,187,1,0,0,0,191,190,1,0,0,0,192,13,1,0,0,0,193,199,3,
        46,23,0,194,199,3,38,19,0,195,199,3,44,22,0,196,199,3,34,17,0,197,
        199,3,40,20,0,198,193,1,0,0,0,198,194,1,0,0,0,198,195,1,0,0,0,198,
        196,1,0,0,0,198,197,1,0,0,0,199,15,1,0,0,0,200,201,7,0,0,0,201,17,
        1,0,0,0,202,207,3,22,11,0,203,204,3,20,10,0,204,205,3,22,11,0,205,
        207,1,0,0,0,206,202,1,0,0,0,206,203,1,0,0,0,207,19,1,0,0,0,208,209,
        5,8,0,0,209,219,3,22,11,0,210,211,5,9,0,0,211,219,3,22,11,0,212,
        213,5,10,0,0,213,219,3,22,11,0,214,215,5,11,0,0,215,219,3,22,11,
        0,216,217,5,12,0,0,217,219,3,22,11,0,218,208,1,0,0,0,218,210,1,0,
        0,0,218,212,1,0,0,0,218,214,1,0,0,0,218,216,1,0,0,0,219,21,1,0,0,
        0,220,230,3,26,13,0,221,222,3,26,13,0,222,223,3,24,12,0,223,225,
        1,0,0,0,224,221,1,0,0,0,225,228,1,0,0,0,226,224,1,0,0,0,226,227,
        1,0,0,0,227,230,1,0,0,0,228,226,1,0,0,0,229,220,1,0,0,0,229,226,
        1,0,0,0,230,23,1,0,0,0,231,235,5,13,0,0,232,235,5,14,0,0,233,235,
        1,0,0,0,234,231,1,0,0,0,234,232,1,0,0,0,234,233,1,0,0,0,235,25,1,
        0,0,0,236,237,3,30,15,0,237,238,3,28,14,0,238,27,1,0,0,0,239,240,
        5,15,0,0,240,245,3,30,15,0,241,242,5,16,0,0,242,245,3,30,15,0,243,
        245,1,0,0,0,244,239,1,0,0,0,244,241,1,0,0,0,244,243,1,0,0,0,245,
        29,1,0,0,0,246,247,5,4,0,0,247,248,3,18,9,0,248,249,5,5,0,0,249,
        257,1,0,0,0,250,251,5,13,0,0,251,257,5,30,0,0,252,253,5,14,0,0,253,
        257,5,30,0,0,254,257,5,30,0,0,255,257,3,32,16,0,256,246,1,0,0,0,
        256,250,1,0,0,0,256,252,1,0,0,0,256,254,1,0,0,0,256,255,1,0,0,0,
        257,31,1,0,0,0,258,259,7,1,0,0,259,33,1,0,0,0,260,261,5,30,0,0,261,
        262,5,4,0,0,262,263,3,18,9,0,263,264,5,5,0,0,264,265,5,1,0,0,265,
        273,1,0,0,0,266,267,5,30,0,0,267,268,5,4,0,0,268,269,3,36,18,0,269,
        270,5,5,0,0,270,271,5,1,0,0,271,273,1,0,0,0,272,260,1,0,0,0,272,
        266,1,0,0,0,273,35,1,0,0,0,274,279,3,18,9,0,275,276,5,2,0,0,276,
        278,3,18,9,0,277,275,1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,0,279,
        280,1,0,0,0,280,37,1,0,0,0,281,279,1,0,0,0,282,283,5,23,0,0,283,
        284,5,4,0,0,284,285,3,18,9,0,285,286,5,5,0,0,286,287,3,10,5,0,287,
        288,5,1,0,0,288,298,1,0,0,0,289,290,5,23,0,0,290,291,5,4,0,0,291,
        292,3,18,9,0,292,293,5,5,0,0,293,294,3,10,5,0,294,295,5,24,0,0,295,
        296,3,10,5,0,296,298,1,0,0,0,297,282,1,0,0,0,297,289,1,0,0,0,298,
        39,1,0,0,0,299,300,5,20,0,0,300,301,5,4,0,0,301,302,3,42,21,0,302,
        303,5,5,0,0,303,304,5,1,0,0,304,41,1,0,0,0,305,315,3,18,9,0,306,
        307,3,18,9,0,307,308,5,2,0,0,308,309,3,42,21,0,309,315,1,0,0,0,310,
        315,5,31,0,0,311,312,5,31,0,0,312,313,5,2,0,0,313,315,3,42,21,0,
        314,305,1,0,0,0,314,306,1,0,0,0,314,310,1,0,0,0,314,311,1,0,0,0,
        315,43,1,0,0,0,316,317,5,25,0,0,317,318,5,4,0,0,318,319,3,18,9,0,
        319,320,5,5,0,0,320,321,5,26,0,0,321,322,3,10,5,0,322,323,5,1,0,
        0,323,45,1,0,0,0,324,325,5,30,0,0,325,326,5,17,0,0,326,327,3,18,
        9,0,327,328,5,1,0,0,328,47,1,0,0,0,329,330,5,2,0,0,330,331,5,30,
        0,0,331,332,5,3,0,0,332,333,3,16,8,0,333,334,3,48,24,0,334,337,1,
        0,0,0,335,337,1,0,0,0,336,329,1,0,0,0,336,335,1,0,0,0,337,49,1,0,
        0,0,27,54,59,77,89,96,106,110,120,131,139,166,175,185,191,198,206,
        218,226,229,234,244,256,272,279,297,314,336
    ]

class patitoParser ( Parser ):

    grammarFileName = "patito.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "':'", "'('", "')'", "'{'", 
                     "'}'", "'>'", "'<'", "'>='", "'<='", "'=='", "'+'", 
                     "'-'", "'*'", "'/'", "'='", "'Inicio'", "'Fin'", "'Escribe'", 
                     "'Nula'", "'Programa'", "'Si'", "'Sino'", "'Mientras'", 
                     "'Haz'", "'Vars'", "'int'", "'float'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INICIO", "FIN", "ESCRIBE", 
                      "NULA", "PROGRAMA", "SI", "SINO", "MIENTRAS", "HAZ", 
                      "VARS", "INT_TOK", "FLOAT_TOK", "ID", "LETRERO", "CTE_ENT", 
                      "CTE_FLOT", "WS" ]

    RULE_programa = 0
    RULE_vars = 1
    RULE_cycle = 2
    RULE_funcs = 3
    RULE_funcsBis = 4
    RULE_cuerpo = 5
    RULE_estatutoBis = 6
    RULE_estatuto = 7
    RULE_tipo = 8
    RULE_expresion = 9
    RULE_bool = 10
    RULE_exp = 11
    RULE_op = 12
    RULE_termino = 13
    RULE_divmult = 14
    RULE_factor = 15
    RULE_cte = 16
    RULE_llamada = 17
    RULE_expresionBis = 18
    RULE_condicion = 19
    RULE_imprime = 20
    RULE_parametros = 21
    RULE_ciclo = 22
    RULE_asigna = 23
    RULE_typeId = 24

    ruleNames =  [ "programa", "vars", "cycle", "funcs", "funcsBis", "cuerpo", 
                   "estatutoBis", "estatuto", "tipo", "expresion", "bool", 
                   "exp", "op", "termino", "divmult", "factor", "cte", "llamada", 
                   "expresionBis", "condicion", "imprime", "parametros", 
                   "ciclo", "asigna", "typeId" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    INICIO=18
    FIN=19
    ESCRIBE=20
    NULA=21
    PROGRAMA=22
    SI=23
    SINO=24
    MIENTRAS=25
    HAZ=26
    VARS=27
    INT_TOK=28
    FLOAT_TOK=29
    ID=30
    LETRERO=31
    CTE_ENT=32
    CTE_FLOT=33
    WS=34

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAMA(self):
            return self.getToken(patitoParser.PROGRAMA, 0)

        def ID(self):
            return self.getToken(patitoParser.ID, 0)

        def INICIO(self):
            return self.getToken(patitoParser.INICIO, 0)

        def cuerpo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.CuerpoContext)
            else:
                return self.getTypedRuleContext(patitoParser.CuerpoContext,i)


        def FIN(self):
            return self.getToken(patitoParser.FIN, 0)

        def vars_(self):
            return self.getTypedRuleContext(patitoParser.VarsContext,0)


        def funcs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.FuncsContext)
            else:
                return self.getTypedRuleContext(patitoParser.FuncsContext,i)


        def funcsBis(self):
            return self.getTypedRuleContext(patitoParser.FuncsBisContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = patitoParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(patitoParser.PROGRAMA)
                self.state = 51
                self.match(patitoParser.ID)
                self.state = 52
                self.match(patitoParser.T__0)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27:
                    self.state = 53
                    self.vars_()


                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==21:
                    self.state = 56
                    self.funcs()
                    self.state = 61
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 62
                self.match(patitoParser.INICIO)
                self.state = 63
                self.cuerpo()
                self.state = 64
                self.match(patitoParser.FIN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(patitoParser.PROGRAMA)
                self.state = 67
                self.match(patitoParser.ID)
                self.state = 68
                self.match(patitoParser.T__0)
                self.state = 69
                self.match(patitoParser.INICIO)
                self.state = 70
                self.cuerpo()
                self.state = 71
                self.match(patitoParser.FIN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.match(patitoParser.PROGRAMA)
                self.state = 74
                self.match(patitoParser.ID)
                self.state = 75
                self.match(patitoParser.T__0)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27:
                    self.state = 76
                    self.vars_()


                self.state = 79
                self.match(patitoParser.INICIO)
                self.state = 80
                self.cuerpo()
                self.state = 81
                self.match(patitoParser.FIN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 83
                self.match(patitoParser.PROGRAMA)
                self.state = 84
                self.match(patitoParser.ID)
                self.state = 85
                self.match(patitoParser.T__0)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==21:
                    self.state = 86
                    self.funcs()
                    self.state = 91
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 92
                self.match(patitoParser.INICIO)
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 93
                    self.cuerpo()
                    self.state = 98
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 99
                self.match(patitoParser.FIN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 100
                self.match(patitoParser.PROGRAMA)
                self.state = 101
                self.match(patitoParser.ID)
                self.state = 102
                self.match(patitoParser.T__0)
                self.state = 106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 103
                        self.funcs() 
                    self.state = 108
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                self.state = 109
                self.funcsBis()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARS(self):
            return self.getToken(patitoParser.VARS, 0)

        def cycle(self):
            return self.getTypedRuleContext(patitoParser.CycleContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)




    def vars_(self):

        localctx = patitoParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(patitoParser.VARS)
            self.state = 113
            self.cycle()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CycleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.ID)
            else:
                return self.getToken(patitoParser.ID, i)

        def tipo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.TipoContext)
            else:
                return self.getTypedRuleContext(patitoParser.TipoContext,i)


        def cycle(self):
            return self.getTypedRuleContext(patitoParser.CycleContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_cycle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCycle" ):
                listener.enterCycle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCycle" ):
                listener.exitCycle(self)




    def cycle(self):

        localctx = patitoParser.CycleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_cycle)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(patitoParser.ID)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 116
                self.match(patitoParser.T__1)
                self.state = 117
                self.match(patitoParser.ID)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
            self.match(patitoParser.T__2)
            self.state = 124
            self.tipo()
            self.state = 125
            self.match(patitoParser.T__0)

            self.state = 126
            self.match(patitoParser.ID)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 127
                self.match(patitoParser.T__1)
                self.state = 128
                self.match(patitoParser.ID)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self.match(patitoParser.T__2)
            self.state = 135
            self.tipo()
            self.state = 136
            self.match(patitoParser.T__0)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 138
                self.cycle()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NULA(self):
            return self.getToken(patitoParser.NULA, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.ID)
            else:
                return self.getToken(patitoParser.ID, i)

        def tipo(self):
            return self.getTypedRuleContext(patitoParser.TipoContext,0)


        def vars_(self):
            return self.getTypedRuleContext(patitoParser.VarsContext,0)


        def cuerpo(self):
            return self.getTypedRuleContext(patitoParser.CuerpoContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_funcs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs" ):
                listener.enterFuncs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs" ):
                listener.exitFuncs(self)




    def funcs(self):

        localctx = patitoParser.FuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcs)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(patitoParser.NULA)
                self.state = 142
                self.match(patitoParser.ID)
                self.state = 143
                self.match(patitoParser.T__3)
                self.state = 144
                self.match(patitoParser.ID)
                self.state = 145
                self.match(patitoParser.T__2)
                self.state = 146
                self.tipo()
                self.state = 147
                self.match(patitoParser.T__4)
                self.state = 148
                self.match(patitoParser.T__5)
                self.state = 149
                self.vars_()
                self.state = 150
                self.cuerpo()
                self.state = 151
                self.match(patitoParser.T__6)
                self.state = 152
                self.match(patitoParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.match(patitoParser.NULA)
                self.state = 155
                self.match(patitoParser.ID)
                self.state = 156
                self.match(patitoParser.T__3)
                self.state = 157
                self.match(patitoParser.ID)
                self.state = 158
                self.match(patitoParser.T__2)
                self.state = 159
                self.tipo()
                self.state = 160
                self.match(patitoParser.T__4)
                self.state = 161
                self.match(patitoParser.T__5)
                self.state = 162
                self.cuerpo()
                self.state = 163
                self.match(patitoParser.T__6)
                self.state = 164
                self.match(patitoParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncsBisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcs(self):
            return self.getTypedRuleContext(patitoParser.FuncsContext,0)


        def funcsBis(self):
            return self.getTypedRuleContext(patitoParser.FuncsBisContext,0)


        def INICIO(self):
            return self.getToken(patitoParser.INICIO, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(patitoParser.CuerpoContext,0)


        def FIN(self):
            return self.getToken(patitoParser.FIN, 0)

        def getRuleIndex(self):
            return patitoParser.RULE_funcsBis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncsBis" ):
                listener.enterFuncsBis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncsBis" ):
                listener.exitFuncsBis(self)




    def funcsBis(self):

        localctx = patitoParser.FuncsBisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcsBis)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.funcs()
                self.state = 169
                self.funcsBis()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.match(patitoParser.INICIO)
                self.state = 172
                self.cuerpo()
                self.state = 173
                self.match(patitoParser.FIN)
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


    class CuerpoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def estatuto(self):
            return self.getTypedRuleContext(patitoParser.EstatutoContext,0)


        def estatutoBis(self):
            return self.getTypedRuleContext(patitoParser.EstatutoBisContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_cuerpo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCuerpo" ):
                listener.enterCuerpo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCuerpo" ):
                listener.exitCuerpo(self)




    def cuerpo(self):

        localctx = patitoParser.CuerpoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_cuerpo)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(patitoParser.T__5)
                self.state = 178
                self.estatuto()
                self.state = 179
                self.match(patitoParser.T__6)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(patitoParser.T__5)
                self.state = 182
                self.estatutoBis()
                self.state = 183
                self.match(patitoParser.T__6)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EstatutoBisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def estatuto(self):
            return self.getTypedRuleContext(patitoParser.EstatutoContext,0)


        def estatutoBis(self):
            return self.getTypedRuleContext(patitoParser.EstatutoBisContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_estatutoBis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstatutoBis" ):
                listener.enterEstatutoBis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstatutoBis" ):
                listener.exitEstatutoBis(self)




    def estatutoBis(self):

        localctx = patitoParser.EstatutoBisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_estatutoBis)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.estatuto()
                self.state = 188
                self.estatutoBis()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.estatuto()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EstatutoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asigna(self):
            return self.getTypedRuleContext(patitoParser.AsignaContext,0)


        def condicion(self):
            return self.getTypedRuleContext(patitoParser.CondicionContext,0)


        def ciclo(self):
            return self.getTypedRuleContext(patitoParser.CicloContext,0)


        def llamada(self):
            return self.getTypedRuleContext(patitoParser.LlamadaContext,0)


        def imprime(self):
            return self.getTypedRuleContext(patitoParser.ImprimeContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_estatuto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstatuto" ):
                listener.enterEstatuto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstatuto" ):
                listener.exitEstatuto(self)




    def estatuto(self):

        localctx = patitoParser.EstatutoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_estatuto)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.asigna()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.condicion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.ciclo()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 196
                self.llamada()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 197
                self.imprime()
                pass


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

        def INT_TOK(self):
            return self.getToken(patitoParser.INT_TOK, 0)

        def FLOAT_TOK(self):
            return self.getToken(patitoParser.FLOAT_TOK, 0)

        def getRuleIndex(self):
            return patitoParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = patitoParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
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


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(patitoParser.ExpContext,0)


        def bool_(self):
            return self.getTypedRuleContext(patitoParser.BoolContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = patitoParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expresion)
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 4, 5, 13, 14, 30, 32, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.exp()
                pass
            elif token in [8, 9, 10, 11, 12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.bool_()
                self.state = 204
                self.exp()
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


    class BoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(patitoParser.ExpContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)




    def bool_(self):

        localctx = patitoParser.BoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_bool)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(patitoParser.T__7)
                self.state = 209
                self.exp()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.match(patitoParser.T__8)
                self.state = 211
                self.exp()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 212
                self.match(patitoParser.T__9)
                self.state = 213
                self.exp()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 214
                self.match(patitoParser.T__10)
                self.state = 215
                self.exp()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 216
                self.match(patitoParser.T__11)
                self.state = 217
                self.exp()
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


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.TerminoContext)
            else:
                return self.getTypedRuleContext(patitoParser.TerminoContext,i)


        def op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.OpContext)
            else:
                return self.getTypedRuleContext(patitoParser.OpContext,i)


        def getRuleIndex(self):
            return patitoParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = patitoParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_exp)
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.termino()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 221
                        self.termino()
                        self.state = 222
                        self.op() 
                    self.state = 228
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return patitoParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)




    def op(self):

        localctx = patitoParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_op)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(patitoParser.T__12)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.match(patitoParser.T__13)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(patitoParser.FactorContext,0)


        def divmult(self):
            return self.getTypedRuleContext(patitoParser.DivmultContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)




    def termino(self):

        localctx = patitoParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_termino)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.factor()
            self.state = 237
            self.divmult()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DivmultContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(patitoParser.FactorContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_divmult

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivmult" ):
                listener.enterDivmult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivmult" ):
                listener.exitDivmult(self)




    def divmult(self):

        localctx = patitoParser.DivmultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_divmult)
        try:
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(patitoParser.T__14)
                self.state = 240
                self.factor()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.match(patitoParser.T__15)
                self.state = 242
                self.factor()
                pass
            elif token in [1, 2, 4, 5, 13, 14, 30, 32, 33]:
                self.enterOuterAlt(localctx, 3)

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


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(patitoParser.ExpresionContext,0)


        def ID(self):
            return self.getToken(patitoParser.ID, 0)

        def cte(self):
            return self.getTypedRuleContext(patitoParser.CteContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = patitoParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_factor)
        try:
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(patitoParser.T__3)
                self.state = 247
                self.expresion()
                self.state = 248
                self.match(patitoParser.T__4)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.match(patitoParser.T__12)
                self.state = 251
                self.match(patitoParser.ID)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.match(patitoParser.T__13)
                self.state = 253
                self.match(patitoParser.ID)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 4)
                self.state = 254
                self.match(patitoParser.ID)
                pass
            elif token in [32, 33]:
                self.enterOuterAlt(localctx, 5)
                self.state = 255
                self.cte()
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


    class CteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CTE_ENT(self):
            return self.getToken(patitoParser.CTE_ENT, 0)

        def CTE_FLOT(self):
            return self.getToken(patitoParser.CTE_FLOT, 0)

        def getRuleIndex(self):
            return patitoParser.RULE_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCte" ):
                listener.enterCte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCte" ):
                listener.exitCte(self)




    def cte(self):

        localctx = patitoParser.CteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_cte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            _la = self._input.LA(1)
            if not(_la==32 or _la==33):
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


    class LlamadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(patitoParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(patitoParser.ExpresionContext,0)


        def expresionBis(self):
            return self.getTypedRuleContext(patitoParser.ExpresionBisContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_llamada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada" ):
                listener.enterLlamada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada" ):
                listener.exitLlamada(self)




    def llamada(self):

        localctx = patitoParser.LlamadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_llamada)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(patitoParser.ID)
                self.state = 261
                self.match(patitoParser.T__3)
                self.state = 262
                self.expresion()
                self.state = 263
                self.match(patitoParser.T__4)
                self.state = 264
                self.match(patitoParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.match(patitoParser.ID)
                self.state = 267
                self.match(patitoParser.T__3)
                self.state = 268
                self.expresionBis()
                self.state = 269
                self.match(patitoParser.T__4)
                self.state = 270
                self.match(patitoParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionBisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(patitoParser.ExpresionContext,i)


        def getRuleIndex(self):
            return patitoParser.RULE_expresionBis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionBis" ):
                listener.enterExpresionBis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionBis" ):
                listener.exitExpresionBis(self)




    def expresionBis(self):

        localctx = patitoParser.ExpresionBisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expresionBis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.expresion()
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 275
                self.match(patitoParser.T__1)
                self.state = 276
                self.expresion()
                self.state = 281
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(patitoParser.SI, 0)

        def expresion(self):
            return self.getTypedRuleContext(patitoParser.ExpresionContext,0)


        def cuerpo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.CuerpoContext)
            else:
                return self.getTypedRuleContext(patitoParser.CuerpoContext,i)


        def SINO(self):
            return self.getToken(patitoParser.SINO, 0)

        def getRuleIndex(self):
            return patitoParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)




    def condicion(self):

        localctx = patitoParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_condicion)
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.match(patitoParser.SI)
                self.state = 283
                self.match(patitoParser.T__3)
                self.state = 284
                self.expresion()
                self.state = 285
                self.match(patitoParser.T__4)
                self.state = 286
                self.cuerpo()
                self.state = 287
                self.match(patitoParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self.match(patitoParser.SI)
                self.state = 290
                self.match(patitoParser.T__3)
                self.state = 291
                self.expresion()
                self.state = 292
                self.match(patitoParser.T__4)
                self.state = 293
                self.cuerpo()
                self.state = 294
                self.match(patitoParser.SINO)
                self.state = 295
                self.cuerpo()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESCRIBE(self):
            return self.getToken(patitoParser.ESCRIBE, 0)

        def parametros(self):
            return self.getTypedRuleContext(patitoParser.ParametrosContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_imprime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImprime" ):
                listener.enterImprime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImprime" ):
                listener.exitImprime(self)




    def imprime(self):

        localctx = patitoParser.ImprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_imprime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(patitoParser.ESCRIBE)
            self.state = 300
            self.match(patitoParser.T__3)
            self.state = 301
            self.parametros()
            self.state = 302
            self.match(patitoParser.T__4)
            self.state = 303
            self.match(patitoParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(patitoParser.ExpresionContext,0)


        def parametros(self):
            return self.getTypedRuleContext(patitoParser.ParametrosContext,0)


        def LETRERO(self):
            return self.getToken(patitoParser.LETRERO, 0)

        def getRuleIndex(self):
            return patitoParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)




    def parametros(self):

        localctx = patitoParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_parametros)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.expresion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.expresion()
                self.state = 307
                self.match(patitoParser.T__1)
                self.state = 308
                self.parametros()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 310
                self.match(patitoParser.LETRERO)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 311
                self.match(patitoParser.LETRERO)
                self.state = 312
                self.match(patitoParser.T__1)
                self.state = 313
                self.parametros()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CicloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(patitoParser.MIENTRAS, 0)

        def expresion(self):
            return self.getTypedRuleContext(patitoParser.ExpresionContext,0)


        def HAZ(self):
            return self.getToken(patitoParser.HAZ, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(patitoParser.CuerpoContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_ciclo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCiclo" ):
                listener.enterCiclo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCiclo" ):
                listener.exitCiclo(self)




    def ciclo(self):

        localctx = patitoParser.CicloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_ciclo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(patitoParser.MIENTRAS)
            self.state = 317
            self.match(patitoParser.T__3)
            self.state = 318
            self.expresion()
            self.state = 319
            self.match(patitoParser.T__4)
            self.state = 320
            self.match(patitoParser.HAZ)
            self.state = 321
            self.cuerpo()
            self.state = 322
            self.match(patitoParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(patitoParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(patitoParser.ExpresionContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_asigna

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsigna" ):
                listener.enterAsigna(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsigna" ):
                listener.exitAsigna(self)




    def asigna(self):

        localctx = patitoParser.AsignaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_asigna)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(patitoParser.ID)
            self.state = 325
            self.match(patitoParser.T__16)
            self.state = 326
            self.expresion()
            self.state = 327
            self.match(patitoParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeIdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(patitoParser.ID, 0)

        def tipo(self):
            return self.getTypedRuleContext(patitoParser.TipoContext,0)


        def typeId(self):
            return self.getTypedRuleContext(patitoParser.TypeIdContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_typeId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeId" ):
                listener.enterTypeId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeId" ):
                listener.exitTypeId(self)




    def typeId(self):

        localctx = patitoParser.TypeIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_typeId)
        try:
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.match(patitoParser.T__1)
                self.state = 330
                self.match(patitoParser.ID)
                self.state = 331
                self.match(patitoParser.T__2)
                self.state = 332
                self.tipo()
                self.state = 333
                self.typeId()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





