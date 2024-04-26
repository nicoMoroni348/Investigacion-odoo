{
    'name': 'addon_prueba',
    'version': '1.0.0',
    'category': 'Sin Categoría',
    'sequence': -1500, # así aparece primero, también pone lo del application true
    'author': 'nico',
    'application': True,
    'summary': 'Este es mi primer addon',
    'description': 'Este es mi primer addon',
    'depends': ['mail','phone_validation',],  # Por ahora no depende de ningún módulo externo
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/persona_view.xml',
        'views/oportunidad_view.xml',
        'views/persona_mujer_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',  # Esta es la que viene por defecto

}