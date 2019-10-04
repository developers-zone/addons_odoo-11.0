# -*- coding: utf-8 -*-
{
    'name': "Web Database Backup",

    'summary': """
        Database Backup From Web""",

    'description': """
        This is an option to take database backup from web and configure the file path also.
    """,

    'author': "BroadTech",
    'website': "http://www.broadtech-innovations.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Administration',
    'version': '11.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/db_config_views.xml',
    ],
}