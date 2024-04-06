# -*- coding: utf-8 -*-
# from odoo import http


# class OdooVerticalHospital(http.Controller):
#     @http.route('/odoo_vertical_hospital/odoo_vertical_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_vertical_hospital/odoo_vertical_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_vertical_hospital.listing', {
#             'root': '/odoo_vertical_hospital/odoo_vertical_hospital',
#             'objects': http.request.env['odoo_vertical_hospital.odoo_vertical_hospital'].search([]),
#         })

#     @http.route('/odoo_vertical_hospital/odoo_vertical_hospital/objects/<model("odoo_vertical_hospital.odoo_vertical_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_vertical_hospital.object', {
#             'object': obj
#         })
