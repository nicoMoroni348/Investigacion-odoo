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

    responsable = fields.Many2one(
        'res.users',
        string="Responsable"
    )

    latitud = fields.Float(
        string="Latitud"
    )

    longitud = fields.Float(
        string="Longitud"
    )

    # One2Many field
    nodo_lines_ids = fields.One2many(
        'nodo.lines', 'id_oportunidad', string="Nodos"
    )

    esconder_campo = fields.Boolean(
        string="Esconder campo", default=False
    )

    # MÉTODOS
    @api.onchange('persona_id')
    def onchange_persona_id(self):
        self.ref = self.persona_id.ref  # Rellena el código pero no de la misma forma que el many2one,
        # este lo autocompleta de forma más personalizada

    # Botón de testing -> efecto "arcoíris"
    def action_test(self):
        print("TEST CORRECTO")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Apretaste un botón :)',
                'type': 'rainbow_man'
            }
        }

    # Botones Cambio de estado de la oportunidad
    def cancelar_oportunidad(self):
        for rec in self:  # Para evitar el error singleton
            rec.estado = 'cancelada'

    def suspender_oportunidad(self):
        for rec in self:  # Para evitar el error singleton
            rec.estado = 'suspendida'

    def en_proceso_oportunidad(self):
        for rec in self:  # Para evitar el error singleton
            rec.estado = 'en_proceso'

    def finalizar_oportunidad(self):
        for rec in self:  # Para evitar el error singleton
            rec.estado = 'finalizada'


class nodoLines(models.Model):
    _name = "nodo.lines"
    _description = "Linea de nodos"

    product_id = fields.Many2one(
        'product.product', required=True
    )

    cantidad = fields.Integer(
        string="Cantidad", default=1
    )

    precio_unitario = fields.Float(
        related="product_id.list_price", string="Precio Unitario"
    )

    precio_final = fields.Float(
        string="Precio Final", compute="_calcular_precio", store=True
    )

    id_oportunidad = fields.Many2one(
        'oportunidad', string="Oportunidad"
    )

    @api.depends('product_id', 'cantidad')
    def _calcular_precio(self):
        for rec in self:
            if rec.product_id:
                rec.precio_final = rec.cantidad * rec.precio_unitario
            else:
                rec.precio_final = 0
