# -*- coding: utf-8 -*-
from odoo import fields,models, api

class Enroll(models.TransientModel):
    _name = 'openacademy.enroll'

    enroll_attendee_ids = fields.One2many('enroll.attendee', 'enroll_id', string="Enroll Attendee")

    @api.one
    def action_enroll(self):
        attendee_object = self.env['openacademy.attendee']
        session_ids = self._context['active_ids']
        for session_id in session_ids:
            for attendee in self.enroll_attendee_ids:
                attendee_object.create({
                    'name': attendee.name,
                    'session_id': session_id,
                    'partner_id': attendee.partner_id.id,
                })
        return True

class EnrollAttendee(models.TransientModel):
    _name = 'enroll.attendee'
    _inherit =  'openacademy.attendee'

    enroll_id = fields.Many2one('openacademy.enroll', string="Enroll")




