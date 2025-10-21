# Generated from Crud.g4 by ANTLR 4.13.1
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
        4,1,25,116,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,3,1,45,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,
        3,57,8,3,10,3,12,3,60,9,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,70,
        8,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,78,8,6,1,7,1,7,1,7,5,7,83,8,7,10,
        7,12,7,86,9,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,97,8,9,1,10,
        1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,3,12,108,8,12,1,13,1,13,
        1,14,1,14,1,15,1,15,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,0,2,1,0,12,17,1,0,18,21,110,0,35,1,0,0,0,2,44,1,0,0,0,4,
        46,1,0,0,0,6,53,1,0,0,0,8,61,1,0,0,0,10,64,1,0,0,0,12,71,1,0,0,0,
        14,79,1,0,0,0,16,87,1,0,0,0,18,91,1,0,0,0,20,98,1,0,0,0,22,102,1,
        0,0,0,24,107,1,0,0,0,26,109,1,0,0,0,28,111,1,0,0,0,30,113,1,0,0,
        0,32,34,3,2,1,0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,
        1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,38,39,5,0,0,1,39,1,1,0,0,0,40,
        45,3,4,2,0,41,45,3,10,5,0,42,45,3,12,6,0,43,45,3,18,9,0,44,40,1,
        0,0,0,44,41,1,0,0,0,44,42,1,0,0,0,44,43,1,0,0,0,45,3,1,0,0,0,46,
        47,5,1,0,0,47,48,5,2,0,0,48,49,3,28,14,0,49,50,5,3,0,0,50,51,3,6,
        3,0,51,52,5,4,0,0,52,5,1,0,0,0,53,58,3,8,4,0,54,55,5,5,0,0,55,57,
        3,8,4,0,56,54,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,
        59,7,1,0,0,0,60,58,1,0,0,0,61,62,3,30,15,0,62,63,3,26,13,0,63,9,
        1,0,0,0,64,65,5,6,0,0,65,66,5,2,0,0,66,69,3,28,14,0,67,68,5,7,0,
        0,68,70,3,20,10,0,69,67,1,0,0,0,69,70,1,0,0,0,70,11,1,0,0,0,71,72,
        5,8,0,0,72,73,3,28,14,0,73,74,5,9,0,0,74,77,3,14,7,0,75,76,5,7,0,
        0,76,78,3,20,10,0,77,75,1,0,0,0,77,78,1,0,0,0,78,13,1,0,0,0,79,84,
        3,16,8,0,80,81,5,5,0,0,81,83,3,16,8,0,82,80,1,0,0,0,83,86,1,0,0,
        0,84,82,1,0,0,0,84,85,1,0,0,0,85,15,1,0,0,0,86,84,1,0,0,0,87,88,
        3,30,15,0,88,89,5,10,0,0,89,90,3,24,12,0,90,17,1,0,0,0,91,92,5,11,
        0,0,92,93,5,2,0,0,93,96,3,28,14,0,94,95,5,7,0,0,95,97,3,20,10,0,
        96,94,1,0,0,0,96,97,1,0,0,0,97,19,1,0,0,0,98,99,3,30,15,0,99,100,
        3,22,11,0,100,101,3,24,12,0,101,21,1,0,0,0,102,103,7,0,0,0,103,23,
        1,0,0,0,104,108,5,22,0,0,105,108,5,23,0,0,106,108,3,30,15,0,107,
        104,1,0,0,0,107,105,1,0,0,0,107,106,1,0,0,0,108,25,1,0,0,0,109,110,
        7,1,0,0,110,27,1,0,0,0,111,112,5,24,0,0,112,29,1,0,0,0,113,114,5,
        24,0,0,114,31,1,0,0,0,8,35,44,58,69,77,84,96,107
    ]

