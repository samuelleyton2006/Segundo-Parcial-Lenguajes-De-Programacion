# Generated from Crud.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CrudParser import CrudParser
else:
    from CrudParser import CrudParser

# This class defines a complete listener for a parse tree produced by CrudParser.
class CrudListener(ParseTreeListener):

    # Enter a parse tree produced by CrudParser#programa.
    def enterPrograma(self, ctx:CrudParser.ProgramaContext):
        pass

    # Exit a parse tree produced by CrudParser#programa.
    def exitPrograma(self, ctx:CrudParser.ProgramaContext):
        pass


    # Enter a parse tree produced by CrudParser#instruccion.
    def enterInstruccion(self, ctx:CrudParser.InstruccionContext):
        pass

    # Exit a parse tree produced by CrudParser#instruccion.
    def exitInstruccion(self, ctx:CrudParser.InstruccionContext):
        pass


    # Enter a parse tree produced by CrudParser#crear_entidad.
    def enterCrear_entidad(self, ctx:CrudParser.Crear_entidadContext):
        pass

    # Exit a parse tree produced by CrudParser#crear_entidad.
    def exitCrear_entidad(self, ctx:CrudParser.Crear_entidadContext):
        pass


    # Enter a parse tree produced by CrudParser#lista_atributos.
    def enterLista_atributos(self, ctx:CrudParser.Lista_atributosContext):
        pass

    # Exit a parse tree produced by CrudParser#lista_atributos.
    def exitLista_atributos(self, ctx:CrudParser.Lista_atributosContext):
        pass


    # Enter a parse tree produced by CrudParser#atributo.
    def enterAtributo(self, ctx:CrudParser.AtributoContext):
        pass

    # Exit a parse tree produced by CrudParser#atributo.
    def exitAtributo(self, ctx:CrudParser.AtributoContext):
        pass


    # Enter a parse tree produced by CrudParser#consultar_entidad.
    def enterConsultar_entidad(self, ctx:CrudParser.Consultar_entidadContext):
        pass

    # Exit a parse tree produced by CrudParser#consultar_entidad.
    def exitConsultar_entidad(self, ctx:CrudParser.Consultar_entidadContext):
        pass


    # Enter a parse tree produced by CrudParser#modificar_entidad.
    def enterModificar_entidad(self, ctx:CrudParser.Modificar_entidadContext):
        pass

    # Exit a parse tree produced by CrudParser#modificar_entidad.
    def exitModificar_entidad(self, ctx:CrudParser.Modificar_entidadContext):
        pass


    # Enter a parse tree produced by CrudParser#lista_modificaciones.
    def enterLista_modificaciones(self, ctx:CrudParser.Lista_modificacionesContext):
        pass

    # Exit a parse tree produced by CrudParser#lista_modificaciones.
    def exitLista_modificaciones(self, ctx:CrudParser.Lista_modificacionesContext):
        pass


    # Enter a parse tree produced by CrudParser#modificacion.
    def enterModificacion(self, ctx:CrudParser.ModificacionContext):
        pass

    # Exit a parse tree produced by CrudParser#modificacion.
    def exitModificacion(self, ctx:CrudParser.ModificacionContext):
        pass


    # Enter a parse tree produced by CrudParser#eliminar_entidad.
    def enterEliminar_entidad(self, ctx:CrudParser.Eliminar_entidadContext):
        pass

    # Exit a parse tree produced by CrudParser#eliminar_entidad.
    def exitEliminar_entidad(self, ctx:CrudParser.Eliminar_entidadContext):
        pass


    # Enter a parse tree produced by CrudParser#expresion_condicion.
    def enterExpresion_condicion(self, ctx:CrudParser.Expresion_condicionContext):
        pass

    # Exit a parse tree produced by CrudParser#expresion_condicion.
    def exitExpresion_condicion(self, ctx:CrudParser.Expresion_condicionContext):
        pass


    # Enter a parse tree produced by CrudParser#operador_comparacion.
    def enterOperador_comparacion(self, ctx:CrudParser.Operador_comparacionContext):
        pass

    # Exit a parse tree produced by CrudParser#operador_comparacion.
    def exitOperador_comparacion(self, ctx:CrudParser.Operador_comparacionContext):
        pass


    # Enter a parse tree produced by CrudParser#valor.
    def enterValor(self, ctx:CrudParser.ValorContext):
        pass

    # Exit a parse tree produced by CrudParser#valor.
    def exitValor(self, ctx:CrudParser.ValorContext):
        pass


    # Enter a parse tree produced by CrudParser#tipo_dato.
    def enterTipo_dato(self, ctx:CrudParser.Tipo_datoContext):
        pass

    # Exit a parse tree produced by CrudParser#tipo_dato.
    def exitTipo_dato(self, ctx:CrudParser.Tipo_datoContext):
        pass


    # Enter a parse tree produced by CrudParser#nombre_entidad.
    def enterNombre_entidad(self, ctx:CrudParser.Nombre_entidadContext):
        pass

    # Exit a parse tree produced by CrudParser#nombre_entidad.
    def exitNombre_entidad(self, ctx:CrudParser.Nombre_entidadContext):
        pass


    # Enter a parse tree produced by CrudParser#nombre_atributo.
    def enterNombre_atributo(self, ctx:CrudParser.Nombre_atributoContext):
        pass

    # Exit a parse tree produced by CrudParser#nombre_atributo.
    def exitNombre_atributo(self, ctx:CrudParser.Nombre_atributoContext):
        pass



del CrudParser