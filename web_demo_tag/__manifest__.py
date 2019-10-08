# -*- coding: utf-8 -*-
{
    'name': "Demo Server Tag",

    'summary': """
        Marking the web pages with Demo Server tag""",

    'description': """
        Tags for Demo Server to notify.
    """,

    'author': "BroadTech",
    'website': "http://www.broadtech-innovations.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Administration',
    'version': '11.0.1',

    # any module necessary for this one to work correctly
    'depends': ['web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'data/data.xml',
    ],
}