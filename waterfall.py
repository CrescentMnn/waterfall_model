#!/usr/bin/env python3

# PRODUCTS:  new products, (name, code, category, quantity, purchase, price, sale price, supplier)

# CAN EDIT: (name, quantity, purchase, price, etc..)

# DELETION: delete prodcuts arent available

# SEARCH: allow search by: name, code, category or supplier

import mysql.connector

print("MySQL connector installed successfully! UwU")

# Set up your connection parameters
db_connection = mysql.connector.connect(
    host="localhost",            # Your host, typically localhost
    user="moon",        # Your MySQL username (e.g., root)
    password="123123",    # Your MySQL password
    database="waterfall_model"     # The name of the database you want to use
)

# Create a cursor object to interact with the database
cursor = db_connection.cursor()


print("\t\t++++++++++++WATERFALL MODEL++++++++++++\n\n\n")

while(1):
    print("\tMENU\n\n1. Search\n2. Edit\n3. View products\n4. Delete\n5. Exit\n\n");
    menu_input = input("input:");
    if menu_input == '1':
        user_input_searchMEN = input("Would you like to search by: 1. Name, 2. Code, 3. Category, 4. Supplier\ninput:")
        if user_input_searchMEN == '1':
            user_input_VAL = input("Name for product:")
            cursor.execute("SELECT * FROM products WHERE name = %s", (user_input_VAL,))

            results = cursor.fetchall()

            if not results:
                print("No result found\n\n\n")
            else:
                print("\nSearch Results:\n")
                
                for result in results:
                    print(f"ID: {result[0]}, Name: {result[1]}, Code: {result[2]}, Category: {result[3]}, Quantity: {result[4]}, Purchase Price: {result[5]}, Sale Price: {result[6]}, Supplier: {result[7]}\n\n\n")

    elif menu_input == '2':
        cursor.execute()
    elif menu_input == '3':
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

    elif menu_input == '4':
        user_input_code = input("Enter the product code to delete: ")
        cursor.execute("DELETE FROM products WHERE product_code = %s", (user_input_code,))

        db_connection.commit()

        print(f"Product with code {user_input_code} deleted.\n\n\n");

    elif menu_input == '5':
        print("Exiting...\n");
        break;

    else:
        print("Invalid choice. Please choose a valid option.");



db_connection.close()
