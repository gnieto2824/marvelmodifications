# -*- coding:utf-8 -*-
from odoo import fields, models


class stock_location(models.Model):
    _inherit = 'stock.location'

    row = fields.Integer(
        default=0,
        store=True,
        string='Row',
    )

    column = fields.Integer(
        default=0,
        store=True,
        string='Column',
    )

    depth = fields.Integer(
        default=0,
        store=True,
        string='Depth',
    )
