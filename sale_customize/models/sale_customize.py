# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    order_line = fields.One2many('sale.order.line', 'order_id', string='Order Lines', states={'cancel': [('readonly', True)], 'done': [('readonly', True)]}, copy=True, auto_join=True)

    leofuma_state_product_field = fields.Selection(string="State",
                                                   selection=[
                                                       ('new', 'New'),
                                                       ('used', 'Used'),
                                                   ],
                                                   required=False,
                                                   )

    guantomeny = fields.One2many('sale.order', 'partner_id')