from odoo import models, fields # type: ignore

class CustomModuleProduct(models.Model):
    _name = 'custom_module.product'
    _description = 'custom_module Product'

    # Fields Dasar
    name = fields.Char(string="Nama Produk", required=True)
    description = fields.Text(string="Deskripsi")
    sku = fields.Char(string="SKU (Stock Keeping Unit)", required=True)
    price = fields.Float(string="Harga", digits=(10, 2))
    quantity = fields.Integer(string="Jumlah Stok", default=0)
    is_available = fields.Boolean(string="Tersedia", default=True)
    purchase_date = fields.Date(string="Tanggal Pembelian")
    created_at = fields.Datetime(string="Dibuat Pada", default=fields.Datetime.now)
    product_image = fields.Binary(string="Gambar Produk")

    # Relasi
    supplier_id = fields.Many2one('res.partner', string="Pemasok")
    category_ids = fields.Many2many(
        'product.category',            
        'custom_product_category_rel', 
        'product_id',                  
        'category_id',                 
        string="Kategori"
    )

    # Selection
    condition = fields.Selection([
        ('new', 'Baru'),
        ('used', 'Bekas'),
        ('refurbished', 'Refurbished'),
    ], string="Kondisi", default='new')

    # Field Monetary
    currency_id = fields.Many2one('res.currency', string="Mata Uang")
    total_value = fields.Monetary(string="Total Nilai", currency_field='currency_id')

    # Field Reference
    related_document = fields.Reference([
        ('res.partner', 'Partner'),
        ('res.users', 'User'),
    ], string="Dokumen Terkait")

    # Field HTML
    notes = fields.Html(string="Catatan Tambahan")

    # One2many Relasi ke Model Lain
    maintenance_log_ids = fields.One2many('custom_module.maintenance.log', 'product_id', string="Log Pemeliharaan")

    # Field Readonly dan Default
    created_by = fields.Many2one('res.users', string="Dibuat Oleh", default=lambda self: self.env.user, readonly=True)