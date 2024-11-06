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
        4,1,35,324,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,1,0,1,
        0,1,0,3,0,57,8,0,1,0,5,0,60,8,0,10,0,12,0,63,9,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,5,0,73,8,0,10,0,12,0,76,9,0,1,0,1,0,1,0,1,0,1,0,
        5,0,83,8,0,10,0,12,0,86,9,0,1,0,1,0,5,0,90,8,0,10,0,12,0,93,9,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,107,8,0,1,0,
        1,0,1,0,1,0,3,0,113,8,0,1,1,1,1,4,1,117,8,1,11,1,12,1,118,1,2,1,
        2,1,2,5,2,124,8,2,10,2,12,2,127,9,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,3,3,158,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,3,4,168,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,177,8,5,1,6,1,6,
        1,6,1,6,3,6,183,8,6,1,7,1,7,1,7,1,7,1,7,3,7,190,8,7,1,8,1,8,1,9,
        1,9,1,9,1,9,3,9,198,8,9,1,10,1,10,1,11,1,11,1,11,1,11,5,11,206,8,
        11,10,11,12,11,209,9,11,3,11,211,8,11,1,12,1,12,1,12,3,12,216,8,
        12,1,13,1,13,1,13,1,13,3,13,222,8,13,1,14,1,14,1,14,1,14,1,14,3,
        14,229,8,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,
        15,241,8,15,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,3,17,257,8,17,1,18,1,18,1,18,5,18,262,8,18,10,
        18,12,18,265,9,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,1,19,1,19,3,19,282,8,19,1,20,1,20,1,20,1,20,1,
        20,1,20,1,21,1,21,1,21,5,21,293,8,21,10,21,12,21,296,9,21,1,22,1,
        22,3,22,300,8,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,
        24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,322,8,
        25,1,25,0,0,26,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,0,3,1,0,29,30,1,0,8,13,1,0,32,33,335,0,112,
        1,0,0,0,2,114,1,0,0,0,4,120,1,0,0,0,6,157,1,0,0,0,8,167,1,0,0,0,
        10,176,1,0,0,0,12,182,1,0,0,0,14,189,1,0,0,0,16,191,1,0,0,0,18,193,
        1,0,0,0,20,199,1,0,0,0,22,210,1,0,0,0,24,215,1,0,0,0,26,221,1,0,
        0,0,28,228,1,0,0,0,30,240,1,0,0,0,32,242,1,0,0,0,34,256,1,0,0,0,
        36,258,1,0,0,0,38,281,1,0,0,0,40,283,1,0,0,0,42,289,1,0,0,0,44,299,
        1,0,0,0,46,301,1,0,0,0,48,309,1,0,0,0,50,321,1,0,0,0,52,53,5,19,
        0,0,53,54,5,31,0,0,54,56,5,1,0,0,55,57,3,2,1,0,56,55,1,0,0,0,56,
        57,1,0,0,0,57,61,1,0,0,0,58,60,3,6,3,0,59,58,1,0,0,0,60,63,1,0,0,
        0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,0,64,65,
        5,22,0,0,65,66,3,8,4,0,66,67,5,23,0,0,67,113,1,0,0,0,68,69,5,19,
        0,0,69,70,5,31,0,0,70,74,5,1,0,0,71,73,3,6,3,0,72,71,1,0,0,0,73,
        76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,77,1,0,0,0,76,74,1,0,0,
        0,77,113,3,10,5,0,78,79,5,19,0,0,79,80,5,31,0,0,80,84,5,1,0,0,81,
        83,3,6,3,0,82,81,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,
        0,85,87,1,0,0,0,86,84,1,0,0,0,87,91,5,22,0,0,88,90,3,8,4,0,89,88,
        1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,
        93,91,1,0,0,0,94,113,5,23,0,0,95,96,5,19,0,0,96,97,5,31,0,0,97,98,
        5,1,0,0,98,99,5,22,0,0,99,100,3,8,4,0,100,101,5,23,0,0,101,113,1,
        0,0,0,102,103,5,19,0,0,103,104,5,31,0,0,104,106,5,1,0,0,105,107,
        3,2,1,0,106,105,1,0,0,0,106,107,1,0,0,0,107,108,1,0,0,0,108,109,
        5,22,0,0,109,110,3,8,4,0,110,111,5,23,0,0,111,113,1,0,0,0,112,52,
        1,0,0,0,112,68,1,0,0,0,112,78,1,0,0,0,112,95,1,0,0,0,112,102,1,0,
        0,0,113,1,1,0,0,0,114,116,5,20,0,0,115,117,3,4,2,0,116,115,1,0,0,
        0,117,118,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,3,1,0,0,0,
        120,125,5,31,0,0,121,122,5,2,0,0,122,124,5,31,0,0,123,121,1,0,0,
        0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,128,1,0,0,
        0,127,125,1,0,0,0,128,129,5,3,0,0,129,130,3,16,8,0,130,131,5,1,0,
        0,131,5,1,0,0,0,132,133,5,21,0,0,133,134,5,31,0,0,134,135,5,4,0,
        0,135,136,5,31,0,0,136,137,5,3,0,0,137,138,3,16,8,0,138,139,5,5,
        0,0,139,140,5,6,0,0,140,141,3,2,1,0,141,142,3,8,4,0,142,143,5,7,
        0,0,143,144,5,1,0,0,144,158,1,0,0,0,145,146,5,21,0,0,146,147,5,31,
        0,0,147,148,5,4,0,0,148,149,5,31,0,0,149,150,5,3,0,0,150,151,3,16,
        8,0,151,152,5,5,0,0,152,153,5,6,0,0,153,154,3,8,4,0,154,155,5,7,
        0,0,155,156,5,1,0,0,156,158,1,0,0,0,157,132,1,0,0,0,157,145,1,0,
        0,0,158,7,1,0,0,0,159,160,5,6,0,0,160,161,3,14,7,0,161,162,5,7,0,
        0,162,168,1,0,0,0,163,164,5,6,0,0,164,165,3,12,6,0,165,166,5,7,0,
        0,166,168,1,0,0,0,167,159,1,0,0,0,167,163,1,0,0,0,168,9,1,0,0,0,
        169,170,3,6,3,0,170,171,3,10,5,0,171,177,1,0,0,0,172,173,5,22,0,
        0,173,174,3,8,4,0,174,175,5,23,0,0,175,177,1,0,0,0,176,169,1,0,0,
        0,176,172,1,0,0,0,177,11,1,0,0,0,178,179,3,14,7,0,179,180,3,12,6,
        0,180,183,1,0,0,0,181,183,3,14,7,0,182,178,1,0,0,0,182,181,1,0,0,
        0,183,13,1,0,0,0,184,190,3,48,24,0,185,190,3,34,17,0,186,190,3,38,
        19,0,187,190,3,46,23,0,188,190,3,40,20,0,189,184,1,0,0,0,189,185,
        1,0,0,0,189,186,1,0,0,0,189,187,1,0,0,0,189,188,1,0,0,0,190,15,1,
        0,0,0,191,192,7,0,0,0,192,17,1,0,0,0,193,197,3,22,11,0,194,195,3,
        20,10,0,195,196,3,22,11,0,196,198,1,0,0,0,197,194,1,0,0,0,197,198,
        1,0,0,0,198,19,1,0,0,0,199,200,7,1,0,0,200,21,1,0,0,0,201,211,3,
        26,13,0,202,203,3,26,13,0,203,204,3,24,12,0,204,206,1,0,0,0,205,
        202,1,0,0,0,206,209,1,0,0,0,207,205,1,0,0,0,207,208,1,0,0,0,208,
        211,1,0,0,0,209,207,1,0,0,0,210,201,1,0,0,0,210,207,1,0,0,0,211,
        23,1,0,0,0,212,216,5,14,0,0,213,216,5,15,0,0,214,216,1,0,0,0,215,
        212,1,0,0,0,215,213,1,0,0,0,215,214,1,0,0,0,216,25,1,0,0,0,217,222,
        3,30,15,0,218,219,3,30,15,0,219,220,3,28,14,0,220,222,1,0,0,0,221,
        217,1,0,0,0,221,218,1,0,0,0,222,27,1,0,0,0,223,224,5,16,0,0,224,
        229,3,30,15,0,225,226,5,17,0,0,226,229,3,30,15,0,227,229,1,0,0,0,
        228,223,1,0,0,0,228,225,1,0,0,0,228,227,1,0,0,0,229,29,1,0,0,0,230,
        231,5,4,0,0,231,232,3,18,9,0,232,233,5,5,0,0,233,241,1,0,0,0,234,
        235,5,14,0,0,235,241,5,31,0,0,236,237,5,15,0,0,237,241,5,31,0,0,
        238,241,5,31,0,0,239,241,3,32,16,0,240,230,1,0,0,0,240,234,1,0,0,
        0,240,236,1,0,0,0,240,238,1,0,0,0,240,239,1,0,0,0,241,31,1,0,0,0,
        242,243,7,2,0,0,243,33,1,0,0,0,244,245,5,31,0,0,245,246,5,4,0,0,
        246,247,3,18,9,0,247,248,5,5,0,0,248,249,5,1,0,0,249,257,1,0,0,0,
        250,251,5,31,0,0,251,252,5,4,0,0,252,253,3,36,18,0,253,254,5,5,0,
        0,254,255,5,1,0,0,255,257,1,0,0,0,256,244,1,0,0,0,256,250,1,0,0,
        0,257,35,1,0,0,0,258,263,3,18,9,0,259,260,5,2,0,0,260,262,3,18,9,
        0,261,259,1,0,0,0,262,265,1,0,0,0,263,261,1,0,0,0,263,264,1,0,0,
        0,264,37,1,0,0,0,265,263,1,0,0,0,266,267,5,27,0,0,267,268,5,4,0,
        0,268,269,3,18,9,0,269,270,5,5,0,0,270,271,3,8,4,0,271,272,5,1,0,
        0,272,282,1,0,0,0,273,274,5,27,0,0,274,275,5,4,0,0,275,276,3,18,
        9,0,276,277,5,5,0,0,277,278,3,8,4,0,278,279,5,28,0,0,279,280,3,8,
        4,0,280,282,1,0,0,0,281,266,1,0,0,0,281,273,1,0,0,0,282,39,1,0,0,
        0,283,284,5,24,0,0,284,285,5,4,0,0,285,286,3,42,21,0,286,287,5,5,
        0,0,287,288,5,1,0,0,288,41,1,0,0,0,289,294,3,44,22,0,290,291,5,2,
        0,0,291,293,3,44,22,0,292,290,1,0,0,0,293,296,1,0,0,0,294,292,1,
        0,0,0,294,295,1,0,0,0,295,43,1,0,0,0,296,294,1,0,0,0,297,300,3,18,
        9,0,298,300,5,34,0,0,299,297,1,0,0,0,299,298,1,0,0,0,300,45,1,0,
        0,0,301,302,5,25,0,0,302,303,5,4,0,0,303,304,3,18,9,0,304,305,5,
        5,0,0,305,306,5,26,0,0,306,307,3,8,4,0,307,308,5,1,0,0,308,47,1,
        0,0,0,309,310,5,31,0,0,310,311,5,18,0,0,311,312,3,18,9,0,312,313,
        5,1,0,0,313,49,1,0,0,0,314,315,5,2,0,0,315,316,5,31,0,0,316,317,
        5,3,0,0,317,318,3,16,8,0,318,319,3,50,25,0,319,322,1,0,0,0,320,322,
        1,0,0,0,321,314,1,0,0,0,321,320,1,0,0,0,322,51,1,0,0,0,27,56,61,
        74,84,91,106,112,118,125,157,167,176,182,189,197,207,210,215,221,
        228,240,256,263,281,294,299,321
    ]

