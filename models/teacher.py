from odoo import api, fields, models, tools




class UniTeacher(models.Model):
    _name = "university.teacher"
    _description = "University Teacher"

    name = fields.Char(string='Name', required=True, translate=True)
    surname = fields.Char(string='Surname', required=True, translate=True)
    email = fields.Char(string='Email', required=True, translate=True)
    course_id = fields.One2many('university.course', 'teacher_id', string="Courses")
