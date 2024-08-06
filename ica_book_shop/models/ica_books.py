from odoo import api, fields, models


class IcaBooks(models.Model):
    _name = 'ica.books'
    _description = 'IcaBooks'

    name = fields.Char(required=True)
    release_year = fields.Integer()
    cover = fields.Binary()
    partner_id = fields.Many2one('res.partner', string="Author", required=True)
    category_ids = fields.Many2many('ica.book.category')
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('available', 'Available'),
            ('no_available', 'Not Available'),
            ('cancel', 'Cancel'),
        ]
        , default='draft')
