"""
ntm - Our Opal Application
"""
from opal.core import application

class Application(application.OpalApplication):
    javascripts = [
        'js/ntm/routes.js',
        'js/opal/controllers/discharge.js',
        'js/ntm/controllers/add_ntm_patient.js',
        # Uncomment this if you want to implement custom dynamic flows.
        # 'js/ntm/flow.js',
    ]
