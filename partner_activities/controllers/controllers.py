# -*- coding: utf-8 -*-
from openerp import http

# class Iscritti(http.Controller):
#     @http.route('/iscritti/iscritti/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iscritti/iscritti/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('iscritti.listing', {
#             'root': '/iscritti/iscritti',
#             'objects': http.request.env['iscritti.iscritti'].search([]),
#         })

#     @http.route('/iscritti/iscritti/objects/<model("iscritti.iscritti"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iscritti.object', {
#             'object': obj
#         })


class partner_activities(http.Controller):
    @http.route('/activities/', auth='public')
    def index(self, **kw):
       return "Hello, world"
    @http.route('/activities/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('activities.listing', {
          'root': '/activities',
           'objects': http.request.env['partner_activities.activity'].search([]),
    })
    @http.route('/activities/objects/<model("partner_activities.activity"):obj>/', auth='public')
    def object(self, obj, **kw):
         return http.request.render('iscritti.object', {
             'object': obj
    })