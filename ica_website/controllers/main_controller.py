from odoo.http import Controller, request, route


class MainController(Controller):
    @route('/ica/info', type="http", auth="user",website=True)
    def ica_info(self):
        partner_ids = request.env['res.partner'].sudo().search([])
        data = {
            "message": "Hello Message",
            "partner_ids": partner_ids,
        }
        return request.render('ica_website.info', data)

    @route('/ica/details/<model("res.partner"):partner_id>', type="http", auth="user",website=True)
    def ica_detail(self, partner_id):
        data = {
            "partner": partner_id
        }
        return request.render('ica_website.details', data)
