from xml import etree

from xlrd.xlsx import ET

from odoo import api, fields, models, tools
from odoo.http import request
from dateutil.relativedelta import relativedelta
from datetime import datetime


# from odoo.tools.safe_eval import datetime


class Courses(models.Model):
    _name = "university.course"
    _description = "University Course"
    _inherit = ["mail.thread"]

    name = fields.Char(string='Course Name', required=True, translate=True)
    field = fields.Char(string='Field of Study', required=True, translate=True)
    semestar = fields.Selection([('1', '1'),
                                 ('2', '2'),
                                 ('3', '3'),
                                 ('4', '4'),
                                 ('5', '5'),
                                 ('6', '6'),
                                 ('7', '7'),
                                 ('8', '8')], required=True)
    state = fields.Selection([('draft', 'Draft'),
                              ('open', 'Open'),
                              ('finished', 'Finished')], default='draft', string='Status')
    description = fields.Text(string='Description')
    begDate = fields.Date(string='Start of Course', required=True)
    teacher_id = fields.Many2one('university.teacher', string="Teacher")
    student_ids = fields.Many2many('university.student', 'university_student_rel', 'course_ids',
                                   'student_ids', string="Students")
    endDate = fields.Date(string='End of Course', copy=False)

    grades = fields.One2many('add.grades', 'kurs_id', string="Grades")

    documents = fields.Many2many('ir.attachment', 'class_ir_attachments_rel', 'class_id', 'attachment_id', 'Documents')
    document_name = fields.Char(string="File Name")

    def action_copy(self):
        return

    def action_open(self):
        self.state = 'open'
        context = self._context

    def action_grades(self):
        return

    def action_finish(self):
        self.state = 'finished'

    @api.onchange('student_ids')
    def _check_courses(self):
        for course in self:
            if not self.student_ids:
                print("Posledniot student e otstranet")
            else:
                ucenik = self.env['university.student'].search([('reference', '=', self.student_ids[-1].reference)])
                data = {
                    'ucenik_id': ucenik.id,
                    'kurs_id': self.id
                }
                flag = 0
                for grade in course.grades:
                    if grade.ucenik_id.id == ucenik.id:
                        flag = 1
                if flag == 0:
                    self.env['add.grades'].sudo().create(data)


    @api.onchange('begDate')
    def _check_change(self):
        if self.begDate:
            date_1 = self.begDate + relativedelta(years=+ 1)
            self.endDate = date_1

    # @api.onchange('student_ids')
    # def _check_courses(self):
    #     flag = 0
    #     course = self.env['university.course'].search([('name', '=', self.name)])
    #     student = self.env['university.student'].search([('reference', '=', self.student_ids.reference)])
    #     for grade in self.grades:
    #         if grade.ucenik_id and grade.ucenik_id.id == student.id:
    #             flag = 1
    #     if flag == 0:
    #         data = {
    #             'ucenik_id': student.id,
    #             'kurs_id': self.id
    #         }
    #         print('data...', data)
    #         self.env['add.grades'].sudo().create(data)
