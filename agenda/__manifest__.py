# -*- coding: utf-8 -*-
# Es el que busca odoo para ver que es un nuevo modulo
# Formato fichero clave:valor
{
    'name': "Agenda",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # modulos necesarios para ejecutar nuesto modulo
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # Archivos que vamos a utilizar y que no sean extensión .py
    # Descomentamos la linea security/ir.model.access.csv
    # Comento la linea views/templates.xml
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

