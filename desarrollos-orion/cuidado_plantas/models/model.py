from odoo import models, fields, api
from odoo.exceptions import ValidationError,UserError


#clase planta
    #atributos planta
        #nombre
        #tipo planta (m2o a tipo_planta)
    #metodos planta


class TipodeRiego(models.Model):
    _name="cuidados.tipo_de_riego"

    name = fields.Char(string="Nombre")

class Sustrato(models.Model):
    _name="cuidados.sustrato"

    name = fields.Char(string="Nombre")

class TipodePlanta(models.Model):
    _name="cuidados.tipo_de_planta"

    name = fields.Char(string="Nombre")

class OperacionDiaria(models.Model):
    _name="cuidados.operacion_diaria"

    name = fields.Char(string="Nombre")

    #asignar jardinero
    #listar plantas a cuidar
        #listar cuidados por planta

class TipodePlanta(models.Model):
    _name="cuidados.tipo_de_planta"

    name = fields.Char(string="Nombre")

#clase tipo planta
    #nombre
    #cuidado por defecto


class TipodePlanta(models.Model):
    _name="cuidados.tipo_de_planta"

    name = fields.Char(string="Nombre")

class TipodePlanta(models.Model):
    _name="cuidados.tipo_de_planta"

    name = fields.Char(string="Nombre")

class TipodePlanta(models.Model):
    _name="cuidados.tipo_de_planta"

    name = fields.Char(string="Nombre")


class Planta(models.Model):
    _name="cuidados.planta"


        #metodos planta

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


class Plagas(models.Model):
    _name="cuidados.plaga"

    name = fields.Char(string="Nombre")


#clase planta
    #atributos planta
        #nombre
        #tipo planta (m2o a tipo_planta)
    #dimensiones
    #color
    #tamano_max
#clase invernaderos
    #nombre
    co2 = 
    sistemas

#clase maceteros
    #dimensiones
    #tipo de macetero
    #tipo de riego


#clase plantacion
    #metricas
    #planta
    #seccion
    #invernadero
    #insumos
    foto_referencia = fields.Binary(string="Foto referencia planta")

#clase secciones
    #nombre
    #tipos de planta admitidos

#clase insumos
    #nombre

#clase jardineros

#clase maquinaria

#clase cuidado

#clase paso_cuidado
