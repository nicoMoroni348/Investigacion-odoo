from odoo import http
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)

class Estudiantes(http.Controller):
    @http.route('/estudiantes', website=True, auth='public')
    def estudiante(self, **kw):
        estudiantes = request.env['estudiante'].sudo().search([])
        _logger.info(f'ESTUDIANTES: {estudiantes}')
        return request.render("addon_prueba.estudiantes_page", {
            'estudiantes': estudiantes
        }) 
    

class Personas(http.Controller):
    @http.route('/personas', website=True, auth='public')
    def personas(self, **kw):
        personas = request.env['persona'].sudo().search([])
        values = {
            'personas': personas,
            'otro_valor': "Acá hay otro valor random que paso por parámetro"
        }
        template = "addon_prueba.personas_page"
        return request.render(template, values) 