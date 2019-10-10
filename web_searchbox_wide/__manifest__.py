# -*- coding: utf-8 -*-
{
    'name': "SearchBox Wide",

    'summary': """
        Widens the search filter box""",

    'description': """
        Widens the search filter box
    """,

    'author': "BroadTech",
    'website': "http://www.broadtech-innovations.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Administration',
    'version': '11.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/templates.xml',
    ],
}