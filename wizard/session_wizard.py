# -*- coding: utf-8 -*-
from odoo import fields,models, api, _

class SessionWizard(models.TransientModel):
    _name = 'openacademy.session.report'

    session_report_ids = fields.Many2many('openacademy.session', 'session_report_sessions_rel', string="Sessions")

    @api.multi
    def print_session_report(self):
        """
        creando un action de tipo ir.actions.report.xml que genere el reporte pasandole los ids de las sesiones seleccionadas en el wizard
        :return:
        """
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'openacademy.session_template',
            'datas': {
                'ids': self.session_report_ids.ids
            },
        }






