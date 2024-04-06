from odoo import http
from odoo.http import request
from werkzeug.exceptions import NotFound
import json

class PatientRESTController(http.Controller):
    @http.route('/pacientes/consulta/<string:seq>', auth='public', type='http', methods=['GET'], csrf=False)
    def consultar_paciente(self, seq):
        paciente = request.env['odoo_vertical_hospital.patient'].sudo().search([('name', '=', seq)], limit=1)
        if paciente:
            response = {
                'seq': paciente.name,
                'name': f"{paciente.first_name} {paciente.last_name}",
                'rnc': paciente.rnc,
                'state': paciente.state,
            }
            return json.dumps(response)
        else:
            return NotFound(description='Paciente no encontrado')
