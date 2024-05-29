from odoo import api, fields, models


class CancelarOportunidadWizard(models.TransientModel):
    _name = "cancelar.oportunidad.wizard"
    _description = "Cancelar Oportunidad Wizard"

    oportunidad_id = fields.Many2one('oportunidad', string="Oportunidad")
    motivo = fields.Text(string="Motivo de cancelación")

    def action_cancelar(self):
        for rec in self:  # Para evitar el error singleton
            rec.oportunidad_id.cancelar_oportunidad()