# -*- coding: utf-8 -*-
{
    'name': "Realtor",

    'summary': """
    Apartment sales
            """,

    'description': """    
    """,

    'author': "Oumar Magomadov & Yacine Mamlouk",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],

    'application' : True, 
}