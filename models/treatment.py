from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Treatment(models.Model):
    _name = 'odoo_vertical_hospital.treatment'
    _description = 'Formulario de Tratamientos'

    name = fields.Char(string='Código de tratamiento', required=True)
    treatment_name = fields.Char(string='Nombre del tratamiento')
    treating_physician = fields.Char(string='Médico tratante')
    
    @api.constrains('name')
    def _check_name(self):
        for record in self:
            if '026' in record.name:
                raise ValidationError("El código de tratamiento no puede contener la secuencia '026'.")
