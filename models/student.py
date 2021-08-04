from odoo import api, fields, models, tools, _
import time
import datetime
from datetime import date
from datetime import datetime, date, time
from werkzeug.urls import url_encode


class UniStudent(models.Model):
    _name = "university.student"
    _description = "University Student"
    # _inherit = 'res.users'

    user_id = fields.Many2one('res.users', 'User', store=True, readonly=False)
    name = fields.Char(string='Name', required=True, translate=True)
    surname = fields.Char(string='Surname', required=True, translate=True)
    email = fields.Char(string='Email', required=True, translate=True)
    year = fields.Char(string='Year Enrolled', required=True)
    bday = fields.Date(string='Date of Birth', required=True)
    study = fields.Char(string='Field of Study', required=True, translate=True)
    course_ids = fields.Many2many('university.course', 'university_student_rel', 'student_ids',
                                  'course_ids', string="Courses")
    reference = fields.Char(string='Index Number', copy=False, readonly=True,
                            default=lambda self: _('New'))

    ocenki_id = fields.One2many('add.grades', 'ucenik_id', string="Grades")


    @api.model
    def create(self, vals):
        res = ""
        if vals.get('reference', 'New') == 'New':
            todays_date = date.today()
            rodenden = f"{self.env['ir.sequence'].next_by_code('student.sequence')}/{todays_date.year}"
            vals['reference'] = rodenden or 'New'
            res = super(UniStudent, self).create(vals)
        user = self.env['res.users'].create({
            'name': res.reference,
            'login': res.reference,
            'password': res.name,
            # 'groups_id': [(3, self.env.ref('om_odoo_university.university_student').id)],
            'sel_groups_1_9_0': 9,
        })
        return res

    @api.onchange('course_ids')
    def _on_change(self):
        for course in self.course_ids:
            kurs = self.env['university.course'].search([('name', '=', course.name)])
            ucenik = self.env['university.student'].search([('reference', '=', self.reference)])
            data = {
                'ucenik_id': ucenik.id,
                'kurs_id': kurs.id
            }
            self.env['add.grades'].sudo().create(data)

