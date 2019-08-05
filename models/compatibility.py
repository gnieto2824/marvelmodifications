# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductoTemplate(models.Model):
    _inherit = "product.template"

    compatible_product_ids = fields.Many2many(
        'product.template', 'product_compatible_rel', 'src_id', 'dest_id',
        string='Compatible',)
