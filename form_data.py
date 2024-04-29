# -*- coding: utf-8 -*-
from io import BytesIO
from odoo import models, fields
import qrcode, datetime
import base64
from odoo import http
from odoo.http import request
class forms_politics(models.Model):
    _name = 'forms.politic'
    name = fields.Char(string="Nombres")
    apellido = fields.Char(string="Apellidos")
    curp = fields.Char(string="CURP")
    seccional = fields.Char(string="Seccional")
    domicilio = fields.Char(string="Domicilio")
    colonia = fields.Char(string="Colonia")
    comunidad = fields.Char(string="Comunidad")
    telefono = fields.Char(string="Telefono")
    referencia = fields.Char(string="Referencia")
    nota = fields.Text(string="Nota")


# class WebsiteFormController(http.Controller):
#
#     @http.route('/crear_registro', type='http', auth='user', website=True)
#     def crear_registro(self, **post):
#         Formulario = request.env['forms.politic']
#         nuevo_registro = Formulario.create({
#             'name': post.get('name'),
#             'apellido': post.get('apellido'),
#             'curp': post.get('curp'),
#             'seccional': post.get('seccional'),
#             'domicilio': post.get('domicilio'),
#             'colonia': post.get('colonia'),
#             'comunidad': post.get('comunidad'),
#             'telefono': post.get('telefono'),
#             'referencia': post.get('referencia'),
#             'nota': post.get('nota'),
#             # Agrega los campos y valores correspondientes aquí
#         })
#         return request.redirect('/ruta/a/la/página/de/éxito')