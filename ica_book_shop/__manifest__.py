{
    "name": "Book Shop",
    "author": "IdeaCode Academy",
    "license": "LGPL-3",
    "depends": ["base", "web", "contacts", "web_hierarchy"],
    "data": [
        "data/sequence.xml",
        "data/server_action.xml",

        "security/groups.xml",
        "security/ir_rule.xml",
        "security/ir.model.access.csv",
        "views/ica_books_order.xml",

        "views/res_partner.xml",
        "views/ica_book_category.xml",
        "views/ica_books.xml",
        "views/client_action.xml",

        "wizard/book_order_wizard.xml",
        "views/res_config_settings.xml",

        "views/menus.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "ica_book_shop/static/static/src/ica_book_shop.js",
            "ica_book_shop/static/static/src/ica_book_shop.xml"
        ]
    }
}
