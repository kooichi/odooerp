from odoo import api, models, fields, _

class book(models.Model):
        _name = "library.book"
        
        name = fields.Text(required=True)
        isbn = fields.Text(required=True)
        edition_data = fields.Date()
        
        #参照キーを作成
        rented_by = fields.One2many("library.customer", "book_id")
        