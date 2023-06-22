from odoo import api, fields, models

class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "Student regist"

    name = fields.Char(string='Нэр',required=True)
    age = fields.Integer(string='Нас')
    Eysh = fields.Boolean(string="ЭЕШ өгсөн эсэх")
    notes = fields.Text(string="Тэмдэглэл")
    gender = fields.Selection([('male','Эр'), ('female','Эм')], string="Хүйс")
