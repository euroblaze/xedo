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

# Search for all sale orders
sale_ids = models.execute_kw(db, uid, password, 'sale.order', 'search', [[]])

# Read partner data
sales = models.execute_kw(db, uid, password, 'sale.order', 'read', [sale_ids], {'fields': ['name', 'partner_id', 'amount_total']})

# Display sale order data
print("Sale Orders:")
for sale in sales:
    partner_id, partner_name = sale['partner_id']
    print(f"Order: {sale['name']}, Customer: {partner_name}, Total: {sale['amount_total']}")