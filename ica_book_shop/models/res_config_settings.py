from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    ica_book_admin = fields.Many2one('res.partner', string='ICA Book Admin')


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    ica_book_shop_boolean = fields.Boolean(string='ICA Book Shop',
                                           config_parameter='ica_book_shop.ica_book_shop_boolean')
    ica_book_shop_char = fields.Char(string='ICA Book Shop Char', config_parameter='ica_book_shop.ica_book_shop_char')
    ica_book_admin = fields.Many2one('res.partner', string='ICA Book Admin', related="company_id.ica_book_admin",
                                     readonly=False)
