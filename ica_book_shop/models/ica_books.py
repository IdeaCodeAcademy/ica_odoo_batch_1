from odoo import api, fields, models


class IcaBooks(models.Model):
    _name = 'ica.books'
    _description = 'IcaBooks'

    name = fields.Char(required=True)
    release_year = fields.Integer()
    cover = fields.Binary()
    partner_id = fields.Many2one('res.partner', string="Author", required=True)
    mobile = fields.Char(related="partner_id.mobile",readonly=True)
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
    sale_price = fields.Monetary(string="Sale Price")

    def action_draft(self):
        self.state = 'draft'

    def action_available(self):
        self.state = 'available'

    def action_no_available(self):
        self.state = 'no_available'

    def action_cancel(self):
        self.state = 'cancel'
