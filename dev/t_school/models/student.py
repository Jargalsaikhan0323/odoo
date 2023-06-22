from odoo import api, fields, models

class SchoolStudent(models.Model):
    _name = "school.student"

    name = fields.Char(string='Нэр',required=True)