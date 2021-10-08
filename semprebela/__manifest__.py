# -*- coding: utf-8 -*-
{
    'name': "LEOFUMA S.A. - SPA Sempre Bela",

    'summary': """
        This module make every change to module Inventory and Appoinment""",

    'description': """
        This module make every change to module Inventory and Appoinment
    """,

    'author': "Ing. Leonel Fuentes Marrero",
    'website': "http://www.leofuma.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Clinica',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'website', 'calendar', 'contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/leofuma_state_views.xml',
        'views/leofuma_menu_views.xml',
        'views/lfm_calendar_event_view.xml',
    ],
    'auto_install': False,
}
