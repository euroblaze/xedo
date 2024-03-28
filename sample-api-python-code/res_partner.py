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

# Search for all partners
partner_ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[]])

# Read partner data
partners = models.execute_kw(db, uid, password, 'res.partner', 'read', [partner_ids], {'fields': ['name', 'email', 'phone']})

# Display partner data
print("Partners:")
for partner in partners:
    print(f"Name: {partner['name']}, Email: {partner['email']}, Phone: {partner['phone']}")
