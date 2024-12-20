# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MyResource(models.Model):
    _name = 'my.resource'
    _description = 'my.resource'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    price = fields.Float(string="Price", default=0.0)
    active = fields.Boolean(string="Is Active", default=True)