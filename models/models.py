# -*- coding: utf-8 -*-

from odoo import models, fields, api

In the models we need to define three functions for import and three for export.
There will be re-usable defs that will collect the data from a SINGLE record from the model 
Then after taking the values from the fields, the values will be appended to a dict()
The dict() will be transformed into an XML type and written to the file.

It is yet to be decided if one file will be used for products, sales, and customers. 
I think that there should be separate files for every model. One for res.partner ,
one for product.template and one for sale.order.

First the export needs to be defined adn the basic structure of the XML file should be defined.
For the product i have exported in xml and it looks like this:
https://pastebin.com/22gpBLkA

For sure there sghould be more fields that will come later in the structure, but it is not yet decided for t
the variants of the products and how the images are going to be kept in the XML format file.

After we define the full xml structure then we will work on the import. It should not be a problem at all for 
the import once the export is done correctly.
