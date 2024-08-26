from odoo.http import request, route, Controller

class Ica_book_shopController(Controller):
    @route("/ica_book_shop/standalone_app", auth="public")
    def standalone_app(self):
        return request.render(
            'ica_book_shop.standalone_app',
            {
                'session_info': request.env['ir.http'].get_frontend_session_info(),
            }
        )
