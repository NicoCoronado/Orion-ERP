from odoo import models, fields, api
from odoo.exceptions import ValidationError,UserError

class OperacionDiaria(models.Model):
    _name = "cuidados.operacion_diaria"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nombre")
    fecha = fields.Datetime(string="Fecha asignación")
    state = fields.Selection([('pendiente', 'Pendiente'),
                              ('proceso', 'Proceso'),
                              ('terminado', 'Terminado'),
                              ('validado', 'Validado')
                             ], string="Estado"
                            )
    instrucciones = fields.One2many('cuidados.operacion_diaria_instruccion', 
                                    "operacion_diaria", 
                                    string="Instrucciones")
    supervisor = fields.Many2one('cuidados.funcionario', string="Funcionario")
    comentarios = fields.Text(string="Comentarios")
    invernadero = fields.Many2one('cuidados.invernadero', string="Invernadero")

class OperacionDiaria_Instruccion(models.Model):
    _name="cuidados.operacion_diaria_instruccion"

    name = fields.Char(string="Nombre")
    operacion_diaria = fields.Many2one('cuidados.operacion_diaria', string="Operación diaria")
    jardinero = fields.Many2one('cuidados.funcionario', string="Jardinero")
    plantacion = fields.Many2one('cuidados.plantacion', string="Plantación")
    acciones = fields.Man2many('cuidados.acciones', string="Acciones")
    fotos = fields.One2many('cuidados.operacion_diaria_instruccion.fotos', string="Foto referencia planta")

class OperacionDiaria_Instruccion_Fotos(models.Model):
    _name="cuidados.operacion_diaria_instruccion.fotos"

    foto = fields.Binary(string="Foto")
    instruccion = fields.Many2one('cuidados.operacion_diaria_instruccion', string="Instruccion")
    plantacion = fields.Many2one('cuidados.plantacion', string="Plantacion")
    planta = fields.Many2one('cuidados.planta', string="Planta")


class AccionesCuidado(models.Model):
    _name = "cuidados.acciones"

    name = fields.Char(string="Nombre")
    descripcion = fields.Char(string="Descripcion")

class Planta(models.Model):
    _name="cuidados.planta"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nombre")
    foto_referencia = fields.Binary(string="Foto referencia planta")
    riego_diario = fields.Float(string="Volúmen riego")
    riego_diario_udm = fields.Many2one('product.uom', string="UdM Riego")
    acidez = fields.Float(string="Nivel de acidez")
    acidez_udm = fields.Many2one('product.uom', string="UdM Acidez")
    intensidad_luminica = fields.Float(string="Intensidad lumínica")
    intensidad_luminica_udm = fields.Many2one('product.uom', string="UdM Int. Lumin.")
    plagas = fields.Many2many('cuidados.plaga', string="Plagas peligrosas")
    temperatura = fields.Float(string="Temperatura")
    temperatura_udm = fields.Many2one('product.uom', string="UdM Temp.")
    sustrato = fields.Many2one('cuidados.sustrato', string="Sustrato preferido")
    tipo_de_riego = fields.Many2one('cuidados.tipo_de_riego', string="Tipo de riego")
    tipo_de_planta = fields.Many2one('cuidados.tipo_de_planta')
    tamano_maximo = fields.Float(string="Tamaño máximo")
    tamano_maximo_udm = fields.Many2one('product.uom', string="UdM Tamaño Max.")

class Plantacion(models.Model):
    _name = "cuidados.plantacion"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    planta = fields.Many2one('cuidados.planta', string="Planta")
    seccion = fields.Many2one('cuidados.seccion', string="Seccion")
    invernadero = fields.Many2one('cuidados.invernadero', string="Invernadero")
    insumos = fields.Many2one('cuidados.insumo', string="Insumos")
    macetero = fields.Many2one('cuidados.macetero', string="Macetero")


    enfermedades = fields.Manymany('cuidados.plantacion.enfermedades', string="Enfermedades")
    plagas = fields.Many2many('cuidados.plaga', string="Plagas")
    agua = fields.Float(string="Nivel de agua")
    riego_diario_udm = fields.Many2one('product.uom', string="Agua")
    acidez = fields.Float(string="Nivel de acidez")
    acidez_udm = fields.Many2one('product.uom', string="UdM Acidez")
    intensidad_luminica = fields.Float(string="Intensidad lumínica")
    intensidad_luminica_udm = fields.Many2one('product.uom', string="UdM Int. Lumin.")
    temperatura = fields.Float(string="Temperatura")
    temperatura_udm = fields.Many2one('product.uom', string="UdM Temp.")
    sustrato = fields.Many2one('cuidados.sustrato', string="Sustrato")
    tipo_de_riego = fields.Many2one('cuidados.tipo_de_riego', string="Tipo de riego")


class TipodeRiego(models.Model):
    _name = "cuidados.tipo_de_riego"

    name = fields.Char(string="Nombre")

class Sustrato(models.Model):
    _name="cuidados.sustrato"

    name = fields.Char(string="Nombre")

class TipodePlanta(models.Model):
    _name="cuidados.tipo_de_planta"

    name = fields.Char(string="Nombre")

class Plagas(models.Model):
    _name="cuidados.plaga"

    name = fields.Char(string="Nombre")

class Invernadero(models.Model):
    _name = "cuidados.invernadero"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    nombre = fields.Char(string="Nombre")
    co2 = fields.Float(string="CO2")
    co2_udm = fields.Many2one('product.uom', string="UdM CO2")
    secciones = fields.One2many('cuidados.seccion', "invernadero", string="Secciones")

class Macetero(models.Model):
    _name = "cuidados.macetero"

    dimensiones = fields.Float()
    tipo = fields.Char(string="Tipo de macetero")

class EnfermedadesPlantas(models.Model):
    _name = "cuidados.plantacion.enfermades"

    name = fields.Char(string="Nombre")

class Secciones(models.Model):
    _name = 'cuidados.seccion'

    name = fields.Char(string="Nombre")
    invernadero = fields.Many2one('cuidados.invernadero', string="Invernadero")
    tipo_planta_admitidos = one2Many()

class Insumos(models.Model):
    _name = "cuidados.insumo"

    nombre = fields.Char(string='Nombre')


class Funcionario(models.Model):
    _name = 'cuidados.funcionario'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    nombre = fields.Char(string="nombre")

    es_jardinero = fields.Boolean(string="Es jardinero")
    es_supervisor = fields.Boolean(string="Es supervisor")


#class Maquinaria(models.Model):
#    _name = 'cuidados.maquinaria'

#    nombre = fields.Char(string='Nombre')
