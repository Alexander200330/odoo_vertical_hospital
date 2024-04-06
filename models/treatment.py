from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Treatment(models.Model):
    _name = 'odoo_vertical_hospital.treatment'
    _description = 'Formulario de Tratamientos'
    _rec_name = 'name_code'

    name = fields.Char(string='Código de tratamiento', required=True)
    treatment_name = fields.Char(string='Nombre del tratamiento')
    treating_physician = fields.Char(string='Médico tratante')
    name_code = fields.Char(string='Nombre y Código', compute='_compute_name_code', store=True)
    
    @api.constrains('name')
    def _check_name(self):
        """
            Constraint para asegurar que el código de tratamiento no contenga la secuencia '026'.
        """
        for record in self:
            if '026' in record.name:
                raise ValidationError("El código de tratamiento no puede contener la secuencia '026'.")

    @api.depends('name', 'treatment_name')
    def _compute_name_code(self):
        """Me permite mostrar el nombre del registro formateado."""
        for record in self:
            record.name_code = f"{record.name} - {record.treatment_name}"