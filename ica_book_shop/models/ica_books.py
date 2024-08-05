from odoo import api, fields, models

class IcaBooks(models.Model):
    _name = 'ica.books'
    _description = 'IcaBooks'

    name = fields.Char()
