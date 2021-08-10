# -*- coding: utf-8 -*-
# from odoo import http


# class ProductExcelReport(http.Controller):
#     @http.route('/product_excel_report/product_excel_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_excel_report/product_excel_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_excel_report.listing', {
#             'root': '/product_excel_report/product_excel_report',
#             'objects': http.request.env['product_excel_report.product_excel_report'].search([]),
#         })

#     @http.route('/product_excel_report/product_excel_report/objects/<model("product_excel_report.product_excel_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_excel_report.object', {
#             'object': obj
#         })
