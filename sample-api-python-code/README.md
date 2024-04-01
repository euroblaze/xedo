# Odoo CRUD Scripts

This repository contains four Python scripts that demonstrate CRUD (Create, Read, Update, Delete) operations on different Odoo models using the `xmlrpc` library.

## Prerequisites

Before running these scripts, make sure you have the following:

- Python installed on your system
- Access to an Odoo server and database

## Setup

1. Clone or download this repository to your local machine.
2. Open each Python script (`res_partner.py`, `product_template.py`, `sale_order.py`, and `stock_quant.py`) and replace the following placeholders with your actual values:
   - `'your_database'`: Your Odoo database name
   - `'your_username'`: Your Odoo username
   - `'your_password'`: Your Odoo password

## Usage

To run a specific script, navigate to the repository folder in your terminal or command prompt, and execute the following command:

python <script_name>.py.

Replace `<script_name>` with the name of the script you want to run (e.g., `res_partner.py`, `product_template.py`, `sale_order.py`, or `stock_quant.py`).

The script will prompt you to enter an action (`create`, `read`, `update`, or `delete`). Enter the desired action, and the script will execute the corresponding function for the specified Odoo model.

**Note:** For the `create`, `update`, and `delete` actions, you might need to modify the default values (e.g., partner IDs, product IDs, location IDs) in the respective functions to match the data in your Odoo database.

## Scripts

### 1. `res_partner.py`

This script demonstrates CRUD operations on the `res.partner` model in Odoo, which represents partners (customers, suppliers, etc.).

### 2. `product_template.py`

This script demonstrates CRUD operations on the `product.template` model in Odoo, which represents product templates.

### 3. `sale_order.py`

This script demonstrates CRUD operations on the `sale.order` model in Odoo, which represents sales orders.

### 4. `stock_quant.py`

This script demonstrates CRUD operations on the `stock.quant` model in Odoo, which represents stock quantities.

## Dependencies

These scripts use the `xmlrpc.client` module, which is part of the Python standard library and does not require any additional installation.