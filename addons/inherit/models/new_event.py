# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EventEventInherit(models.Model):
    _name = 'new.event'
    _inherits = {'event.event': 'event_event_id'}

    event_event_id = fields.Many2one('event.event', string='Event Template', required=True, ondelete='cascade')
    premium_ticket_price = fields.Float(string="Harga Tiket Premium")
    vip_perks = fields.Text(string="Fasilitas VIP")