from odoo import models, fields, api
from odoo.tools.translate import _

class lcc(models.Model):
    _name = 'lcc_for_partners.lcc'
    _description = "Local Complementary Currency"

    id = fields.Integer(
        string=_("ID"),
        required=False,
        translate=False,
        readonly=True
    )
    create_date = fields.Datetime(
        string=_("Created on"),
        required=False,
        translate=False,
        readonly=True
    )
    create_uid = fields.Many2one(
        string=_("Created by"),
        required=False,
        translate=False,
        readonly=True
    )
    write_date = fields.Datetime(
        string=_("Last Updated on"),
        required=False,
        translate=False,
        readonly=True
    )
    write_uid = fields.Many2one(
        string=_("Last Updated by"),
        required=False,
        translate=False,
        readonly=True
    )
    __last_update = fields.Datetime(
        string=_("Last Modified on"),
        required=False,
        translate=False,
        readonly=True
    )



    name = fields.Char(
        string=_("Name"),
        required=True,
        translate=False,
        readonly=False
    )
    department = fields.Char(
        string=_("Department"),
        required=True,
        translate=False,
        readonly=False
    )
    creation_year = fields.Integer(
        string=_("Year of creation"),
        required=False,
        translate=False,
        readonly=False
    )    
    in_sol_movement = fields.Boolean(
        string=_("SOL Movement"),
        required=False,
        translate=False,
        readonly=False
    )