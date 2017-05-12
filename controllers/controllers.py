# -*- coding: utf-8 -*-
from odoo import http

# class EbXedoV1(http.Controller):
#     @http.route('/eb_xedo_v1/eb_xedo_v1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eb_xedo_v1/eb_xedo_v1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('eb_xedo_v1.listing', {
#             'root': '/eb_xedo_v1/eb_xedo_v1',
#             'objects': http.request.env['eb_xedo_v1.eb_xedo_v1'].search([]),
#         })

#     @http.route('/eb_xedo_v1/eb_xedo_v1/objects/<model("eb_xedo_v1.eb_xedo_v1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eb_xedo_v1.object', {
#             'object': obj
#         })