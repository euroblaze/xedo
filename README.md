# XEDO – XML ERP Dataexchange for odoo

## Why XEDO?

odoo is a very powerful business-applications framework, with a robust, mature and stable data-model underneath, a powerful workflow engine and a modern UI. It is most often used as ERP, but it can be used for various other applications as well, for example as a data-bridge between existing ERP-Systems like SAP or Microsoft Navision and online-sales platforms likes Amazon or eBay.

It is too difficult (and expensive) to develop and maintain connectors among ERP-Systems, which odoo can successfully moderate as a middleware data-bridge.

## What is XEDO?

With XEDO, we aim to provide an open-sourced XML data-format specification to get data _into_ (imports) and _out of_ (exports) odoo. ERP-Systems which can deliver data according to the XEDO specification can expect it to be easily imported into odoo, and hence prepared to thereafter apply business-process to the data.

File-transfer takes place over simple FTP "letter-box", where structured `input` and `output` folders allow for data-exchange.

![XML Dataexchange for odoo](https://simplify-erp.com/web/image/27414-8f39408b/Simplify-ERP-Multichannel-E-Commerce.png)

## Reference XML for Commerce

### Reference product.xml

This is the initial XML structure for one product exchanged between random 3rd-party system (PIM, CMS etc) and odoo (random_system --> odoo):
https://github.com/euroblaze/xedo/blob/v1.0/product.xml

### Reference order.xml

This is the initial XML structure for one order exported from odoo (random_system -> odoo):
https://github.com/euroblaze/xedo/blob/v1.0/order.xml

`<foreign_erp_key>` is an optional node where the ID of the order in a connected ERP can be stored.

## Sponsor

Simplify-ERP®, inspired by its experiences in the E-Commerce industry initiated the development of XEDO, including the initial definitions of XML, and a reference implementation for E-Commerce companies.

Their products and services can be found at [simplify-erp.com/xedo](https://www.simplify-erp.com/)