class CrudParser ( Parser ):

    grammarFileName = "Crud.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'INICIAR'", "'ENTIDAD'", "'('", "')'", 
                     "';'", "'OBTENER'", "'CONDICION'", "'CAMBIAR'", "'CON'", 
                     "'='", "'BORRAR'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'NUMERO'", "'TEXTO'", "'DECIMAL'", "'BOOLEANO'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "TEXTO", "NUMERO", "IDENTIFICADOR", 
                      "WS" ]

    RULE_programa = 0
    RULE_instruccion = 1
    RULE_crear_entidad = 2
    RULE_lista_atributos = 3
    RULE_atributo = 4
    RULE_consultar_entidad = 5
    RULE_modificar_entidad = 6
    RULE_lista_modificaciones = 7
    RULE_modificacion = 8
    RULE_eliminar_entidad = 9
    RULE_expresion_condicion = 10
    RULE_operador_comparacion = 11
    RULE_valor = 12
    RULE_tipo_dato = 13
    RULE_nombre_entidad = 14
    RULE_nombre_atributo = 15

    ruleNames =  [ "programa", "instruccion", "crear_entidad", "lista_atributos", 
                   "atributo", "consultar_entidad", "modificar_entidad", 
                   "lista_modificaciones", "modificacion", "eliminar_entidad", 
                   "expresion_condicion", "operador_comparacion", "valor", 
                   "tipo_dato", "nombre_entidad", "nombre_atributo" ]

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
    T__18=19
    T__19=20
    T__20=21
    TEXTO=22
    NUMERO=23
    IDENTIFICADOR=24
    WS=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CrudParser.EOF, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CrudParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(CrudParser.InstruccionContext,i)


        def getRuleIndex(self):
            return CrudParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = CrudParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2370) != 0):
                self.state = 32
                self.instruccion()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(CrudParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def crear_entidad(self):
            return self.getTypedRuleContext(CrudParser.Crear_entidadContext,0)


        def consultar_entidad(self):
            return self.getTypedRuleContext(CrudParser.Consultar_entidadContext,0)


        def modificar_entidad(self):
            return self.getTypedRuleContext(CrudParser.Modificar_entidadContext,0)


        def eliminar_entidad(self):
            return self.getTypedRuleContext(CrudParser.Eliminar_entidadContext,0)


        def getRuleIndex(self):
            return CrudParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)




    def instruccion(self):

        localctx = CrudParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccion)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.crear_entidad()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.consultar_entidad()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.modificar_entidad()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.eliminar_entidad()
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


    class Crear_entidadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nombre_entidad(self):
            return self.getTypedRuleContext(CrudParser.Nombre_entidadContext,0)


        def lista_atributos(self):
            return self.getTypedRuleContext(CrudParser.Lista_atributosContext,0)


        def getRuleIndex(self):
            return CrudParser.RULE_crear_entidad

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCrear_entidad" ):
                listener.enterCrear_entidad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCrear_entidad" ):
                listener.exitCrear_entidad(self)




    def crear_entidad(self):

        localctx = CrudParser.Crear_entidadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_crear_entidad)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(CrudParser.T__0)
            self.state = 47
            self.match(CrudParser.T__1)
            self.state = 48
            self.nombre_entidad()
            self.state = 49
            self.match(CrudParser.T__2)
            self.state = 50
            self.lista_atributos()
            self.state = 51
            self.match(CrudParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_atributosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atributo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CrudParser.AtributoContext)
            else:
                return self.getTypedRuleContext(CrudParser.AtributoContext,i)


        def getRuleIndex(self):
            return CrudParser.RULE_lista_atributos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_atributos" ):
                listener.enterLista_atributos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_atributos" ):
                listener.exitLista_atributos(self)




    def lista_atributos(self):

        localctx = CrudParser.Lista_atributosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_lista_atributos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.atributo()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 54
                self.match(CrudParser.T__4)
                self.state = 55
                self.atributo()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtributoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nombre_atributo(self):
            return self.getTypedRuleContext(CrudParser.Nombre_atributoContext,0)


        def tipo_dato(self):
            return self.getTypedRuleContext(CrudParser.Tipo_datoContext,0)


        def getRuleIndex(self):
            return CrudParser.RULE_atributo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtributo" ):
                listener.enterAtributo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtributo" ):
                listener.exitAtributo(self)




    def atributo(self):

        localctx = CrudParser.AtributoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atributo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.nombre_atributo()
            self.state = 62
            self.tipo_dato()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Consultar_entidadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nombre_entidad(self):
            return self.getTypedRuleContext(CrudParser.Nombre_entidadContext,0)


        def expresion_condicion(self):
            return self.getTypedRuleContext(CrudParser.Expresion_condicionContext,0)


        def getRuleIndex(self):
            return CrudParser.RULE_consultar_entidad

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConsultar_entidad" ):
                listener.enterConsultar_entidad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConsultar_entidad" ):
                listener.exitConsultar_entidad(self)




    def consultar_entidad(self):

        localctx = CrudParser.Consultar_entidadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_consultar_entidad)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(CrudParser.T__5)
            self.state = 65
            self.match(CrudParser.T__1)
            self.state = 66
            self.nombre_entidad()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 67
                self.match(CrudParser.T__6)
                self.state = 68
                self.expresion_condicion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Modificar_entidadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nombre_entidad(self):
            return self.getTypedRuleContext(CrudParser.Nombre_entidadContext,0)


        def lista_modificaciones(self):
            return self.getTypedRuleContext(CrudParser.Lista_modificacionesContext,0)


        def expresion_condicion(self):
            return self.getTypedRuleContext(CrudParser.Expresion_condicionContext,0)


        def getRuleIndex(self):
            return CrudParser.RULE_modificar_entidad

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModificar_entidad" ):
                listener.enterModificar_entidad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModificar_entidad" ):
                listener.exitModificar_entidad(self)




    def modificar_entidad(self):

        localctx = CrudParser.Modificar_entidadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_modificar_entidad)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(CrudParser.T__7)
            self.state = 72
            self.nombre_entidad()
            self.state = 73
            self.match(CrudParser.T__8)
            self.state = 74
            self.lista_modificaciones()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 75
                self.match(CrudParser.T__6)
                self.state = 76
                self.expresion_condicion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_modificacionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def modificacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CrudParser.ModificacionContext)
            else:
                return self.getTypedRuleContext(CrudParser.ModificacionContext,i)


        def getRuleIndex(self):
            return CrudParser.RULE_lista_modificaciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_modificaciones" ):
                listener.enterLista_modificaciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_modificaciones" ):
                listener.exitLista_modificaciones(self)




    def lista_modificaciones(self):

        localctx = CrudParser.Lista_modificacionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_lista_modificaciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.modificacion()
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 80
                self.match(CrudParser.T__4)
                self.state = 81
                self.modificacion()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModificacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nombre_atributo(self):
            return self.getTypedRuleContext(CrudParser.Nombre_atributoContext,0)


        def valor(self):
            return self.getTypedRuleContext(CrudParser.ValorContext,0)


        def getRuleIndex(self):
            return CrudParser.RULE_modificacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModificacion" ):
                listener.enterModificacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModificacion" ):
                listener.exitModificacion(self)




    def modificacion(self):

        localctx = CrudParser.ModificacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_modificacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.nombre_atributo()
            self.state = 88
            self.match(CrudParser.T__9)
            self.state = 89
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Eliminar_entidadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nombre_entidad(self):
            return self.getTypedRuleContext(CrudParser.Nombre_entidadContext,0)


        def expresion_condicion(self):
            return self.getTypedRuleContext(CrudParser.Expresion_condicionContext,0)


        def getRuleIndex(self):
            return CrudParser.RULE_eliminar_entidad

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEliminar_entidad" ):
                listener.enterEliminar_entidad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEliminar_entidad" ):
                listener.exitEliminar_entidad(self)




    def eliminar_entidad(self):

        localctx = CrudParser.Eliminar_entidadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_eliminar_entidad)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(CrudParser.T__10)
            self.state = 92
            self.match(CrudParser.T__1)
            self.state = 93
            self.nombre_entidad()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 94
                self.match(CrudParser.T__6)
                self.state = 95
                self.expresion_condicion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expresion_condicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nombre_atributo(self):
            return self.getTypedRuleContext(CrudParser.Nombre_atributoContext,0)


        def operador_comparacion(self):
            return self.getTypedRuleContext(CrudParser.Operador_comparacionContext,0)


        def valor(self):
            return self.getTypedRuleContext(CrudParser.ValorContext,0)


        def getRuleIndex(self):
            return CrudParser.RULE_expresion_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion_condicion" ):
                listener.enterExpresion_condicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion_condicion" ):
                listener.exitExpresion_condicion(self)




    def expresion_condicion(self):

        localctx = CrudParser.Expresion_condicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expresion_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.nombre_atributo()
            self.state = 99
            self.operador_comparacion()
            self.state = 100
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operador_comparacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CrudParser.RULE_operador_comparacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperador_comparacion" ):
                listener.enterOperador_comparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperador_comparacion" ):
                listener.exitOperador_comparacion(self)




    def operador_comparacion(self):

        localctx = CrudParser.Operador_comparacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_operador_comparacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
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


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXTO(self):
            return self.getToken(CrudParser.TEXTO, 0)

        def NUMERO(self):
            return self.getToken(CrudParser.NUMERO, 0)

        def nombre_atributo(self):
            return self.getTypedRuleContext(CrudParser.Nombre_atributoContext,0)


        def getRuleIndex(self):
            return CrudParser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor" ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor" ):
                listener.exitValor(self)




    def valor(self):

        localctx = CrudParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_valor)
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(CrudParser.TEXTO)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(CrudParser.NUMERO)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.nombre_atributo()
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


    class Tipo_datoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CrudParser.RULE_tipo_dato

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo_dato" ):
                listener.enterTipo_dato(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo_dato" ):
                listener.exitTipo_dato(self)




    def tipo_dato(self):

        localctx = CrudParser.Tipo_datoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_tipo_dato)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3932160) != 0)):
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


    class Nombre_entidadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(CrudParser.IDENTIFICADOR, 0)

        def getRuleIndex(self):
            return CrudParser.RULE_nombre_entidad

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNombre_entidad" ):
                listener.enterNombre_entidad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNombre_entidad" ):
                listener.exitNombre_entidad(self)




    def nombre_entidad(self):

        localctx = CrudParser.Nombre_entidadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_nombre_entidad)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(CrudParser.IDENTIFICADOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nombre_atributoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICADOR(self):
            return self.getToken(CrudParser.IDENTIFICADOR, 0)

        def getRuleIndex(self):
            return CrudParser.RULE_nombre_atributo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNombre_atributo" ):
                listener.enterNombre_atributo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNombre_atributo" ):
                listener.exitNombre_atributo(self)




    def nombre_atributo(self):

        localctx = CrudParser.Nombre_atributoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_nombre_atributo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(CrudParser.IDENTIFICADOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





