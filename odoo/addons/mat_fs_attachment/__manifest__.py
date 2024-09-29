# Copyright 2023 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "matournee Fs Attachment",
    "description": """
        Filestore configurations""",
    "author": "ACSONE SA/NV",
    "website": "https://acsone.eu",
    "category": "matournee",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "depends": [
        "fs_attachment",
    ],
    "external_dependencies": {
        "python": [
            "s3fs",
        ]
    },
    "data": [
        "data/fs_storage.xml",
    ],
}
