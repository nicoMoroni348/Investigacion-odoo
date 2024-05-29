from odoo import api, fields, models


class CancelarOportunidadWizard(models.TransientModel):
    _name = "cancelar.oportunidad.wizard"
    _description = "Cancelar Oportunidad Wizard"

    oportunidad_id = fields.Many2one('oportunidad', string="Oportunidad")