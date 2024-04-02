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
model_name = 'res.partner'


def create_partner():
    partner_data = {
        'name': 'New Partner',
        'email': 'new_partner@example.com',
        'phone': '1234567890',
    }
    partner_id = models.execute_kw(db, uid, password, model_name, 'create', [partner_data])
    print(f"Partner created with ID: {partner_id}")


def read_partners():
    partner_ids = models.execute_kw(db, uid, password, model_name, 'search', [[]])
    partners = models.execute_kw(db, uid, password, model_name, 'read', [partner_ids], {'fields': ['name', 'email', 'phone']})
    print("Partners:")
    for partner in partners:
        print(f"Name: {partner['name']}, Email: {partner['email']}, Phone: {partner['phone']}")


def update_partner():
    partner_id = 14  # Replace with the desired partner ID
    partner_data = {
        'name': 'Updated Partner Name',
        'phone': '9876543210',
    }
    models.execute_kw(db, uid, password, model_name, 'write', [[partner_id], partner_data])
    print(f"Partner with ID {partner_id} updated successfully")


def delete_partner():
    partner_id = 14  # Replace with the desired partner ID
    models.execute_kw(db, uid, password, model_name, 'unlink', [[partner_id]])
    print(f"Partner with ID {partner_id} deleted successfully")


if __name__ == '__main__':
    action = input("Enter action (create, read, update, delete): ").lower()
    if action == 'create':
        create_partner()
    elif action == 'read':
        read_partners()
    elif action == 'update':
        update_partner()
    elif action == 'delete':
        delete_partner()
    else:
        print("Invalid action. Please use create, read, update, or delete.")

