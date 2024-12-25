from odoo import models, fields # type: ignore

class Estudiante(models.Model):
    _name = 'estudiante'
    _description = 'Estudiante para probar access rights'
    
    name = fields.Char(
        string="Nombre",
        required=True
    )
    
    edad = fields.Integer(
        string="Edad"
    )
    
    email = fields.Char(
        string="Email"
    )
    
    phone = fields.Char(
        string="Telefono"
    )