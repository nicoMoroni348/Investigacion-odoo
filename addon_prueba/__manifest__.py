{
    'name': 'addon_prueba',
    'version': '1.0.0',
    'category': 'Sin Categoría',
    'sequence': -1500, # así aparece primero, también pone lo del application true
    'author': 'nico',
    'application': True,
    'summary': 'Este es mi primer addon',
    'description': 'Este es mi primer addon',
    'depends': ['mail',
                'phone_validation',
                'product',
                ],
    'data': [
        'security/ir.model.access.csv',
        'data/persona_tag_data.xml',
        'data/persona.tag.csv',
        'wizard/cancelar_oportunidad_view.xml',
        'views/menu.xml',
        'views/persona_view.xml',
        'views/persona_tag_view.xml',
        'views/oportunidad_view.xml',
        'views/persona_mujer_view.xml',
        'report/oportunidad_report.xml',
        'report/oportunidad_template.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',  # Esta es la que viene por defecto

}