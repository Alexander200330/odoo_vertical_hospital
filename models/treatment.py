from odoo import models, fields

class Treatment(models.Model):
    _name = 'odoo_vertical_hospital.treatment'
    _description = 'Formulario de Tratamientos'

    name = fields.Char(string='Código de tratamiento', required=True)
    treatment_name = fields.Char(string='Nombre del tratamiento')
    treating_physician = fields.Char(string='Médico tratante')
