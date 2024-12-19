# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplateInherit(models.Model):
    _name = 'new.product'
    _inherits = {'product.template': 'product_template_id'}

    product_template_id = fields.Many2one('product.template', string='Product Template', required=True, ondelete='cascade')
    warranty_period = fields.Integer(string="Garansi (Bulan)")