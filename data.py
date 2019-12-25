import datetime


def get_data():
    data = {
        'current_day': datetime.datetime.today().weekday(),
        'premier': {
            'horaires': {
                'mardi': [10, 19],
                'mercredi': [10, 19],
                'jeudi': [13, 19],
                'vendredi': [13, 19],
                'samedi': [14, 18]
            },
            'address': '7 rue Saint Polycarpe 69001 Lyon'
        },
        'deuxième': {
            'horaires': {
                'mardi': [13, 19],
                'mercredi': [10, 19],
                'jeudi': [13, 19],
                'vendredi': [13, 19],
                'samedi': [10, 18]
            },
            'address': '13 rue de Condé 69002 Lyon'
        },
        'troisième': {
            'horaires': {
                'mardi': [10, 19],
                'mercredi': [10, 19],
                'jeudi': [10, 19],
                'vendredi': [10, 19],
                'samedi': [10, 18]
            },
            'address': '30 boulevard Vivier-Merle 69003 Lyon'
        },
        'quatrième': {
            'horaires': {
                'mardi': [13, 19],
                'mercredi': [10, 19],
                'jeudi': [13, 19],
                'vendredi': [13, 19],
                'samedi': [10, 18]
            },
            'address': '12 bis rue de Cuire 69004 Lyon'
        },
        'cinquième': {
            'horaires': {
                'mardi': [10, 19],
                'mercredi': [10, 19],
                'jeudi': [13, 19],
                'vendredi': [13, 19],
                'samedi': [10, 17]
            },
            'address': '4 avenue Adolphe Max 69005 Lyon'
        },
        'sixième': {
            'horaires': {
                'mardi': [13, 19],
                'mercredi': [10, 19],
                'jeudi': [13, 19],
                'vendredi': [13, 19],
                'samedi': [10, 18]
            },
            'address': '35 rue Bossuet 69006 Lyon'
        },
        'septième': {
            'horaires': {
                'mardi': [13, 19],
                'mercredi': [10, 19],
                'jeudi': [13, 19],
                'vendredi': [13, 19],
                'samedi': [10, 18]
            },
            'address': '2 rue Domer 69007 Lyon'
        },
        'huitième': {
            'horaires': {
                'mardi': [13, 19],
                'mercredi': [10, 19],
                'jeudi': [13, 19],
                'vendredi': [12, 19],
                'samedi': [10, 18]
            },
            'address': '2 place du 11 novembre 1918 69008 Lyon'
        },
        'neuvième': {
            'horaires': {
                'mardi': [10, 19],
                'mercredi': [10, 19],
                'jeudi': [14, 19],
                'vendredi': [14, 19],
                'samedi': [10, 18]
            },
            'address': 'place Valmy 69009 Lyon'
        }
    }
    return data

