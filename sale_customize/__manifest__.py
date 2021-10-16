# -*- coding: utf-8 -*-
{
    'name': "LEOFUMA S.A. - Sale Customize",

    'summary': """
        This module make Sale Customize""",

    'description': """
        This module make Sale Customize
    """,

    'author': "Ing. Leonel Fuentes Marrero",
    'website': "http://www.leofuma.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tool',
    'version': '1.1.3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_customize.xml',
        'views/lfm_widget.xml',
        'views/assets.xml',
    ],
    'application': True,
    'license': 'OPL-1',
}
