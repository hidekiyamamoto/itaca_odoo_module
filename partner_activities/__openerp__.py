# -*- coding: utf-8 -*-
{
    'name': "Partner Activities",

    'summary': """
        Partner 2 Partner activities""",

    'description': """
        This is a module to provide activity tracking between partner.
    """,

    'author': "Hideki Andrea Yamamoto",
    'website': "http://metaschema.io",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}