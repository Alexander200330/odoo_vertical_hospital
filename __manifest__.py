# -*- coding: utf-8 -*-
{
    'name': "odoo_vertical_hospital",

    'summary': """
        Aplicación para gestión hospitalaria que incluye registro de pacientes, generación de reportes en PDF,
        web service para consultas de pacientes y auditoría de modificaciones de datos.
    """,

    'description': """
        Esta aplicación está diseñada para simplificar la gestión hospitalaria. 
        Ofrece las siguientes funciones principales:

        - Registro de Pacientes: Agregar, actualizar y eliminar información de pacientes de manera sencilla.
        
        - Reportes en PDF: Genera informes detallados sobre los pacientes en formato PDF para compartir fácilmente.
        
        - Consulta de Pacientes vía Web: Permite acceder a la información de pacientes a través de un servicio web.
        
        - Auditoría de Modificaciones: Registra cambios importantes en los datos para garantizar la seguridad y 
        la integridad de la información.

        Esta solución ayuda a hospitales a gestionar eficientemente su información, 
        asegurando una atención médica de calidad y una administración efectiva.
    """,

    'author': "Alexander Ventura",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/view_patient.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/icon.png'],
}
