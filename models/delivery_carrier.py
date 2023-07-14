# -*- coding: utf-8 -*-
from odoo import fields, models, api, _

class Transportes(models.Model):
    _inherit = "delivery.carrier"

    partner_id = fields.Many2one(comodel_name='res.partner', string='Compañia de Transporte')

    