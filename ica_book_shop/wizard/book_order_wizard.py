from odoo import api, fields, models


class BookOrderWizard(models.TransientModel):
    _name = 'book.order.wizard'
    _description = 'BookOrderWizard'

    partner_id = fields.Many2one('res.partner', string='Customer')
    line_ids = fields.One2many('books.order.wizard.line', 'order_id')

    def action_create_book_order(self):
        book_order = self.env['ica.books.order']
        # print("*" * 20)
        # print()
        data = {
            "partner_id": self.partner_id.id,
            # "line_ids": [
            #     (0, 0, {"book_id": 7, "sale_price": 500}),
            #     (0, 0, {"book_id": 7, "sale_price": 600})
            # ]
            "line_ids": [(0, 0, {
                "book_id": line_id.book_id.id,
                "sale_price": line_id.sale_price})
                         for line_id in self.line_ids]
        }
        # print(data)
        book_order.create(data)


class IcaBooksOrderLine(models.TransientModel):
    _name = 'books.order.wizard.line'
    _description = 'IcaBooksOrderLine'

    order_id = fields.Many2one('book.order.wizard')
    book_id = fields.Many2one('ica.books')
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  default=lambda self: self.env.company.currency_id)
    sale_price = fields.Monetary(string="Sale Price")
    author_id = fields.Many2one('res.partner', string="Author", related="book_id.partner_id")

    @api.onchange('book_id')
    def _onchange_sale_price(self):
        if self.book_id:
            self.sale_price = self.book_id.sale_price
