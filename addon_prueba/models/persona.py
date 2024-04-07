from odoo import api, fields, models


class Persona(models.Model):
    _name = 'persona'
    _description = 'Este es mi primer modelo'

    name = fields.Char(string='Nombre', required=True)
    age = fields.Integer(string='Edad', required=False)
    gender = fields.Selection([('Hombre', 'hombre'), ('Mujer', 'mujer'), ('Otro', 'otro')], string='Genero')
