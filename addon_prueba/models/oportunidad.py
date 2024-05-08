from odoo import models, fields, api

class Oportunidad(models.Model):
    _name = 'oportunidad'
    _description = 'Oportunidad'
    _rec_name = 'custom_id'

    custom_id = fields.Char(string="ID Oportunidad", required=True)
    descripcion = fields.Html(string="Descripcion")
    estado = fields.Selection([('Nueva', 'Nueva'), ('En proceso', 'En proceso'), ('Finalizada', 'Finalizada')], string="Estado", default="Nueva")
    persona_id = fields.Many2one('persona', string="Contacto asociado")
    persona_genero = fields.Selection(related="persona_id.gender")

    fecha_oportunidad = fields.Date(string="Fecha", default=fields.Date.context_today) # Datetime.now también funca
    ref = fields.Char(string='Referencia')


    # Para lo de google maps
    latitud = fields.Float(string="Latitud")
    longitud = fields.Float(string="Longitud")

    @api.onchange('persona_id')
    def onchange_persona_id(self):
        self.ref = self.persona_id.ref # Rellena el código pero no de la misma forma que el many2one,
                                        # este lo autocompleta de forma más personalizada