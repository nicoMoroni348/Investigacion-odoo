from odoo import models, fields, api

class Oportunidad(models.Model):
    _name = 'oportunidad'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Oportunidad'
    _rec_name = 'custom_id'

    custom_id = fields.Char(
        string="ID Oportunidad",
        required=True
    )

    descripcion = fields.Html(
        string="Descripcion"
    )

    estado = fields.Selection([
        ('nueva', 'Nueva'),
        ('en_proceso', 'En proceso'),
        ('finalizada', 'Finalizada'),
        ('suspendida', 'Suspendida'),
        ('cancelada', 'Cancelada')
    ], string="Estado", default="nueva", required=True)

    persona_id = fields.Many2one(
        'persona',
        string="Contacto asociado"
    )

    persona_genero = fields.Selection(
        related="persona_id.gender"
    )

    fecha_oportunidad = fields.Date(
        string="Fecha",
        default=fields.Date.context_today  # Datetime.now también funca
    )

    ref = fields.Char(
        string='Ref',
        help='Referencia de la persona',
        related="persona_id.ref"
    )

    prioridad = fields.Selection([
        ("0", "Normal"),
        ("1", "Baja"),
        ("2", "Media"),
        ("3", "Alta"),
        ("4", "Muy alta")
    ], string="Prioridad")

    # Para lo de google maps
    latitud = fields.Float(string="Latitud")
    longitud = fields.Float(string="Longitud")

    @api.onchange('persona_id')
    def onchange_persona_id(self):
        self.ref = self.persona_id.ref # Rellena el código pero no de la misma forma que el many2one,
                                        # este lo autocompleta de forma más personalizada

    def action_test(self):
        print("TEST CORRECTO")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Apretaste un botón :)',
                'type': 'rainbow_man'
            }
        }

    def cancelar_oportunidad(self):
        self.estado = 'cancelada'

    def suspender_oportunidad(self):
        self.estado = 'suspendida'