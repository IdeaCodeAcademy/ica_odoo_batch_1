from odoo import api, fields, models


class IcaBooksOrder(models.Model):
    _name = 'ica.books.order'
    _description = 'IcaBooksOrder'
    _rec_name = 'partner_id'
    _order = "id desc"

    partner_id = fields.Many2one('res.partner', string='Customer')
    line_ids = fields.One2many('ica.books.order.line', 'order_id')


class IcaBooksOrderLine(models.Model):
    _name = 'ica.books.order.line'
    _description = 'IcaBooksOrderLine'

    order_id = fields.Many2one('ica.books.order')
    book_id = fields.Many2one('ica.books')
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  default=lambda self: self.env.company.currency_id)
    sale_price = fields.Monetary(string="Sale Price")
    author_id = fields.Many2one('res.partner', string="Author",related="book_id.partner_id")
    @api.onchange('book_id')
    def _onchange_sale_price(self):
        if self.book_id:
            self.sale_price = self.book_id.sale_price
