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
model_name = 'stock.quant'


def create_stock_quant():
    stock_quant_data = {
        'product_id': 1,  # Replace with the desired product ID
        'location_id': 1,  # Replace with the desired location ID
        'quantity': 10.0,
    }
    stock_quant_id = models.execute_kw(db, uid, password, model_name, 'create', [stock_quant_data])
    print(f"Stock Quant created with ID: {stock_quant_id}")


def read_stock_quants():
    stock_quant_ids = models.execute_kw(db, uid, password, model_name, 'search', [[]])
    stock_quants = models.execute_kw(db, uid, password, model_name, 'read', stock_quant_ids, ['product_id', 'location_id', 'quantity'])
    print("Stock Quants:")
    for stock_quant in stock_quants:
        product_id, product_name = stock_quant['product_id']
        location_id, location_name = stock_quant['location_id']
        print(f"Product: {product_name}, Location: {location_name}, Quantity: {stock_quant['quantity']}")


def update_stock_quant():
    stock_quant_id = 1  # Replace with the desired stock quant ID
    stock_quant_data = {
        'quantity': 20.0,
    }
    models.execute_kw(db, uid, password, model_name, 'write', [[stock_quant_id], stock_quant_data])
    print(f"Stock Quant with ID {stock_quant_id} updated successfully")


def delete_stock_quant():
    stock_quant_id = 1  # Replace with the desired stock quant ID
    models.execute_kw(db, uid, password, model_name, 'unlink', [[stock_quant_id]])
    print(f"Stock Quant with ID {stock_quant_id} deleted successfully")


if __name__ == '__main__':
    action = input("Enter action (create, read, update, delete): ").lower()
    if action == 'create':
        create_stock_quant()
    elif action == 'read':
        read_stock_quants()
    elif action == 'update':
        update_stock_quant()
    elif action == 'delete':
        delete_stock_quant()
    else:
        print("Invalid action. Please use create, read, update, or delete.")
