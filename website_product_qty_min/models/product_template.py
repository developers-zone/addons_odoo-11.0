# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    min_qty = fields.Integer('Minimum Quantity', default=0)