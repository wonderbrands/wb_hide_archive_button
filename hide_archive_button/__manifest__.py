{
    "name": "Hide Action Archive Button",
    "summary": "Hide Action Archive Button",
    "version": "1.0.4",
    "description": """Hide Action Archive Button""",
    "author": "Sergio Guerrero",
    "category": "Extra Tools",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": ["views/groups.xml"],
    "assets": {
        "web.assets_backend": [
            "hide_archive_button/static/src/**/*",
        ]
    },
    "installable": True,
    "auto_install": False,
    "application": True,
    "images": [
        'icon.png',
    ],
}
