# -*- coding: utf-8 -*-
from odoo import models, fields, api

#agenda es el nombre de la tabla que se va a dar en Postgre, lo definimos en _name
class agenda(models.Model):
     _name = 'agenda.agenda'
     _description = 'agenda.agenda'

#columnas de las tablas que vamos a definir
     nombre = fields.Char()
     telefono = fields.Char()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

