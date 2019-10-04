# -*- coding: utf-8 -*-
{
    'name': "Record Authenticate By User",

    'summary': """
        Validates the user before gets saving the record""",

    'description': """
        A popup window will appear to validate the user before gets saving the record. And you can 
        configure the models in user interface.
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
        'views/config_views.xml',
    ],
}