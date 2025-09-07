# -*- coding: utf-8 -*-
{
    "name": "Project for GW",
    "version": "1.0",
    "category": "Custom",
    "summary": "",
    "depends": ["web", "stock", "bus"],
    "data": [
        "views/order_summary_template.xml",
        "security/ir.model.access.csv",
    ],
    "assets": {
        "web.assets_backend": [
            "project_gw/static/src/js/order_summary_service.js",
            "project_gw/static/src/js/order_summary_service.xml",
        ],
    },
    "installable": True,
    "application": True,
}
