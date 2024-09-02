from odoo import http
from odoo.http import request


class IcaBookController(http.Controller):
    @http.route('/ica/books', type='json', auth='user')
    def get_all_books(self,limit=0,fields=[], **kw):
        book_ids = request.env['ica.books'].search_read(domain=[], limit=limit, offset=0, fields=fields)
        return {"message": "All Books", "book_ids": book_ids}

    @http.route('/ica/login', type='json', auth='none')
    def login(self, **kw):
        username = kw.get('username')
        password = kw.get('password')
        uid = request.session.authenticate(request.session.db, username, password)
        return {"uid": uid}

    @http.route('/ica/create/books', type='json', auth='user')
    def login(self, **kw):
        data = request.env['ica.books'].create(kw)
        return {"data":data.read(),"message":"Books Create successfully."}