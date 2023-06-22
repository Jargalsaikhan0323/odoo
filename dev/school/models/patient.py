from odoo import api, fields, models

class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "school.student"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string="Age")
    is_child = fields.Boolean(string="эеш өгсөн эсэх")
    notes = fields.Text(string="Notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender")