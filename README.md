# XEDO – XML ERP Dataexchange for odoo

## Why?

odoo is a very powerful business-applications framework, with a robust, mature and stable data-model underneath. It is most often used as ERP, but it can be used for various other applications as well, for example as a data-bridge between existing ERP-Systems like SAP or Microsoft Navision and online-sales platforms likes Amazon or eBay.

It is too difficult (and expensive) to develop and maintain connectors among ERP-Systems, which odoo can successfully moderate as a middleware data-bridge.

## What

With XEDO, we aim to provide an open-sourced data-format specification to get data **into** odoo. ERP-Systems which can deliver data according to the XEDO specification can expect it to be easily imported into odoo, and hence prepared for thereafter applying business-process to the data.

File-transfer takes place over simple FTP "letter-box", where structured `input` and `output` folders allow for data-exchange.
