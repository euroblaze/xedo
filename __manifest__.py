# -*- coding: utf-8 -*-
{
    'name': "EB XEDO",

    'summary': """
       Standardized XEDO (XML ERP DATA EXCHANGE FOR ODOO) IMPORT EXPORT""",

    'description': """
       Standardized XEDO (XML ERP DATA EXCHANGE FOR ODOO) IMPORT EXPORT
    """,

    'author': "odoo@simplify-erp.com",
    'website': "http://www.simplify-erp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}