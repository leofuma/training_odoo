# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    name = fields.Char(string="Appointment", required=True)
    patient = fields.Many2one('res.partner', string="Patient")

    @api.multi
    def get_partner_id(self):
        res_partner = self.env['res.partner']
        id_partnerx = self._context.get('active_id')
        print(id_partnerx)