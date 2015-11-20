# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Partner(models.Model):
    _inherit = ['res.partner']

    sector = fields.Many2one(comodel_name='gsos.business.sector', string='Business Sector',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        ondelete=None)

    rfc = fields.Char(string='RFC',
        help=None,
        readonly=False,
        required=False,
        groups=[])
