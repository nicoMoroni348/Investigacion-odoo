from odoo import models, fields, api

class Oportunidad(models.Model):
    _name = 'oportunidad'
    _description = 'Oportunidad'

    custom_id = fields.Char(string="ID Oportunidad", required=True)
    descripcion = fields.Char(string="Descripcion", required=True)
    estado = fields.Selection([('Nueva', 'Nueva'), ('En proceso', 'En proceso'), ('Finalizada', 'Finalizada')], string="Estado", default="Nueva")
    persona_id = fields.Many2one('persona', string="Contacto asociado")
    persona_genero = fields.Selection(related="persona_id.gender")

    fecha_oportunidad = fields.Date(string="Fecha", default=fields.Date.context_today) # Datetime.now también funca


    # Para lo de google maps
    latitud = fields.Float(string="Latitud")
    longitud = fields.Float(string="Longitud")