from odoo import api, fields, models
from odoo.tests.common import Form, tagged, users


class IcaBooks(models.Model):
    _name = 'ica.books'
    _description = 'IcaBooks'

    name = fields.Char(required=True, copy=True)
    release_year = fields.Integer(copy=False)
    cover = fields.Binary()
    partner_id = fields.Many2one('res.partner', string="Author", required=True)
    mobile = fields.Char(related="partner_id.mobile", readonly=True)
    email = fields.Char(related="partner_id.email")
    image_1920 = fields.Binary(related="partner_id.image_1920")
    category_ids = fields.Many2many('ica.book.category')
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('available', 'Available'),
            ('no_available', 'Not Available'),
            ('cancel', 'Cancel'),
        ]
        , default='draft')

    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', string="Currency", related='company_id.currency_id')
    sale_price = fields.Monetary(string="Sale Price", copy=False)
    active = fields.Boolean(default=True)
    download_link_ids = fields.One2many('ica.books.download.link.line', 'book_id')
    line_ids = fields.One2many('ica.books.order.line', 'book_id')

    def action_draft(self):
        self.state = 'draft'

    def action_available(self):
        # data = [
        #     (1, self.download_link_ids[1].id, {
        #         # "book_id": self.id,
        #         "name": "Google MM",
        #         # "download_link": "https://localhost:8069/books"
        #     }),
        #     # (0, 0, {
        #     #     # "book_id": self.id,
        #     #     "name": "Mega",
        #     #     "download_link": "https://localhost:8069/books"
        #     # })
        # ]
        # print("*" * 10)
        # print(data)
        # self.write({
        #     "download_link_ids": data
        # })
        # self.download_link_ids.unlink()
        # self.download_link_ids.create(data)
        self.state = 'available'

    def action_no_available(self):
        self.state = 'no_available'

    def action_cancel(self):
        self.state = 'cancel'

    def action_book_order(self):
        wizard = self.env['book.order.wizard'].create({
            "partner_id": self.env.user.partner_id.id,
            "line_ids": [
                (0, 0, {
                    "book_id": self.id,
                })
            ]

        })
        wizard.line_ids._onchange_sale_price()
        return {
            "type": "ir.actions.act_window",
            "res_model": "book.order.wizard",
            "res_id": wizard.id,
            "view_mode": "form",
            "target": "new",
        }
        # Form
        # ...


class BookDownloadLink(models.Model):
    _name = 'ica.books.download.link.line'
    _description = 'Book Download Link'

    name = fields.Char(required=True)
    download_link = fields.Char()
    book_id = fields.Many2one('ica.books', string="Book")
    sequence = fields.Integer()
