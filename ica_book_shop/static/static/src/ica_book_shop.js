/** @odoo-module **/

import { registry } from "@web/core/registry";

import { Component } from  "@odoo/owl";

class IcaBookShop extends Component {}
IcaBookShop.template = "ica_bookshop.IcaBookShop";

// remember the tag name we put in the first step
registry.category("actions").add("ica_bookshop.IcaBookShop", IcaBookShop);