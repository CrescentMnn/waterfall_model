#!/usr/bin/env python3

# PRODUCTS:  new products, (name, code, category, quantity, purchase, price, sale price, supplier)

# CAN EDIT: (name, quantity, purchase, price, etc..)

# DELETION: delete prodcuts arent available

# SEARCH: allow search by: name, code, category or supplier

import mysql.connector

# Set up your connection parameters
db_connection = mysql.connector.connect(
    #parameters
)

# Create a cursor object to interact with the database
cursor = db_connection.cursor()


print("\t\t++++++++++++WATERFALL MODEL++++++++++++\n\n\n")

while(1):
    print("\tMENU\n\n1. Add product\n2. Search\n3. Edit\n4. View products\n5. Delete\n6. Exit\n\n");
    menu_input = input("input:");

# ADDING

    if menu_input == '1':
        product_name = input("Product Name: ")
        product_code = input("Product Code: ")
        category = input("Category: ")
        quantity = input("Quantity: ")
        purchase_price = input("Purchase Price: ")
        sale_price = input("Sale Price: ")
        supplier = input("Supplier: ")

        query = """INSERT INTO products (name, product_code, category, quantity, purchase_price, sale_price, supplier) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (product_name, product_code, category, quantity, purchase_price, sale_price, supplier))
        db_connection.commit()

        print("New product added successfully!\n\n\n")

        
# SEARCH
    if menu_input == '2':
        search_fields = {
        '1': 'name',
        '2': 'product_code',
        '3': 'category',
        '4': 'supplier'
        }
        user_input_searchMEN = input("Would you like to search by: 1. Name, 2. Code, 3. Category, 4. Supplier\ninput:")
        if user_input_searchMEN in search_fields:
            user_input_VAL = input(f"Enter {search_fields[user_input_searchMEN]} for product: ")
            query = f"SELECT * FROM products WHERE {search_fields[user_input_searchMEN]} = %s"
            cursor.execute(query, (user_input_VAL,))
            results = cursor.fetchall()
        if not results:
            print("No result found\n\n\n")
        else:
            print("\nSearch Results:\n")
            for result in results:
                print(f"ID: {result[0]}, Name: {result[1]}, Code: {result[2]}, Category: {result[3]}, Quantity: {result[4]}, Purchase Price: {result[5]}, Sale Price: {result[6]}, Supplier: {result[7]}\n\n\n")
 
# EDIT 

    elif menu_input == '3':
        edit_fields = {
            '1': 'name',
            '2': 'product_code',
            '3': 'category',
            '4': 'quantity',
            '5': 'purchase_price',
            '6': 'sale_price',
            '7': 'supplier'
        }
        user_edit = input("Would you like to edit a product's: 1. Name, 2. Code, 3. Category, 4. Supplier\ninput:")
        
        if user_edit in edit_fields:
            product_code = input("Product Code:")
            new_value = input(f"Enter new value for {edit_fields[user_edit]}: ")

            query = f"UPDATE products SET {edit_fields[user_edit]} = %s WHERE product_code = %s"
            cursor.execute(query, (new_value, product_code))
            db_connection.commit()

            print("Product updated successfully!\n\n\n")
        else:
            print("Invalid option for editing.\n\n\n")

# SHOW

    elif menu_input == '4':
        try:
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()

            if not products:
                print("No products found.\n\n\n");
            else:
                print("\nProdcuts List:")
                for product in products:
                    print(f"ID: {product[0]}, Name: {product[1]}, Code: {product[2]}, Category: {product[3]}, Quantity: {product[4]}, Purchase Price: {product[5]}, Sale Price: {product[6]}, Supplier: {product[7]}\n\n\n")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

# DELETE

    elif menu_input == '5':
        user_input_code = input("Enter the product code to delete: ")
        cursor.execute("DELETE FROM products WHERE product_code = %s", (user_input_code,))

        db_connection.commit()

        print(f"Product with code {user_input_code} deleted.\n\n\n");

# EXIT

    elif menu_input == '6':
        print("Exiting...\n");
        break;

    else:
        print("Invalid choice. Please choose a valid option.");


cursor.close()
db_connection.close()
