import xmlrpc.client

# Connect to the Odoo server
url = 'https://v16cc.simplifwy-erp.de/'
db = 'v16cc'
username = 'testapi@simplify-erp.de'
password = '5327e818de6a32587348ca4d10ce41c9318276c6'

# Create a connection to the Odoo server
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

# Search for all stock quants
quant_ids = models.execute_kw(db, uid, password, 'stock.quant', 'search', [[]])

# Read partner data
quants = models.execute_kw(db, uid, password, 'stock.quant', 'read', [quant_ids], {'fields': ['product_id', 'location_id', 'quantity']})

# Display stock quant data
print("Stock Quants:")
for quant in quants:
    product_id, product_name = quant['product_id']
    location_id, location_name = quant['location_id']
    print(f"Product: {product_name}, Location: {location_name}, Quantity: {quant['quantity']}")