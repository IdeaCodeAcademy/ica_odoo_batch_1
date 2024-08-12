from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    books_ids = fields.One2many('ica.books', 'partner_id')
    book_count = fields.Integer(compute="_compute_books")

    @api.depends('books_ids')
    def _compute_books(self):
        self.book_count = len(self.books_ids)

    def action_books(self):
        ...
        return {
            "name": f"{self.name}'s Books",
            "type": "ir.actions.act_window",
            "res_model": "ica.books",
            "view_mode": "tree,graph,form"
        }
