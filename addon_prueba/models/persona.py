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
    email = fields.Char(string='Correo Electrónico')
    ref = fields.Char(string='Referencia')
    oportunidad_id = fields.Many2one('oportunidad', string="Oportunidad")
    foto = fields.Image(string="Foto")

    tag_ids = fields.Many2many(
        'persona.tag', string="Tags"
    )

    @api.depends('fecha_nacimiento')
    def _compute_age(self):
        for rec in self: # para evitar el SINGLETON error
            hoy = date.today()
            if rec.fecha_nacimiento:
                rec.age = hoy.year - rec.fecha_nacimiento.year
            else:
                rec.age = 1

    @api.model_create_multi  # Uso "Multi" para evitar el warning
    def create(self, vals):
        print("VALS: ", vals)
        # vals[0]['ref'] = '1'
        # De esta forma sobreescribe el registro "referencia", sin importar lo que
        # ponga se va a guardar el 1
        return super(Persona, self).create(vals)

