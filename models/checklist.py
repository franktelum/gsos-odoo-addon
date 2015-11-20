# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Checklist(models.Model):
    _name = "gsos.checklist"

    name = fields.Char(string='Name',
        size=100,
        required=True)

    checklist_template_url = fields.Char(string='Checklist File URL',
        help=None,
        readonly=False,
        required=True,
        groups=[])

    resolution_template_url = fields.Char(string='Resolution File URL',
        help=None,
        readonly=False,
        required=True,
        groups=[])
