# -*- coding: utf-8 -*-
# from odoo import http


# class Cibeles(http.Controller):
#     @http.route('/cibeles/cibeles/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cibeles/cibeles/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cibeles.listing', {
#             'root': '/cibeles/cibeles',
#             'objects': http.request.env['cibeles.cibeles'].search([]),
#         })

#     @http.route('/cibeles/cibeles/objects/<model("cibeles.cibeles"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cibeles.object', {
#             'object': obj
#         })
