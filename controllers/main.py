from odoo import http
from odoo.http import request



class University(http.Controller):

    @http.route('/student/', website=True, auth='public')
    def university_student(self, **kw):
        # return "hello world"
        # target = request.env['university.student'].sudo().search([('reference', '=', '041/2020')]) # So ova da vidam koj e logiran
        logged = request.env.user
        if logged.name == 'OdooBot':
            target = request.env['university.student'].sudo().search([('reference', '=', '124/2021')])
        else:
            target = request.env['university.student'].sudo().search([('reference', '=', logged.name)])
        state = ([('done', 'Done'),
                  ('edit', 'Edit')])
        state = 'done'
        print('STUDENT gleda', kw)
        return request.render('om_odoo_university.students_page', {
            'target_student': target,
            'state': state,
        })

    @http.route('/student/editing', website=True, auth='public')
    def university_student_edit_(self, **kw):
        state = ([('done', 'Done'),
                  ('edit', 'Edit')])
        print('EDITING gleda', kw)
        # target = request.env['university.student'].sudo().search([('reference', '=', '041/2020')])
        logged = request.env.user
        if logged.name == 'OdooBot':
            target = request.env['university.student'].sudo().search([('reference', '=', '124/2021')])
        else:
            target = request.env['university.student'].sudo().search([('reference', '=', logged.name)])
        state = 'edit'
        return request.render('om_odoo_university.students_page', {
            'target_student': target,
            'state': state,
        })

    @http.route('/student_save_changes', type='http', methods=['POST'], auth="public", website=True, csrf=False)
    def university_student_save(self, **kw):
        # print(kw['student_name'])
        state = ([('done', 'Done'),
                  ('edit', 'Edit')])
        # target = request.env['university.student'].sudo().search([('reference', '=', '041/2020')])
        logged = request.env.user
        if logged.name == 'OdooBot':
            target = request.env['university.student'].sudo().search([('reference', '=', '124/2021')])
        else:
            target = request.env['university.student'].sudo().search([('reference', '=', logged.name)])
        state = 'done'
        print('SAVE CHANGES gleda', kw)
        if kw:
            target.sudo().write(kw)
        return request.render('om_odoo_university.students_page', {
            'target_student': target,
            'state': state,
        })

    @http.route('/student/print', type='http', auth="public", website=True)
    def university_student_print(self, **kw):

        # target = request.env['university.student'].sudo().search([('reference', '=', '041/2020')])
        logged = request.env.user
        if logged.name == 'OdooBot':
            target = request.env['university.student'].sudo().search([('reference', '=', '124/2021')])
        else:
            target = request.env['university.student'].sudo().search([('reference', '=', logged.name)])
        print("SEGA KJE PRINTAME")
        # pdf = request.env['reports'].sudo().get_pdf([target.id], 'reports.report_student', data=None)
        # pdfhttpheaders = [('Content-Type', 'application/pdf'), ('Content-Length', len(pdf))]
        # return request.make_response(pdf, headers=pdfhttpheaders)

    @http.route('/student/courses', type='http', auth='public', website=True)
    def university_student_courses(self, **kw):
        logged = request.env.user
        if logged.name == 'OdooBot':
            target = request.env['university.student'].sudo().search([('reference', '=', '124/2021')])
        else:
            target = request.env['university.student'].sudo().search([('reference', '=', logged.name)])
        dokumenti = []
        for course in target.course_ids:
            for document in course.documents:
                if document:
                    print(document)
                    dokumenti.append(document)
                else:
                    break
        for dokument in dokumenti:
            print(dokument.name)

        return request.render('om_odoo_university.students_page_courses', {
                'target_student': target,
                'documents': dokumenti
        })







