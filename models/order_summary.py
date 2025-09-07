import requests
from odoo import models, fields


import logging
_logger = logging.getLogger(__name__)

class OrderSummary(models.Model):
    _name = "order.summary"
    _description="Order Summary Model"

    domain = fields.Char("User Custom Domain")

    def action_show_filtered_stock_moves(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        url = f"{base_url}/api/v1/order-summary"

        user_domain = self.domain or "[]"

        payload = {
            "jsonrpc": "2.0",
            "method": "call",
            "params": {"domain": user_domain},
            "id": 1,
        }

        response = requests.post(url, json=payload)
        _logger.info(f"\n\n=============Response==============={response}")
        data = response.json()
        stocks_moves = data.get("result", {}).get("stock_moves", [])

        return{
            "type": "ir.actions.client",
            "tag": "project_gw.stock_move_popup",
            "params": {
                "stock_moves": stocks_moves
            },
            "target": "new",
        }