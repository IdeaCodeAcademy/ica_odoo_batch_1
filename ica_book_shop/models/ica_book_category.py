from odoo import api, fields, models


class IcaBookCategory(models.Model):
    _name = 'ica.book.category'
    _description = 'IcaBookCategory'
    _parent_store = True

    name = fields.Char(required=True)
    image = fields.Binary()
    parent_id = fields.Many2one('ica.book.category', string='Parent Category')
    child_ids = fields.One2many('ica.book.category', 'parent_id')
    parent_path = fields.Char(index=True, unaccent=False)
    sequence = fields.Integer(string='Sequence')
