# XEDO – XML ERP Dataexchange for odoo

## Why XEDO?

odoo is a very powerful business-applications framework, with a robust, mature and stable data-model underneath, a powerful workflow engine and a modern UI. It is most often used as ERP, but it can be used for various other applications as well, for example as a data-bridge between existing ERP-Systems like SAP or Microsoft Navision and online-sales platforms likes Amazon or eBay.

It is too difficult (and expensive) to develop and maintain connectors among ERP-Systems, which odoo can successfully moderate as a middleware data-bridge.

## What is XEDO?

With XEDO, we aim to provide an open-sourced XML data-format specification to get data _into_ (imports) and _out of_ (exports) odoo. ERP-Systems which can deliver data according to the XEDO specification can expect it to be easily imported into odoo, and hence prepared to thereafter apply business-process to the data.

File-transfer takes place over simple FTP "letter-box", where structured `input` and `output` folders allow for data-exchange.

## Reference XML for Commerce

### Simplest Product-XML

This is the initial XML structure for one product imported into odoo:
```
<Product>
<item>
<available>1</available>
<isbn/>
<name>ARMANI 06235 V8 12</name>
<price>179.95</price>
<barcode>False</barcode>
<description>
ARMANI 06235 V8 12ARMANI JEANS06235 V8 12 Laptoptasche Farbe: SchwarzMetall ARMANI JEANS Logo1 Reißverschlussfach innen B 34cm x H 26cm x T11cm2 Steckfächer innenein HandyfachRaumteiler, <strong>TrennwandSchultergurt</strong> (Länge ca.80-120cm)in der Hand tragbar, über Schulter <span class="font-color: red;">tragbar</span>
</description>
<cost>0.0</cost>
<internal_reference>2899022604710</internal_reference>
<stock>1.0</stock>
</item>
</Product>
```
### Simplest Order-XML (order.xml)

This is the initial XML structure for one order exported from odoo:
https://github.com/euroblaze/xedo/blob/v1.0/order.xml

## Sponsor

Simplify-ERP, inspired by it's experiences in the E-Commerce industry initiated the development of XEDO, including the initial definitions of XML, and a reference implementation for E-Commerce companies.

Their products can be found at [simplify-erp.com/xedo](https://www.simplify-erp.com/odoo-komplettloesungen/e-commerce/xedo-xml-erp-data-exchange-mit-odoo/)
