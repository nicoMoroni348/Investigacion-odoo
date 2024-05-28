from odoo import api, fields, models


class PersonaTag(models.Model):
    _name = 'persona.tag'
    _description = 'Etiqueta de persona'

    nombre = fields.Char(
        string="Nombre",
        required=True
    )

    color = fields.Integer(
        string="Color"
    )

    activo = fields.Boolean(
        string="Activo",
        default=True
    )
