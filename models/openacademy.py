# -*- coding: utf-8 -*-
from datetime import timedelta, datetime

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class OpenacademyCourse(models.Model):
    _name = 'openacademy.course'
    _description = 'Course Class'

    name = fields.Char("Title", required=True)
    description = fields.Text('Description')
    session_ids = fields.One2many('openacademy.session', 'course_id', 'Session')
    responsible_id = fields.Many2one('res.users', 'Responsible')

    _sql_constraints = [('name_check', 'check(name!=description)',
                         'The name and description must be different!'),
                        ('name_uniq', 'unique(name)',
                         'The name must be unique!')]

    @api.one
    def copy(self, default=None):
        if default is None:
            default = {}
        default['name'] = self.name + '(copy)'
        return super(OpenacademyCourse, self).copy(default)


class OpenacademySession(models.Model):
    _name = 'openacademy.session'
    _description = ''

    name = fields.Char("Name", required=True)
    duration = fields.Float("Duration")
    seats = fields.Integer("Seats")
    start_date = fields.Date("Start Date", default=datetime.now())
    course_id = fields.Many2one('openacademy.course', 'Course')
    attendee_ids = fields.One2many('openacademy.attendee', 'session_id', 'Attendee')
    instructor_id = fields.Many2one('res.partner', 'Instructor',
                                    domain=['|', ('is_instructor', '=', True),
                                            ('category_id.name', 'in', ['nivel1', 'nivel2'])])
    attendee_count = fields.Integer('Attendee Count', compute='_compute_attendee_count', store=True)
    remaining_seats = fields.Float('Remaining Seats', compute='_compute_remaining_seats')
    end_date = fields.Date('End Date', compute='_compute_end_date', inverse='_inverse_end_date')
    state = fields.Selection([('draft', 'Draft'),
                              ('confirmed', 'Confirmed'),
                              ('done', 'Done')], string='State', readonly=True)
    color = fields.Integer('Color')

    @api.onchange('seats', 'attendee_ids')
    def _onchange_seats(self):
        """
        WARNING IF THE NUMBER OF THE SEATS ARE LESS THAN 0
        :return:
        """
        if self.seats < 0:
            return {
                'warning': {
                    'title': _("Warning!"),
                    'message': 'Check the seat number out!'
                }
            }
        if len(self.attendee_ids) > self.seats:
            return {
                'warning': {
                    'title': _("Warning!"),
                    'message': 'The number attendee must be less or equals than the number seats!'
                }
            }



    @api.one
    @api.depends('attendee_ids')
    def _compute_attendee_count(self):
        self.attendee_count = len(self.attendee_ids)

    @api.one
    @api.depends('attendee_ids', 'seats')
    def _compute_remaining_seats(self):
        self.remaining_seats = 100 - (self.seats and len(self.attendee_ids) * 100 / self.seats)

    @api.one
    @api.depends('duration', 'start_date')
    def _compute_end_date(self):
        start = datetime.strptime(self.start_date, '%Y-%m-%d')
        durat = timedelta(days=self.duration - 1)
        end = start + durat
        self.end_date = end.strftime('%Y-%m-%d')

    @api.one
    def _inverse_end_date(self):
        end = datetime.strptime(self.end_date, '%Y-%m-%d')
        start = datetime.strptime(self.start_date, '%Y-%m-%d')
        if start > end:
            raise ValidationError('Wrong start date')
        self.duration = (end - start).days + 1

    @api.multi
    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_attendee(self):
        for session in self:
            if session.instructor_id in session.attendee_ids.mapped('partner_id'):
                raise ValidationError('The instructor does not be an attende')

    @api.one
    def action_draft(self):
        self.state = 'draft'

    @api.one
    def action_confirm(self):
        self.state = 'confirmed'

    @api.one
    def action_done(self):
        self.state = 'done'


class OpenacademyAttendee(models.Model):
    _name = 'openacademy.attendee'
    _description = ''

    name = fields.Char("Code", required=True)
    session_id = fields.Many2one('openacademy.session', 'Session')
    partner_id = fields.Many2one('res.partner', 'Partner')









