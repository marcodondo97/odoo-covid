{
    'name': "Covid-19 italian region",
    'summary': "Import and display updated SARS-CoV-2 data by Italian region",
    'version': '1.0.1',
    'author': 'Marco Dondo',
    'website': 'https://github.com/marcodondo97/odoo-covid',
    'category': 'Health',
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
    'depends': ['base'],
    'data': [
        'views/covid_region_views.xml',
        'security/ir.model.access.csv',
    ],
    'images': [
        'static/description/icon.png',
    ],
    'external_dependencies': {
        'python': ['requests'],
    },
    'description': """
Odoo module to import and display up-to-date COVID-19 data for Italian regions.
Includes dynamic date search and aggregated data views.
    """,
}
