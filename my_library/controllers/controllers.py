# -*- coding: utf-8 -*-
# from odoo import http


# class SimplifyCustom/courses(http.Controller):
#     @http.route('/simplify_custom/courses/simplify_custom/courses', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/simplify_custom/courses/simplify_custom/courses/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('simplify_custom/courses.listing', {
#             'root': '/simplify_custom/courses/simplify_custom/courses',
#             'objects': http.request.env['simplify_custom/courses.simplify_custom/courses'].search([]),
#         })

#     @http.route('/simplify_custom/courses/simplify_custom/courses/objects/<model("simplify_custom/courses.simplify_custom/courses"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('simplify_custom/courses.object', {
#             'object': obj
#         })
