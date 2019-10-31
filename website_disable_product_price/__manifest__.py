# -*- coding: utf-8 -*-
{
    'name': "Disable Product Price - Website",

    'summary': """
        Disable product price for users who not logged the system.""",

    'description': """
        This module deals with while the users who not logged the system can't see the product price.
    """,

    'author': "BroadTech",
    'website': "http://www.broadtech-innovations.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'website',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    'depends': ['website_sale'],

    # always loaded
    'data': [
        'views/templates.xml',
    ],
}