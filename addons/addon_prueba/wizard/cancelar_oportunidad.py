import datetime
from odoo import api, fields, models


class CancelarOportunidadWizard(models.TransientModel):
    _name = "cancelar.oportunidad.wizard"
    _description = "Cancelar Oportunidad Wizard"

    @api.model
    def default_get(self, fields_list):
        res = super(CancelarOportunidadWizard, self).default_get(fields_list)
        res['fecha_cancelacion'] = datetime.date.today()
        return res

    oportunidad_id = fields.Many2one(
        'oportunidad', string="Oportunidad"
    )

    motivo = fields.Text(
        string="Motivo de cancelación"
    )

    fecha_cancelacion = fields.Date(
        string="Fecha de cancelación"
    )

    def action_cancelar(self):
        for rec in self:  # Para evitar el error singleton
            rec.oportunidad_id.cancelar_oportunidad()