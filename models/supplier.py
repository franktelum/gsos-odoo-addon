# -*- coding: utf-8 -*-

from openerp import models, fields, api

class BusinessSector(models.Model):
    _name = 'gsos.business.sector'

    name = fields.Char(string='Name',
        help=None,
        readonly=False,
        required=True,
        groups=[])

class Supplier(models.Model):
    _name = 'gsos.supplier'

    name = fields.Char(related='partner_id.name',
        string='Name')

    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        ondelete=None)

    complaint_ids = fields.One2many(comodel_name='gsos.complaint',
        inverse_name='supplier_id',
        string='Complaints',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        auto_join=False)

    audit_ids = fields.One2many(comodel_name='gsos.audit',
        inverse_name='supplier_id',
        string='Audits',
        help=None,
        readonly=False,
        required=False,
        domain=None,
        context=None,
        auto_join=False)

    complaints_count = fields.Integer(compute='_complaints_count',
        string='Complaints Count')

    audits_count = fields.Integer(compute='_audits_count',
        string='Audits Count')

    def _complaints_count(self):
        for record in self:
            record.complaints_count = 0

    def _audits_count(self):
        for record in self:
            record.audits_count = 0
