from odoo import models, fields # type: ignore

class CustomModuleMaintenanceLog(models.Model):
    _name = 'custom_module.maintenance.log'
    _description = 'custom_module Maintenance Log'

    product_id = fields.Many2one('custom_module.product', string="Produk", ondelete='cascade')
    maintenance_date = fields.Date(string="Tanggal Pemeliharaan", default=fields.Date.today)
    notes = fields.Text(string="Catatan Pemeliharaan")
    maintenance_by = fields.Many2one('res.users', string="Dilakukan Oleh", default=lambda self: self.env.user)