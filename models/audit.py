# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Audit(models.Model):
    _name = 'gsos.audit'
    _inherit = ['mail.thread']
    _description = 'gsos.audit'

    name = fields.Char(string='Name',
        help=None,
        readonly=False,
        required=False,
        groups=[],
        default='New')

    supplier_id = fields.Many2one(comodel_name='gsos.supplier', string='Supplier',
        required=True,
        domain=None,
        context=None,
        ondelete=None)

    checklist_id = fields.Many2one(comodel_name='gsos.checklist', string='Checklist',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        ondelete=None)

    date_start = fields.Date(string='Start Date',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    resolution_score = fields.Integer(string='Score',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    resolution_file_url = fields.Char(string='Resolution',
        help=None,
        readonly=False,
        required=False,
        groups=[])

    state = fields.Selection(
        selection=[
          ('draft', 'Draft'),
          ('sent', 'Sent'),
          ('scheduled', 'Scheduled'),
          ('cancelled', 'Cancelled'),
          ('done', 'Done')
        ],
        string='State',
        help=None,
        readonly=False,
        required=False,
        groups=[],
        default='draft')

    @api.multi
    def action_audit_send(self):
        self.ensure_one()
        self.state = 'sent'
        return True
