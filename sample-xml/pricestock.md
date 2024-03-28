# XEDO XML for Price & Stock Update
In E-Commerce Systems, price and stock-count of products (and related variations) change very often, in fact in real-time, and orders are generated on points of sale (webshops, market-places etc. See [Architecture for Omnichannel E-Commerce with Enterprise Opensource](https://www.simplify-erp.com/odoo-komplettloesungen/e-commerce/omnichannel-architektur-opensource/)).

XEDO helps to keep up with this regularly changing data by allowing a simple price and stock-count update XML file.

## Sample XML 

    <product currency=EUR>
        <internal_reference></internal_reference>
        <price></price>
        <stock></stock>
    </product>
