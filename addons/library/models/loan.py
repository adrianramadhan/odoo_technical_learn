from odoo import models, fields

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Library Loan'

    book_id = fields.Many2one('library.book', string="Buku", required=True)
    borrower_name = fields.Char(string="Nama Peminjam", required=True)
    loan_date = fields.Date(string="Tanggal Peminjaman", default=fields.Date.today)
    return_date = fields.Date(string="Tanggal Pengembalian")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('borrowed', 'Dipinjam'),
        ('returned', 'Dikembalikan')
    ], string="Status", default='draft')