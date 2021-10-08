# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Product(models.Model):
    _inherit = 'product.template'

    leofuma_state_product_field = fields.Selection(string="State",
                selection=[
                    ('new', 'New'),
                    ('used', 'Used'),
                    ],
                    required=False,
            )
