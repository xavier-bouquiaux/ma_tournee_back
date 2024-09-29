# Copyright 2023 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "matournee",
    "description": """
        Odoo aplication for matournee""",
    "author": "ACSONE SA/NV",
    "website": "https://acsone.eu",
    "category": "matournee",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "depends": [
        # matournee open source addons
        # !!! no odoo enterprise addons dependencies !!!
        # OCA
        "mail_environment",
        "server_environment_ir_config_parameter",
        "web_environment_ribbon",
        "mat_fs_attachment",
    ],
    "data": [],
    "application": True,
}
