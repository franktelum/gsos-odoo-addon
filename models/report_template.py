# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ReportTemplate(models.Model):
    _name = 'gsos.report.template'

    name = fields.Char(string='Name',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    file_url = fields.Char(string='File URL',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    type = fields.Selection(
        selection=[
          ('complaints.totals', 'Complaints Totals'),
          ('suppliers.results', 'Suppliers Results')
        ],
        string='Type',
        help=None,
        readonly=False,
        required=False,
        groups=[])
