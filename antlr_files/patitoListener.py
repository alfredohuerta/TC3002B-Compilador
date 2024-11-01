# Generated from patito.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .patitoParser import patitoParser
else:
    from patitoParser import patitoParser

# This class defines a complete listener for a parse tree produced by patitoParser.
class patitoListener(ParseTreeListener):

    # Enter a parse tree produced by patitoParser#programa.
    def enterPrograma(self, ctx:patitoParser.ProgramaContext):
        pass

    # Exit a parse tree produced by patitoParser#programa.
    def exitPrograma(self, ctx:patitoParser.ProgramaContext):
        pass


    # Enter a parse tree produced by patitoParser#vars.
    def enterVars(self, ctx:patitoParser.VarsContext):
        pass

    # Exit a parse tree produced by patitoParser#vars.
    def exitVars(self, ctx:patitoParser.VarsContext):
        pass


    # Enter a parse tree produced by patitoParser#cycle.
    def enterCycle(self, ctx:patitoParser.CycleContext):
        pass

    # Exit a parse tree produced by patitoParser#cycle.
    def exitCycle(self, ctx:patitoParser.CycleContext):
        pass


    # Enter a parse tree produced by patitoParser#funcs.
    def enterFuncs(self, ctx:patitoParser.FuncsContext):
        pass

    # Exit a parse tree produced by patitoParser#funcs.
    def exitFuncs(self, ctx:patitoParser.FuncsContext):
        pass


    # Enter a parse tree produced by patitoParser#cuerpo.
    def enterCuerpo(self, ctx:patitoParser.CuerpoContext):
        pass

    # Exit a parse tree produced by patitoParser#cuerpo.
    def exitCuerpo(self, ctx:patitoParser.CuerpoContext):
        pass


    # Enter a parse tree produced by patitoParser#programaBis.
    def enterProgramaBis(self, ctx:patitoParser.ProgramaBisContext):
        pass

    # Exit a parse tree produced by patitoParser#programaBis.
    def exitProgramaBis(self, ctx:patitoParser.ProgramaBisContext):
        pass


    # Enter a parse tree produced by patitoParser#estatutoBis.
    def enterEstatutoBis(self, ctx:patitoParser.EstatutoBisContext):
        pass

    # Exit a parse tree produced by patitoParser#estatutoBis.
    def exitEstatutoBis(self, ctx:patitoParser.EstatutoBisContext):
        pass


    # Enter a parse tree produced by patitoParser#estatuto.
    def enterEstatuto(self, ctx:patitoParser.EstatutoContext):
        pass

    # Exit a parse tree produced by patitoParser#estatuto.
    def exitEstatuto(self, ctx:patitoParser.EstatutoContext):
        pass


    # Enter a parse tree produced by patitoParser#tipo.
    def enterTipo(self, ctx:patitoParser.TipoContext):
        pass

    # Exit a parse tree produced by patitoParser#tipo.
    def exitTipo(self, ctx:patitoParser.TipoContext):
        pass


    # Enter a parse tree produced by patitoParser#expresion.
    def enterExpresion(self, ctx:patitoParser.ExpresionContext):
        pass

    # Exit a parse tree produced by patitoParser#expresion.
    def exitExpresion(self, ctx:patitoParser.ExpresionContext):
        pass


    # Enter a parse tree produced by patitoParser#bool.
    def enterBool(self, ctx:patitoParser.BoolContext):
        pass

    # Exit a parse tree produced by patitoParser#bool.
    def exitBool(self, ctx:patitoParser.BoolContext):
        pass


    # Enter a parse tree produced by patitoParser#exp.
    def enterExp(self, ctx:patitoParser.ExpContext):
        pass

    # Exit a parse tree produced by patitoParser#exp.
    def exitExp(self, ctx:patitoParser.ExpContext):
        pass


    # Enter a parse tree produced by patitoParser#op.
    def enterOp(self, ctx:patitoParser.OpContext):
        pass

    # Exit a parse tree produced by patitoParser#op.
    def exitOp(self, ctx:patitoParser.OpContext):
        pass


    # Enter a parse tree produced by patitoParser#termino.
    def enterTermino(self, ctx:patitoParser.TerminoContext):
        pass

    # Exit a parse tree produced by patitoParser#termino.
    def exitTermino(self, ctx:patitoParser.TerminoContext):
        pass


    # Enter a parse tree produced by patitoParser#divmult.
    def enterDivmult(self, ctx:patitoParser.DivmultContext):
        pass

    # Exit a parse tree produced by patitoParser#divmult.
    def exitDivmult(self, ctx:patitoParser.DivmultContext):
        pass


    # Enter a parse tree produced by patitoParser#factor.
    def enterFactor(self, ctx:patitoParser.FactorContext):
        pass

    # Exit a parse tree produced by patitoParser#factor.
    def exitFactor(self, ctx:patitoParser.FactorContext):
        pass


    # Enter a parse tree produced by patitoParser#cte.
    def enterCte(self, ctx:patitoParser.CteContext):
        pass

    # Exit a parse tree produced by patitoParser#cte.
    def exitCte(self, ctx:patitoParser.CteContext):
        pass


    # Enter a parse tree produced by patitoParser#llamada.
    def enterLlamada(self, ctx:patitoParser.LlamadaContext):
        pass

    # Exit a parse tree produced by patitoParser#llamada.
    def exitLlamada(self, ctx:patitoParser.LlamadaContext):
        pass


    # Enter a parse tree produced by patitoParser#expresionBis.
    def enterExpresionBis(self, ctx:patitoParser.ExpresionBisContext):
        pass

    # Exit a parse tree produced by patitoParser#expresionBis.
    def exitExpresionBis(self, ctx:patitoParser.ExpresionBisContext):
        pass


    # Enter a parse tree produced by patitoParser#condicion.
    def enterCondicion(self, ctx:patitoParser.CondicionContext):
        pass

    # Exit a parse tree produced by patitoParser#condicion.
    def exitCondicion(self, ctx:patitoParser.CondicionContext):
        pass


    # Enter a parse tree produced by patitoParser#imprime.
    def enterImprime(self, ctx:patitoParser.ImprimeContext):
        pass

    # Exit a parse tree produced by patitoParser#imprime.
    def exitImprime(self, ctx:patitoParser.ImprimeContext):
        pass


    # Enter a parse tree produced by patitoParser#parametros.
    def enterParametros(self, ctx:patitoParser.ParametrosContext):
        pass

    # Exit a parse tree produced by patitoParser#parametros.
    def exitParametros(self, ctx:patitoParser.ParametrosContext):
        pass


    # Enter a parse tree produced by patitoParser#ciclo.
    def enterCiclo(self, ctx:patitoParser.CicloContext):
        pass

    # Exit a parse tree produced by patitoParser#ciclo.
    def exitCiclo(self, ctx:patitoParser.CicloContext):
        pass


    # Enter a parse tree produced by patitoParser#asigna.
    def enterAsigna(self, ctx:patitoParser.AsignaContext):
        pass

    # Exit a parse tree produced by patitoParser#asigna.
    def exitAsigna(self, ctx:patitoParser.AsignaContext):
        pass


    # Enter a parse tree produced by patitoParser#typeId.
    def enterTypeId(self, ctx:patitoParser.TypeIdContext):
        pass

    # Exit a parse tree produced by patitoParser#typeId.
    def exitTypeId(self, ctx:patitoParser.TypeIdContext):
        pass



del patitoParser