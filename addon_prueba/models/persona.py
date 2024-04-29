from odoo import api, fields, models
from datetime import date


class Persona(models.Model):
    _name = 'persona'
    _inherit = ['mail.thread.cc',
                'mail.thread.blacklist',
                'mail.activity.mixin',
                ]  # esto lo agrego para el chatter
    _description = 'Este es mi primer modelo'

    name = fields.Char(string='Nombre', required=True, tracking=True)
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    age = fields.Integer(string='Edad', compute='_compute_age', store=True) # campo que se calcula, y se guarda en la bda porque tiene el store=True
    gender = fields.Selection([('Hombre', 'hombre'), ('Mujer', 'mujer'), ('Otro', 'otro')], string='Genero',
                              required=True)
    active = fields.Boolean(string="Activo", default=True)
    email = fields.Char(string='Correo Electrónico', required=True)

    @api.depends('fecha_nacimiento')
    def _compute_age(self):
        for rec in self: # para evitar el SINGLETON error
            hoy = date.today()
            if rec.fecha_nacimiento:
                rec.age = hoy.year - rec.fecha_nacimiento.year
            else:
                rec.age = 0

    @api.depends('email')
    def _compute_email_normalized(self):
        for record in self:
            if record.email:
                # Realiza la normalización del correo electrónico aquí
                normalized_email = record.email.lower()  # Por ejemplo, convierte a minúsculas
                record.email_normalized = normalized_email
            else:
                record.email_normalized = False

