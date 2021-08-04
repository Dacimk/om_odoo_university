from stdnum.at import uid
from stdnum.cr import cr

from odoo import models, fields, api, _


class AddGrades(models.Model):
    _name = "add.grades"
    _description = "Addition of grades"

    # student_id = fields.Many2one('university.student', string='Student')
    # ^^^^^^^^^^Ova ide kon university.student, nas ni treba studenti vo kurost
    # many2one kon courses, many2one kon student da bide computed/onChange sho gi racuna studentite na kursot ili False
    # view vo edna linija ocenka i student / od courses one2many, tree view, prvo Strudent, Ocenka
    # vo view so notebook pages

    kurs_id = fields.Many2one('university.course', string='Course')
    ucenik_id = fields.Many2one('university.student', string='Student')

    grade = fields.Selection([('5', '5'),
                              ('6', '6'),
                              ('7', '7'),
                              ('8', '8'),
                              ('9', '9'),
                              ('10', '10')])

    @api.onchange('kurs_id.student_ids')
    def _change_students(self):
        print("Vidov deka se smeni")