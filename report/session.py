# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
from odoo.osv import osv
from odoo.report import report_sxw


class SessionParser(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(SessionParser, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'hello': self._getHello(),
        })

    def _getHello(self):
        msg = ' World'
        return msg

class SessionReport(osv.AbstractModel):
    _name = 'report.openacademy.session_template'
    _inherit = 'report.abstract_report'
    _template = 'openacademy.session_template'
    _wrapped_report_class = SessionParser



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
