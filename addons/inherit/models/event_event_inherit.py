# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EventEventInherit(models.Model):
    _inherit = 'event.event'

    event_type = fields.Selection([('physical', 'Physical'), ('virtual', 'Virtual')], string="Event Type", default='physical')