from odoo import api, models, fields, _

class customer(models.Model):
        
        # テーブル名
        _name = "library.customer"
        
        name = fields.Text(required=True, string="customer name")
        book_id = fields.Many2one("library.book")