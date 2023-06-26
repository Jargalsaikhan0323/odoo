from odoo import api, fields, models

class SchoolTeacher(models.Model):
    _name = "school.teacher"
    _description = "Teacher regist"

    name = fields.Char(string='Нэр',required=True)
    age = fields.Integer(string='Нас')
    child = fields.Boolean(string="Хүүхэдтэй эсэх")
    notes = fields.Text(string="Тэмдэглэл")
    gender = fields.Selection([('male','Эр'), ('female','Эм')], string="Хүйс")
