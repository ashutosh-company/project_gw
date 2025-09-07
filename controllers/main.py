import ast

from odoo import http
from odoo.http import request

class StockMovesAPI(http.Controller):
    @http.route('/api/v1/order-summary', type="json", auth="public")
    def get_stock_moves(self, domain="[]", limit=50, offset=0, **kwargs):
        safe_domain = []
        if domain:
            try:
                safe_domain = ast.literal_eval(domain)
                if not isinstance(safe_domain, list):
                    safe_domain=[]

            except Exception:
                safe_domain = []
                

        # stock_moves = request.env["stock.move"].sudo().search(safe_domain)

        # stock_moves = request.env["stock.move"].sudo().search_read(safe_domain, ["id","name", "product_id", "state"])

        StockMove = request.env["stock.move"].sudo()

        total_count = StockMove.search_count(safe_domain)
        stock_moves = StockMove.search_read(
            safe_domain,
            ["id", "name", "product_id", "product_uom_qty", "state", "reference"],
            offset=int(offset),
            limit=int(limit),
        )

        for move in stock_moves:
            move["product"] = move["product_id"][1] if move.get("product_id") else ""
            move.pop("product_id", None)

        return {
            "total": total_count,
            "limit": limit,
            "offset": offset,
            "stock_moves": stock_moves,
        }