from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Patient(models.Model):
    _name = 'odoo_vertical_hospital.patient'
    _description = 'Formulario de Pacientes'
    _inherit = 'mail.thread'
    
    name = fields.Char(string='Número de Paciente', readonly=True)
    first_name = fields.Char(string='Nombre')
    last_name = fields.Char(string='Apellido')
    rnc = fields.Char(string='RNC', size=11, tracking=True)
    date_admission = fields.Datetime(string='Fecha de Alta')
    state = fields.Selection([('draft', 'Borrador'), ('admission', 'Alta'), ('discharge', 'Baja')], string='Estado', default='draft', tracking=True)
    treatment_ids = fields.One2many('odoo_vertical_hospital.patient.treatment', 'patient_id', string='Tratamientos Realizados')

    @api.model
    def create(self, vals):
        """Obtener la siguiente secuencia en la creación de un nuevo registro.
        """
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('odoo_vertical_hospital.patient.sequence') or _('New')
        return super(Patient, self).create(vals)
    
    @api.constrains('rnc')
    def _check_rnc(self):
        """
            Constraint para asegurar que no se escriban letras en el campo RNC.
        """
        for record in self:
            rnc = record.rnc
            if rnc and not rnc.isdigit():
                raise ValidationError("El RNC debe contener solo números.")

class PatientTreatment(models.Model):
    _name = 'odoo_vertical_hospital.patient.treatment'
    _description = 'Tratamientos Realizados por Pacientes'

    patient_id = fields.Many2one('odoo_vertical_hospital.patient', string='Paciente')
    treatment_id = fields.Many2one('odoo_vertical_hospital.treatment', string='Tratamiento Realizado', required=True)

    # Campos relacionados para mostrar el código y nombre del tratamiento
    treatment_code = fields.Char(string='Código del Tratamiento', related='treatment_id.name', readonly=True)
    treatment_name = fields.Char(string='Nombre del Tratamiento', related='treatment_id.treatment_name', readonly=True)
