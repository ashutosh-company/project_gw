/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, useState} from "@odoo/owl";
import { rpc } from "@web/core/network/rpc";


export class StockMovePopup extends Component {
    setup() {
        this.state = useState({
                stockMoves: [],
                total: 0,
                limit: 20,
                offset: 0,
                domain: this.props.action.params.domain || "[]",
            });
        this.loadData();
    }

    async loadData() {
        const result = await rpc("/api/v1/order-summary", {
            domain: this.state.domain,
            limit: this.state.limit,
            offset: this.state.offset,
        });
        this.state.stockMoves = result.stock_moves;
        this.state.total = result.total;
    }
    nextPage() {
        if (this.state.offset + this.state.limit < this.state.total) {
            this.state.offset += this.state.limit;
            this.loadData();
        }
    }

    prevPage() {
        if (this.state.offset - this.state.limit >= 0) {
            this.state.offset -= this.state.limit;
            this.loadData();
        }
    }

}

StockMovePopup.template = "project_gw.StockMovePopup";

registry.category("actions").add("project_gw.stock_move_popup", StockMovePopup);