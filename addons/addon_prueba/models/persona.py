from odoo import api, fields, models
from datetime import date


class Persona(models.Model):
    _name = 'persona'
    _inherit = ['mail.thread.cc',
                'mail.thread.blacklist',
                'mail.activity.mixin',
                ]  # esto lo agrego para el chatter
    _description = 'Este es mi primer modelo'
    _rec_name = 'ref'

    name = fields.Char(
        string='Nombre', required=True, tracking=True
    )

    fecha_nacimiento = fields.Date(
        string="Fecha de nacimiento"
    )

    age = fields.Integer(
        string='Edad', compute='_compute_age', store=True
    ) # campo que se calcula, y se guarda en la bda porque tiene el store=True

    gender = fields.Selection(
        [('Hombre', 'hombre'), ('Mujer', 'mujer'), ('Otro', 'otro')],
        string='Genero', required=True
    )
    active = fields.Boolean(
        string="Activo", default=True
    )

    email = fields.Char(
        string='Correo Electrónico'
    )

    ref = fields.Char(
        string='Referencia'
    )

    oportunidad_id = fields.Many2one(
        'oportunidad', string="Oportunidad"
    )

    foto = fields.Image(string="Foto")

    tag_ids = fields.Many2many(
        'persona.tag', string="Tags"
    )

    # MÉTODOS
    @api.depends('fecha_nacimiento')  # Decorador para que se actualice ante un cambio en la interfaz
    def _compute_age(self):
        for rec in self:  # para evitar el SINGLETON error
            hoy = date.today()
            if rec.fecha_nacimiento:  # para evitar el NOT STORED COMPUTED FIELD error
                rec.age = hoy.year - rec.fecha_nacimiento.year
            else:
                rec.age = 1

    # Override Create Method
    @api.model_create_multi
    def create(self, vals):
        vals[0]['ref'] = self.env['ir.sequence'].next_by_code('persona')  # Genera el campo 'ref' secuencialmente
        return super(Persona, self).create(vals)

    def write(self, vals):
        return super(Persona, self).write(vals)

    def name_get(self):
        persona_list = []
        for rec in self:
            if rec.name and rec.ref:
                name = rec.name + " - " + rec.ref
                persona_list.append((rec.id, name))  # Fijate que se agrega una tupla

        return persona_list
