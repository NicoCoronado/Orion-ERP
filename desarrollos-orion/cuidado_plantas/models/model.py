from odoo import models, fields, api
from odoo.exceptions import ValidationError,UserError


class TipodeRiego(models.Model):
    _name="cuidados.tipo_de_riego"

    name = fields.Char(string="Nombre")

    def listar_tipo_de_riego():
        # 
    def ver_detalle_tipo_riego():
        # 


class Sustrato(models.Model):
    _name="cuidados.sustrato"

    name = fields.Char(string="Nombre")

class OperacionDiaria(models.Model):
    _name="cuidados.operacion_diaria"

    name = fields.Char(string="Nombre")

    def asignar jardinero()
        # 
    def listar plantas a cuidar()
        # 
    def listar cuidados por planta()
        # 


class TipodePlanta(models.Model):
    _name="cuidados.tipo_de_planta"

    name = fields.Char(string="Nombre")

    def listar_tipo_de_planta():
        # 
    def crear_tipo_planta():
        # 
    def eliminar_tipo_planta():
        # 
    def ver_detalle_tipo_planta():
        # 
    def actualizar_tipo_planta():

class Planta(models.Model):
    _name="cuidados.planta"

    name = fields.Char(string="Nombre")
    foto_referencia = fields.Binary(string="Foto referencia planta")
    riego_diario = fields.Float(string="Volúmen riego")
    riego_diario_udm = fields.Many2one('product.uom', string="UdM Riego")
    acidez = fields.Float(string="Nivel de acidez")
    acidez_udm = fields.Many2one('product.uom', string="UdM Acidez")
    intensidad_luminica = fields.Float(string="Intensidad lumínica")
    intensidad_luminica_udm = fields.Many2one('product.uom', string="UdM Int. Lumin.")
    plagas = fields.Many2many('cuidados.plaga', string="Plagas peligrosas")
    temperatura = fields.Float(string="Temperatura ideal")
    temperatura_udm = fields.Many2one('product.uom', string="UdM Temp.")
    sustrato = fields.Many2one('cuidados.sustrato', string="Sustrato preferido")
    tipo_de_riego = fields.Many2one('cuidados.tipo_de_riego', string="Tipo de riego")
    tipo_de_planta = fields.Many2one('cuidados.tipo_de_planta')
    tamano_maximo = fields.Float(string="Tamaño máximo")
    tamano_maximo_udm = fields.Many2one('product.uom', string="UdM Tamaño Max.")

    def listar_planta():
        # 
    def crear_planta():
        # 
    def eliminar_planta():
        # 
    def ver_detalle_planta():
        # 
    def actualizar_planta():
        # 
    def tiempo_riego():
        # cada cierto tiempo regar la planta

class Plagas(models.Model):
    _name="cuidados.plaga"

    name = fields.Char(string="Nombre")

    def listar_plaga():
        # 
    def crear_plaga():
        # 
    def ver_detalle_plaga():
        # 
    def eliminar_plaga():
        # 
    def actualizar_plaga():
        # 


class Invernadero(models.Model):
    _name = "cuidados.invernadero"

    nombre = fields.Char(string="Nombre")
    co2 = fields.Float()
    sistemas = fields.Char(string="Nombre")

    def listar_invernadero():
        # 
    def crear_invernadero():
        # 
    def eliminar_invernadero():
        # 
    def ver_detalle_invernadero():
        # 
    def actualizar_invernadero():
        # 


class Macetero(models.Model):
    _name = "cuidados.macetero"

    dimensiones = fields.Float()
    tipo = fields.Char(string="Tipo de macetero")

    def listar_macetero():
        #
    def crear_macetero():
        # 
    def ver_detalle_macetero():
        # 
    def eliminar_macetero():
        # 
    def actualizar_macetero():
        # 

class Plantacion(models.Model):
    _name = "cuidados.plantacion"

    planta = fields.Many2one()
    seccion = fields.Many2one()
    invernadero = fields.Many2one()
    insumos = fields.Many2one()
    metricas = fields.Float()
    foto_referencia = fields.Binary(string="Foto referencia planta")
    
    def crear_plantacion():
        # 
    def eliminar_plantacion():
        # 
    def listar_plantacion():
        # 
    def ver_detalle_plantacion():
        # 
    def actualizar_plantacion():
        # 

class secciones(models.Model):
    _name = 'cuidados.secciones'

    invernadero = Many2one()
    tipo_planta_admitidos = one2Many()
    nombre = fields.Char()

    def crear_seccion():
        # 
    def eliminar_seccion():
        # 
    def listar_seccion():
        # 
    def ver_detalle_seccion():
        # 
    def actualizar_seccion():
        # 

class Insumos(models.Model):
    _name = "cuidados.insumos"

    nombre = fields.Char(string='Nombre')

    def crear_insumos():
        # 
    def eliminar_insumo():
        #
    def listar_insumos():
        #
    def ver_detalle_insumos():
        #
    def actualizar_insumos():
        # 

class Jardineros(models.Model):
    _name = 'cuidados.jardineros'

    nombre = fields.Char(string="nombre")

    def crear_jardinero():
        # 
    def eliminar_jardinero():
        # 
    def listar_jardinero():
        # 
    def ver_detalle_jardinero():
        # 
    def actualizar_jardinero():
        # 

class Maquinaria(models.Model):
    _name = 'cuidados.maquinaria'

    nombre = fields.Char(string='Nombre')

