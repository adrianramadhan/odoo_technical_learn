from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string="Nama Buku", required=True)
    author = fields.Char(string="Penulis")
    isbn = fields.Char(string="Nomor ISBN")
    available_copies = fields.Integer(string="Jumlah Buku Tersedia", default=1)
    book_cover = fields.Binary(string="Sampul Buku")

    # Relasi One2many dengan peminjaman
    loan_ids = fields.One2many('library.loan', 'book_id', string="Peminjaman")