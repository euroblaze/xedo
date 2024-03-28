import xmlrpc.client

# Connect to the Odoo server
url = 'https://v16cc.simplify-erp.de/'
db = 'v16cc'
username = 'testapi@simplify-erp.de'
password = '5327e818de6a32587348ca4d10ce41c9318276c6'

# Create a connection to the Odoo server
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

# Search for all product templates
product_ids = models.execute_kw(db, uid, password, 'product.template', 'search', [[]])

# Read partner data
products = models.execute_kw(db, uid, password, 'product.template', 'read', [product_ids], {'fields': ['name', 'categ_id', 'list_price', 'type']})

# Display product template data
print("Product Templates:")
for product in products:
    category_id, category_name = product['categ_id']
    print(f"Name: {product['name']}, Category: {category_name}, Price: {product['list_price']}, Type: {product['type']}")