from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    use_hospital_feature = fields.Boolean(string='Usar Funcionalidad del Endpoint', config_parameter='your_module.use_hospital_feature')
