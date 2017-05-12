# XEDO – XML ERP Dataexchange for odoo

## Why XEDO?

odoo is a very powerful business-applications framework, with a robust, mature and stable data-model underneath, a powerful workflow engine and a modern UI. It is most often used as ERP, but it can be used for various other applications as well, for example as a data-bridge between existing ERP-Systems like SAP or Microsoft Navision and online-sales platforms likes Amazon or eBay.

It is too difficult (and expensive) to develop and maintain connectors among ERP-Systems, which odoo can successfully moderate as a middleware data-bridge.

## What is XEDO?

With XEDO, we aim to provide an open-sourced XML data-format specification to get data _into_ (imports) and _out of_ (exports) odoo. ERP-Systems which can deliver data according to the XEDO specification can expect it to be easily imported into odoo, and hence prepared to thereafter apply business-process to the data.

File-transfer takes place over simple FTP "letter-box", where structured `input` and `output` folders allow for data-exchange.

# This is the initial XML structure for one product exported from odoo:
```
<Product>
<item>
<available>1</available>
<isbn/>
<name>ARMANI 06235 V8 12</name>
<price>179.95</price>
<barcode>False</barcode>
<description><strong>ARMANI 06235 V8 12</strong><br /><h1>ARMANI JEANS</h1><h1>06235 V8 12</h1><p><b>Laptoptasche<br /></b></p><p>Farbe: Schwarz<br /></p><p>Metall ARMANI JEANS Logo<br /></p><p>1 Reißverschlussfach innen <br /></p><p>B 34cm x H 26cm x T11cm</p><p>2 Steckfächer innen<br /></p><p>ein Handyfach</p><p>Raumteiler,Trennwand</p><p>Schultergurt (Länge ca.80-120cm)</p><p>in der Hand tragbar, über Schulter tragbar<span><span><br /></span></span></p><p> </p></description>
<cost>0.0</cost>
<internal_reference>2899022604710</internal_reference>
<stock>1.0</stock>
</item>
</Product>
```
# This is the initial XML structure for one order (without products) exported from odoo:
```
<Order>
<item>
<status>invoiced</status>
<amount_untaxed>212.74</amount_untaxed>
<name>SO1021</name>
<confirmation_date>2017-05-11 12:15:37</confirmation_date>
<order_id>1021</order_id>
<amount_tax>39.11</amount_tax>
<partner_name>Janosh Umpelkirch</partner_name>
<partner_id>11054</partner_id>
<amount_total>251.85</amount_total>
</item>
</Order>
```
## We extend and keep the structure of product with <item>