from odoo import api, fields, models


class Persona(models.Model):
    _name = 'persona'
    _inherit = ['mail.thread.cc',
                'mail.thread.blacklist',
                'mail.activity.mixin',
                ]  # esto lo agrego para el chatter
    _description = 'Este es mi primer modelo'

    name = fields.Char(string='Nombre', required=True)
    age = fields.Integer(string='Edad', required=False)
    gender = fields.Selection([('Hombre', 'hombre'), ('Mujer', 'mujer'), ('Otro', 'otro')], string='Genero',
                              required=True)
    active = fields.Boolean(string="Activo", default=True)

    # """ ESTO ME LO TIRO EL CHAT PARA SOLUCIONAR EL ERROR DEL CHATTER"""

    email = fields.Char(string='Correo Electrónico')

@api.depends('email')
def _compute_email_normalized(self):
    for record in self:
        if record.email:
            # Realiza la normalización del correo electrónico aquí
            normalized_email = record.email.lower()  # Por ejemplo, convierte a minúsculas
            record.email_normalized = normalized_email
        else:
            record.email_normalized = False
