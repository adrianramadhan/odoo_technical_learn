# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    material_type = fields.Char(string="Jenis Bahan")
    manufacturing_date = fields.Date(string="Tanggal Produksi")