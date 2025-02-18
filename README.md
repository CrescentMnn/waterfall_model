# Waterfall Model

[[Software Engineering]]

For this Product Manager Application there were multiple requirements determined for the correct functionality and satisfaction of the client. The requirements were the following:

* 1.Product registration: The system must allow new products, with the following fields: *name, product code, category, quantity, purchase price, sale price, supplier.*

* 2.Product editing: It must be possible to modify the information of a product (*name, quantity, price,* etc.).

* 3.Product deletion: The system must allow delete products that are no longer available or no longer part of the system.

* 4.Product search: Allow searching for products by *name, code, category or supplier.*

### ER

The database model for this inventory system consists of a single table named `PRODUCTS` with the following structure:

- `ID`: An auto-generated unique identifier for each product.
    
- `name`: The name of the product.
    
- `product_code`: A unique code assigned to each product.
    
- `category`: The category to which the product belongs.
    
- `quantity`: The available quantity of the product in stock.
    
- `purchase_price`: The price at which the product was purchased.
    
- `sale_price`: The price at which the product is sold.
    
- `supplier`: The supplier providing the product.

This table serves as the central data storage, with each field corresponding to product attributes that can be manipulated through the program’s functionalities like search, edit, view, and delete.

![image](https://github.com/user-attachments/assets/a83ca17c-f097-4cbd-8ef3-9bcc5bf093b6)

	Fig 1. ER diagram regarding the database used

 ### Explanation

Through a menu-driven interface, users may manage product information with this Python inventory management system, which combines Python and MySQL. Products saved in a MySQL database can be viewed, edited, deleted, and searched using the program's options.  
  
In order to facilitate communication between the Python code and the MySQL database, the program starts by importing *mysql*.*connector*. Using parameters like *host, user, password, and database*, a connection to the database is made, and a cursor object is made in order to run SQL queries.

The application presents a menu with five choices after connecting: adding, search, edit, view products and delete. Because each option is managed by a distinct block of code, the user can carry out the intended action.  