class patitoParser ( Parser ):

    grammarFileName = "patito.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "':'", "'('", "')'", "'{'", 
                     "'}'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", 
                     "'+'", "'-'", "'*'", "'/'", "'='", "'Programa'", "'Vars'", 
                     "'Nula'", "'Inicio'", "'Fin'", "'Escribe'", "'Mientras'", 
                     "'Haz'", "'Si'", "'Sino'", "'int'", "'float'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "PROGRAMA", 
                      "VARS", "NULA", "INICIO", "FIN", "ESCRIBE", "MIENTRAS", 
                      "HAZ", "SI", "SINO", "INT_TOK", "FLOAT_TOK", "ID", 
                      "CTE_FLOT", "CTE_ENT", "LETRERO", "WS" ]

    RULE_programa = 0
    RULE_vars = 1
    RULE_var_decl = 2
    RULE_funcs = 3
    RULE_cuerpo = 4
    RULE_programaBis = 5
    RULE_estatutoBis = 6
    RULE_estatuto = 7
    RULE_tipo = 8
    RULE_expresion = 9
    RULE_relop = 10
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
    RULE_param = 22
    RULE_ciclo = 23
    RULE_asigna = 24
    RULE_typeId = 25

    ruleNames =  [ "programa", "vars", "var_decl", "funcs", "cuerpo", "programaBis", 
                   "estatutoBis", "estatuto", "tipo", "expresion", "relop", 
                   "exp", "op", "termino", "divmult", "factor", "cte", "llamada", 
                   "expresionBis", "condicion", "imprime", "parametros", 
                   "param", "ciclo", "asigna", "typeId" ]

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
    T__17=18
    PROGRAMA=19
    VARS=20
    NULA=21
    INICIO=22
    FIN=23
    ESCRIBE=24
    MIENTRAS=25
    HAZ=26
    SI=27
    SINO=28
    INT_TOK=29
    FLOAT_TOK=30
    ID=31
    CTE_FLOT=32
    CTE_ENT=33
    LETRERO=34
    WS=35

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


        def programaBis(self):
            return self.getTypedRuleContext(patitoParser.ProgramaBisContext,0)


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
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(patitoParser.PROGRAMA)
                self.state = 53
                self.match(patitoParser.ID)
                self.state = 54
                self.match(patitoParser.T__0)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 55
                    self.vars_()


                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==21:
                    self.state = 58
                    self.funcs()
                    self.state = 63
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 64
                self.match(patitoParser.INICIO)
                self.state = 65
                self.cuerpo()
                self.state = 66
                self.match(patitoParser.FIN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.match(patitoParser.PROGRAMA)
                self.state = 69
                self.match(patitoParser.ID)
                self.state = 70
                self.match(patitoParser.T__0)
                self.state = 74
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 71
                        self.funcs() 
                    self.state = 76
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 77
                self.programaBis()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.match(patitoParser.PROGRAMA)
                self.state = 79
                self.match(patitoParser.ID)
                self.state = 80
                self.match(patitoParser.T__0)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==21:
                    self.state = 81
                    self.funcs()
                    self.state = 86
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 87
                self.match(patitoParser.INICIO)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 88
                    self.cuerpo()
                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 94
                self.match(patitoParser.FIN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 95
                self.match(patitoParser.PROGRAMA)
                self.state = 96
                self.match(patitoParser.ID)
                self.state = 97
                self.match(patitoParser.T__0)
                self.state = 98
                self.match(patitoParser.INICIO)
                self.state = 99
                self.cuerpo()
                self.state = 100
                self.match(patitoParser.FIN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 102
                self.match(patitoParser.PROGRAMA)
                self.state = 103
                self.match(patitoParser.ID)
                self.state = 104
                self.match(patitoParser.T__0)
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 105
                    self.vars_()


                self.state = 108
                self.match(patitoParser.INICIO)
                self.state = 109
                self.cuerpo()
                self.state = 110
                self.match(patitoParser.FIN)
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

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.Var_declContext)
            else:
                return self.getTypedRuleContext(patitoParser.Var_declContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(patitoParser.VARS)
            self.state = 116 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 115
                self.var_decl()
                self.state = 118 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(patitoParser.ID)
            else:
                return self.getToken(patitoParser.ID, i)

        def tipo(self):
            return self.getTypedRuleContext(patitoParser.TipoContext,0)


        def getRuleIndex(self):
            return patitoParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)




    def var_decl(self):

        localctx = patitoParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(patitoParser.ID)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 121
                self.match(patitoParser.T__1)
                self.state = 122
                self.match(patitoParser.ID)
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
            self.match(patitoParser.T__2)
            self.state = 129
            self.tipo()
            self.state = 130
            self.match(patitoParser.T__0)
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
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(patitoParser.NULA)
                self.state = 133
                self.match(patitoParser.ID)
                self.state = 134
                self.match(patitoParser.T__3)
                self.state = 135
                self.match(patitoParser.ID)
                self.state = 136
                self.match(patitoParser.T__2)
                self.state = 137
                self.tipo()
                self.state = 138
                self.match(patitoParser.T__4)
                self.state = 139
                self.match(patitoParser.T__5)
                self.state = 140
                self.vars_()
                self.state = 141
                self.cuerpo()
                self.state = 142
                self.match(patitoParser.T__6)
                self.state = 143
                self.match(patitoParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.match(patitoParser.NULA)
                self.state = 146
                self.match(patitoParser.ID)
                self.state = 147
                self.match(patitoParser.T__3)
                self.state = 148
                self.match(patitoParser.ID)
                self.state = 149
                self.match(patitoParser.T__2)
                self.state = 150
                self.tipo()
                self.state = 151
                self.match(patitoParser.T__4)
                self.state = 152
                self.match(patitoParser.T__5)
                self.state = 153
                self.cuerpo()
                self.state = 154
                self.match(patitoParser.T__6)
                self.state = 155
                self.match(patitoParser.T__0)
                pass


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
        self.enterRule(localctx, 8, self.RULE_cuerpo)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(patitoParser.T__5)
                self.state = 160
                self.estatuto()
                self.state = 161
                self.match(patitoParser.T__6)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(patitoParser.T__5)
                self.state = 164
                self.estatutoBis()
                self.state = 165
                self.match(patitoParser.T__6)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramaBisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcs(self):
            return self.getTypedRuleContext(patitoParser.FuncsContext,0)


        def programaBis(self):
            return self.getTypedRuleContext(patitoParser.ProgramaBisContext,0)


        def INICIO(self):
            return self.getToken(patitoParser.INICIO, 0)

        def cuerpo(self):
            return self.getTypedRuleContext(patitoParser.CuerpoContext,0)


        def FIN(self):
            return self.getToken(patitoParser.FIN, 0)

        def getRuleIndex(self):
            return patitoParser.RULE_programaBis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgramaBis" ):
                listener.enterProgramaBis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgramaBis" ):
                listener.exitProgramaBis(self)




    def programaBis(self):

        localctx = patitoParser.ProgramaBisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_programaBis)
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.funcs()
                self.state = 170
                self.programaBis()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(patitoParser.INICIO)
                self.state = 173
                self.cuerpo()
                self.state = 174
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
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.estatuto()
                self.state = 179
                self.estatutoBis()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
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


        def llamada(self):
            return self.getTypedRuleContext(patitoParser.LlamadaContext,0)


        def condicion(self):
            return self.getTypedRuleContext(patitoParser.CondicionContext,0)


        def ciclo(self):
            return self.getTypedRuleContext(patitoParser.CicloContext,0)


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
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.asigna()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.llamada()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 186
                self.condicion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 187
                self.ciclo()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 188
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
            self.state = 191
            _la = self._input.LA(1)
            if not(_la==29 or _la==30):
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

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.ExpContext)
            else:
                return self.getTypedRuleContext(patitoParser.ExpContext,i)


        def relop(self):
            return self.getTypedRuleContext(patitoParser.RelopContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.exp()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0):
                self.state = 194
                self.relop()
                self.state = 195
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return patitoParser.RULE_relop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelop" ):
                listener.enterRelop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelop" ):
                listener.exitRelop(self)




    def relop(self):

        localctx = patitoParser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
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
        self._la = 0 # Token type
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.termino()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15032434704) != 0):
                    self.state = 202
                    self.termino()
                    self.state = 203
                    self.op()
                    self.state = 209
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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
            self.state = 215
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.match(patitoParser.T__13)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.match(patitoParser.T__14)
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
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.factor()
                self.state = 219
                self.divmult()
                pass


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
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.match(patitoParser.T__15)
                self.state = 224
                self.factor()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.match(patitoParser.T__16)
                self.state = 226
                self.factor()
                pass
            elif token in [1, 2, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 31, 32, 33]:
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
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(patitoParser.T__3)
                self.state = 231
                self.expresion()
                self.state = 232
                self.match(patitoParser.T__4)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(patitoParser.T__13)
                self.state = 235
                self.match(patitoParser.ID)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 236
                self.match(patitoParser.T__14)
                self.state = 237
                self.match(patitoParser.ID)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 4)
                self.state = 238
                self.match(patitoParser.ID)
                pass
            elif token in [32, 33]:
                self.enterOuterAlt(localctx, 5)
                self.state = 239
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
            self.state = 242
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
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.match(patitoParser.ID)
                self.state = 245
                self.match(patitoParser.T__3)
                self.state = 246
                self.expresion()
                self.state = 247
                self.match(patitoParser.T__4)
                self.state = 248
                self.match(patitoParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.match(patitoParser.ID)
                self.state = 251
                self.match(patitoParser.T__3)
                self.state = 252
                self.expresionBis()
                self.state = 253
                self.match(patitoParser.T__4)
                self.state = 254
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
            self.state = 258
            self.expresion()
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 259
                self.match(patitoParser.T__1)
                self.state = 260
                self.expresion()
                self.state = 265
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
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(patitoParser.SI)
                self.state = 267
                self.match(patitoParser.T__3)
                self.state = 268
                self.expresion()
                self.state = 269
                self.match(patitoParser.T__4)
                self.state = 270
                self.cuerpo()
                self.state = 271
                self.match(patitoParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.match(patitoParser.SI)
                self.state = 274
                self.match(patitoParser.T__3)
                self.state = 275
                self.expresion()
                self.state = 276
                self.match(patitoParser.T__4)
                self.state = 277
                self.cuerpo()
                self.state = 278
                self.match(patitoParser.SINO)
                self.state = 279
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
            self.state = 283
            self.match(patitoParser.ESCRIBE)
            self.state = 284
            self.match(patitoParser.T__3)
            self.state = 285
            self.parametros()
            self.state = 286
            self.match(patitoParser.T__4)
            self.state = 287
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

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(patitoParser.ParamContext)
            else:
                return self.getTypedRuleContext(patitoParser.ParamContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.param()
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 290
                self.match(patitoParser.T__1)
                self.state = 291
                self.param()
                self.state = 296
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

        def expresion(self):
            return self.getTypedRuleContext(patitoParser.ExpresionContext,0)


        def LETRERO(self):
            return self.getToken(patitoParser.LETRERO, 0)

        def getRuleIndex(self):
            return patitoParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = patitoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_param)
        try:
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 31, 32, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.expresion()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.match(patitoParser.LETRERO)
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
        self.enterRule(localctx, 46, self.RULE_ciclo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(patitoParser.MIENTRAS)
            self.state = 302
            self.match(patitoParser.T__3)
            self.state = 303
            self.expresion()
            self.state = 304
            self.match(patitoParser.T__4)
            self.state = 305
            self.match(patitoParser.HAZ)
            self.state = 306
            self.cuerpo()
            self.state = 307
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
        self.enterRule(localctx, 48, self.RULE_asigna)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(patitoParser.ID)
            self.state = 310
            self.match(patitoParser.T__17)
            self.state = 311
            self.expresion()
            self.state = 312
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
        self.enterRule(localctx, 50, self.RULE_typeId)
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.match(patitoParser.T__1)
                self.state = 315
                self.match(patitoParser.ID)
                self.state = 316
                self.match(patitoParser.T__2)
                self.state = 317
                self.tipo()
                self.state = 318
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





