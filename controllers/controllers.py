from odoo import http
from odoo.http import request
from werkzeug.exceptions import NotFound, Forbidden
import json

class PatientRESTController(http.Controller):
    @http.route('/pacientes/consulta/<string:seq>', auth='public', type='http', methods=['GET'], csrf=False)
    def consultar_paciente(self, seq):
        # Leer el valor del campo use_hospital_feature
        use_hospital_feature = request.env['ir.config_parameter'].sudo().get_param('your_module.use_hospital_feature')
        # Verificar si la funcionalidad del hospital está activada
        if use_hospital_feature:
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
        else:
            return Forbidden(description=f'Funcionalidad del hospital no activada')
