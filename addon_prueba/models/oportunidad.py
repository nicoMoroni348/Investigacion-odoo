from odoo import models, api, fields

class Oportunidad(models.Model):
    _name = 'oportunidad'
    _description = 'Oportunidad'

    name = fields.Char(string="Nombre")
    state = fields.Selection([('Nueva', 'nueva'), ('En proceso', 'en proceso'), ('Finalizada', 'finalizada')], string="Estado")
