from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    books_ids = fields.One2many('ica.books', 'partner_id')