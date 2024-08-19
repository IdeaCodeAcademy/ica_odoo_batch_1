from odoo import api, fields, models, _


class IcaBooksOrder(models.Model):
    _name = 'ica.books.order'
    _description = 'IcaBooksOrder'
    _rec_name = 'partner_id'
    _order = "id desc"

    name = fields.Char(string='Name', default=lambda self: _('New'), readonly=True)
    partner_id = fields.Many2one('res.partner', string='Customer')
    line_ids = fields.One2many('ica.books.order.line', 'order_id')

    @api.model
    def create(self, values):
        # Add code here
        if values.get('name', _("New")) == _('New'):
            values['name'] = self.env['ir.sequence'].next_by_code(self._name) or _('New')
        return super(IcaBooksOrder, self).create(values)


class IcaBooksOrderLine(models.Model):
    _name = 'ica.books.order.line'
    _description = 'IcaBooksOrderLine'

    order_id = fields.Many2one('ica.books.order')
    partner_id = fields.Many2one('res.partner', string='Customer',related="order_id.partner_id")
    book_id = fields.Many2one('ica.books')
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  default=lambda self: self.env.company.currency_id)
    sale_price = fields.Monetary(string="Sale Price")
    author_id = fields.Many2one('res.partner', string="Author", related="book_id.partner_id")

    @api.onchange('book_id')
    def _onchange_sale_price(self):
        if self.book_id:
            self.sale_price = self.book_id.sale_price
