from odoo import models, fields, api, _

class Patient(models.Model):
    _name = 'odoo_vertical_hospital.patient'
    _description = 'Formulario de Pacientes'
    _inherit = 'mail.thread'
    
    name = fields.Char(string='Número de Paciente', readonly=True)
    first_name = fields.Char(string='Nombre')
    last_name = fields.Char(string='Apellido')
    rnc = fields.Char(string='RNC', size=11, tracking=True)
    date_admission = fields.Datetime(string='Fecha de Alta', default=fields.Datetime.now)
    state = fields.Selection([('draft', 'Borrador'), ('admission', 'Alta'), ('discharge', 'Baja')], string='Estado', default='draft', tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('odoo_vertical_hospital.patient.sequence') or _('New')
        return super(Patient, self).create(vals)
