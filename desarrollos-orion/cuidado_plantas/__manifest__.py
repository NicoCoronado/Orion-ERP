# -*- coding: utf-8 -*-
{
    "name": """Cuidado de plantas""",
    "summary": """Este módulo sirve para gestionar el cuidado de plantas en Orion ERP""",
    "category": "Project",

    "version": "11.18.1.0.0",
    "description": """
        Conexión con API Fintoc
    """,
    "author": "Orion Soluciones SpA",
    "license": "OPL-1",
    "website": "http://www.orionsoluciones.cl",
    "support": "fernando.rios@orionsoluciones.cl",
    "depends": ["account"],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'views/vista.xml'
    ],
    "qweb": [],
    "demo": [],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "installable": True,
    "auto_install": False,
    "application": False,
}

