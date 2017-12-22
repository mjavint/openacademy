{
    'name': "Open Academy",

    'summary': """
        """,

    'description': """

    """,

    'author': "desoft",
    'website': "http://www.desoft.cu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Open Academy',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/group.xml',
        'security/ir.model.access.csv',
        'views/openacademy_view.xml',
        'views/partner_view.xml',
        'wizard/enroll_wizard.xml',
        'workflow/openacademy_workflow.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# -*- coding: utf-8 -*-
