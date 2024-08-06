from odoo import api, fields, models

class IcaBookCategory(models.Model):
    _name = 'ica.book.category'
    _description = 'IcaBookCategory'

    name = fields.Char(required=True)
    parent_category_id = fields.Many2one('ica.book.category', string='Parent Category')
    sequence = fields.Integer(string='Sequence')