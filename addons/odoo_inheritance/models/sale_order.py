from odoo import api,models,fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    confirmed_user_id = fields.Many2one('res.users', string="Usuario confirmado")
    color = fields.Integer(string="Color")

    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        print(f"Color: {self.color}")
        if self.confirmed_user_id is not None:
            self.confirmed_user_id = self.env.user.id