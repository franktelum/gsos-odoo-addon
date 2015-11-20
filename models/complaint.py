# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ComplaintSeverity(models.Model):
    _name = "gsos.complaint.severity"

    name = fields.Char(string='Name',
        help=None,
        readonly=False,
        required=True,
        groups=[])

class Complaint(models.Model):
    _name = 'gsos.complaint'
    _inherit = ['mail.thread']
    _description = 'gsos.complaint'

    name = fields.Char(string='Name',
        help=None,
        readonly=False,
        required=False,
        groups=[],
        default='New')

    monitor = fields.Char(string='Monitor',
        help=None,
        readonly=False,
        required=True,
        groups=[])

    reason = fields.Text(string='Reason',
        help=None,
        readonly=False,
        required=True,
        groups=[],
        translate=False)

    severity_id = fields.Selection(
        selection=[
          ('low', 'Low'),
          ('medium', 'Medium'),
          ('high', 'High')
        ],
        string='Severity',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    supplier_id = fields.Many2one(comodel_name='gsos.supplier', string='Supplier',
        required=True,
        domain=None,
        context=None,
        ondelete=None)

    state = fields.Selection(
        selection=[
          ('open', 'Open'),
          ('closed', 'Closed')
        ],
        string='Status',
        help=None,
        readonly=False,
        required=False,
        groups=[],
        default='open')
