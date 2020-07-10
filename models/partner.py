# -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    lcc = fields.Many2one("lcc", default=False, string='Local currency')