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
model_name = 'product.template'


def create_product():
    product_data = {
        'name': 'New Product',
        'categ_id': 1,  # Replace with the desired category ID
        'list_price': 10.0,
        'weight': 0.5,
    }
    product_id = models.execute_kw(db, uid, password, model_name, 'create', [product_data])
    print(f"Product created with ID: {product_id}")


def read_products():
    product_ids = models.execute_kw(db, uid, password, model_name, 'search', [[]])
    products = models.execute_kw(db, uid, password, model_name, 'read', [product_ids], {'fields': ['name', 'categ_id', 'list_price', 'weight']})
    print("Product Templates:")
    for product in products:
        category_id, category_name = product['categ_id']
        print(f"Name: {product['name']}, Category: {category_name}, Price: {product['list_price']}, Weight: {product['weight']}")


def update_product():
    product_id = 1  # Replace with the desired product template ID
    product_data = {
        'name': 'Updated Product Name',
        'list_price': 15.0,
    }
    models.execute_kw(db, uid, password, model_name, 'write', [[product_id], product_data])
    print(f"Product with ID {product_id} updated successfully")


def delete_product():
    product_id = 1  # Replace with the desired product template ID
    models.execute_kw(db, uid, password, model_name, 'unlink', [[product_id]])
    print(f"Product with ID {product_id} deleted successfully")


if __name__ == '__main__':
    action = input("Enter action (create, read, update, delete): ").lower()
    if action == 'create':
        create_product()
    elif action == 'read':
        read_products()
    elif action == 'update':
        update_product()
    elif action == 'delete':
        delete_product()
    else:
        print("Invalid action. Please use create, read, update, or delete.")
