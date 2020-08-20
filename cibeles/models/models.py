# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cibeles(models.Model):
    _name = 'purchase.order'
    _inherit = 'purchase.order'

    numero_OC = fields.Integer(string="Número orden de compra")
    numero_contenedor = fields.Char(string="Número contenedor")
    bl = fields.Char(string="BL")
    naviera = fields.Char(string="Naviera")
    fecha_embarque = fields.Date(string="Fecha de embarque")
    enviado = fields.Boolean(string="Enviado", default=False)

class order_extend(models.Model):
    _name = 'purchase.order.line'
    _inherit = 'purchase.order.line'

    piezas_por_caja = fields.Integer(string="Piezas por caja", required=True)
    cajas_total = fields.Integer(string="Cajas total", required=True)
    total_piezas = fields.Integer(string="Total piezas", required=True)

    # @api.depends('piezas_por_caja')
    # def cajas_por_piezas(self):
    #     if (self.piezas_por_caja > 0) and (self.cajas_total > 0):
    #         self.total_piezas = self.piezas_por_caja*self.cajas_total

