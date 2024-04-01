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
model_name = 'sale.order'


def create_sale_order():
    sale_order_data = {
        'partner_id': 1,  # Replace with the desired partner ID
        'order_line': [
            (0, 0, {
                'product_id': 1,  # Replace with the desired product ID
                'product_uom_qty': 2,
                'price_unit': 10.0,
            }),
        ],
    }
    sale_order_id = models.execute_kw(db, uid, password, model_name, 'create', [sale_order_data])
    print(f"Sale Order created with ID: {sale_order_id}")


def read_sale_orders():
    sale_order_ids = models.execute_kw(db, uid, password, model_name, 'search', [[]])
    sale_orders = models.execute_kw(db, uid, password, model_name, 'read', [sale_order_ids], ['name', 'partner_id', 'amount_total'])
    print("Sale Orders:")
    for sale_order in sale_orders:
        partner_id, partner_name = sale_order['partner_id']
        print(f"Order: {sale_order['name']}, Customer: {partner_name}, Total: {sale_order['amount_total']}")


def update_sale_order():
    sale_order_id = 1  # Replace with the desired sale order ID
    sale_order_data = {
        'partner_id': 2,  # Replace with the desired partner ID
    }
    models.execute_kw(db, uid, password, model_name, 'write', [[sale_order_id], sale_order_data])
    print(f"Sale Order with ID {sale_order_id} updated successfully")


def delete_sale_order():
    sale_order_id = 1  # Replace with the desired sale order ID
    models.execute_kw(db, uid, password, model_name, 'unlink', [[sale_order_id]])
    print(f"Sale Order with ID {sale_order_id} deleted successfully")


if __name__ == '__main__':
    action = input("Enter action (create, read, update, delete): ").lower()
    if action == 'create':
        create_sale_order()
    elif action == 'read':
        read_sale_orders()
    elif action == 'update':
        update_sale_order()
    elif action == 'delete':
        delete_sale_order()
    else:
        print("Invalid action. Please use create, read, update, or delete.")
