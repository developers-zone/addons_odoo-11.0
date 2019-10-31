# -*- coding: utf-8 -*-
{
    'name': "Minimum Products In Cart",

    'summary': """
        Each product has a minimum quantity to move in Cart.""",

    'description': """
        This module deals with managing minimum product quantity. 
        Each product has a minimum quantity and is defaults to 0 for that this is disabled.
        This is setup for product. Hence all variants will get apply the rule, if the field tends greater than 0.
    """,

    'author': "BroadTech",
    'website': "http://www.broadtech-innovations.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'website',
    'version': '12.0.1',


    # any module necessary for this one to work correctly
    'depends': ['website_sale','product'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
}