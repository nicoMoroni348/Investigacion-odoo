from odoo import api, fields, models


class PersonaTag(models.Model):
    _name = 'persona.tag'
    _description = 'Etiqueta de persona'

    name = fields.Char(
        string="Nombre",
        required=True
    )

    color = fields.Integer(
        string="Color"
    )

    active = fields.Boolean(
        string="Activo",
        default=True
    )


