from odoo import http
from odoo.http import request

class Politic(http.Controller):
    @http.route('/form_politic_web',type="http", auth="public", website=True)
    def politic_webform(self, **kw):
        return http.request.render('Encuestas_Politicas.create_form_politic', {})
    print("paso el def")

    @http.route('/create/webformpolitic', type="http", auth="public", website=True)
    def create_webform(self, **kw):
        request.env['forms.politic'].sudo().create(kw)
        return request.render('Encuestas_Politicas.webform_thanks', {})


