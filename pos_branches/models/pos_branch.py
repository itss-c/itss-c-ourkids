# -*- coding: utf-8 -*-
""" init object """
from odoo import fields, models


class PosBranch(models.Model):
    _name = 'pos.branch'
    _rec_name = 'name'

    name = fields.Char(string="Name", required=False, )
