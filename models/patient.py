from odoo import models, fields, api

class Patient(models.Model):
    _name = 'odoo_vertical_hospital.patient'
    _description = 'Formulario de Pacientes'

    first_name = fields.Char(string='Nombre')
    last_name = fields.Char(string='Apellido')
    rnc = fields.Char(string='RNC', size=11)
    date_admission = fields.Datetime(string='Fecha de Alta', default=fields.Datetime.now)
    state = fields.Selection([('draft', 'Borrador'), ('admission', 'Alta'), ('discharge', 'Baja')], string='Estado', default='draft')
