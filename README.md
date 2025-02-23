# Waterfall Model
[[Software Engineering]]

## Introduction

For this Product Manager Application there were multiple requirements determined for the correct functionality and satisfaction of the client. The requirements were the following:

* 1.Product registration: The system must allow new products, with the following fields: *name, product code, category, quantity, purchase price, sale price, supplier.*

* 2.Product editing: It must be possible to modify the information of a product (*name, quantity, price,* etc.).

* 3.Product deletion: The system must allow delete products that are no longer available or no longer part of the system.

* 4.Product search: Allow searching for products by *name, code, category or supplier.*

## ER

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

![image](https://github.com/user-attachments/assets/b04e2901-4fdf-42b3-bbdf-1021404fd763)
	Fig 1. ER diagram regarding the database used

## Calendar

![bcon-waterfall-904136447](https://github.com/user-attachments/assets/bc0363f5-1395-470d-b498-385172d1a036)
	Fig 2. Waterfall Model

### Project Timeline Explanation

This project follows a structured calendar based on the Waterfall model, divided into five phases:

- **Communication Phase (06/02/2025 - 07/02/2025):** Initial discussions and requirements gathering for the project.
    
- **Planning Phase (07/02/2025 - 09/02/2025):** Defining the project scope, tasks, and resources.
    
- **Modeling Phase (10/02/2025):** Designing the system architecture and database model.
    
- **Construction Phase (10/02/2025 - 12/02/2025):** Implementing the code, including the Python inventory system and database.
    
- **Deployment Phase (13/02/2025):** Deploying the system and ensuring it is operational.
    

This timeline reflects the sequential approach of the Waterfall model, where each phase builds on the previous one, ensuring thorough development and deployment of the inventory management system.

| **PHASE**             | **DATES**               |
| --------------------- | ----------------------- |
| **Communication Phase** | 06/02/2025 -07/02/2025  |
| **Planning Phase**      | 07/02/2025 - 9/2/2025   |
| **Modeling Phase**      | 10/02/2025 - 10/02/2025 |
| **Construction Phase**  | 10/02/2025 - 12/02/2025 |
| **Deployment Phase**    | 13/02/2025 - 13/02/2025 |

## Code Explanation

Through a menu-driven interface, users may manage product information with this Python inventory management system, which combines Python and MySQL. Products saved in a MySQL database can be viewed, edited, deleted, and searched using the program's options.  
  
In order to facilitate communication between the Python code and the MySQL database, the program starts by importing *mysql*.*connector*. Using parameters like *host, user, password, and database*, a connection to the database is made, and a cursor object is made in order to run SQL queries.

The application presents a menu with five choices after connecting: adding, search, edit, view products and delete. Because each option is managed by a distinct block of code, the user can carry out the intended action.  

**Adding new product**

Users can add a product by introducing all of the neccessary arguuments (*name, product code, category, quantity, purchase price, sale price, supplier.*)
![Screenshot 2025-02-17 192443](https://github.com/user-attachments/assets/049ad9c5-0f47-4614-a36b-a3eb13a2c04d)
	Fig 3. ADD function

**Search**
Users can look up products using the search functionality by:  
* Name 
* Code Category  
* Supplier  

Based on the chosen criterion, the application creates a SQL query to retrieve and show related products from the database.

![Screenshot 2025-02-17 192546](https://github.com/user-attachments/assets/a140907e-d120-4249-a3c0-86712fdd6be7)
	Fig 4. SEARCH function

**Edit function**
Users can change the product's name, code, category, quantity, buy price, sale price, and supplier using the edit function. The application changes the relevant database record after asking the user for the product code and the updated value.  

![Screenshot 2025-02-17 192601](https://github.com/user-attachments/assets/6843a695-7626-4de5-86f4-0ffbd9eb9f5a)
	Fig 5. EDIT function

**View Products**
All of the products kept in the database are retrieved and shown using the view option. The ID, name, code, category, quantity, buy price, sale price, and supplier of every product are printed in an easily legible format.  

![Screenshot 2025-02-17 192624](https://github.com/user-attachments/assets/e16cb59f-583c-4985-8053-22610ced0332)
	Fig 6. SHOW function

**Delete function**
By entering a product's code, consumers can utilize the delete function to get rid of it. The modifications are committed and the associated product is removed from the database.

Lastly, the application provides an exit option to end the session, making sure that the database connection and cursor are correctly terminated before doing so. This application offers a straightforward yet efficient inventory management solution and shows how to use Python to manage database activities.

![Screenshot 2025-02-17 192636](https://github.com/user-attachments/assets/3d1b6dfa-e089-4bbb-8554-f07f98696ce9)
	Fig 7. DELETE and EXIT functions, as well as closing the cursor and connection to the database

It should also be noted that for connecting the python program to a database we used the libraries MySQL. Connector and time, both of these ensure a connection to the database without any issues with the docker containers.

![Screenshot 2025-02-19 110022](https://github.com/user-attachments/assets/99f4c603-b1fe-48de-a0c4-db42a9fdb1cc)
	Fig 8. Connection to the database and libraries
 
## Docker Implementation

For this project, I chose Docker to simplify deployment and maintain a consistent environment for both the program and the database. 

To make deployment simpler, I prepared a docker-compose.yml file that outlines the project's required services: a MySQL database and a Python application. The database service (db) is created using a custom Dockerfile from the database/ directory, which runs a MySQL instance with predetermined credentials. It exposes port 3306 and uses a Docker volume (MySQL data) to keep data consistent between restarts.  
  
The application service (app) is created in the python/ directory and is database dependent, so it only starts when MySQL is ready. It sends database connection information as environment variables, making configuration more flexible. The local python/ directory is mounted inside the container at /app, allowing for changes without rebuilding the image.

If you want to use this setup, make sure Docker is installed and updated on your machine.

1. **Clone the Repository and/or Navigate to the Project Directory**

	You should first clone the GitHub repository and navigate to the folder in which you have all the necessary documents such as the *Docker-compose.yaml*.
	
		`git clone https://github.com/CrescentMnn/waterfall_model`
		`cd waterfall_model`
	
2. **Build and Start the containers**  
	Once you are inside the project directory you should build and start the containers by executing:
		`docker-compose build`
	
	This will build the database and application images.
	
	![Screenshot 2025-02-19 102804](https://github.com/user-attachments/assets/93cd5355-d609-4d71-9248-a5cfcfbe8a4b)
		Fig 9. Successful docker build
	
	Following the correct build you should also Start the containers with a different command:
	``
		`docker-compose up -d`
	
	![Screenshot 2025-02-19 103049](https://github.com/user-attachments/assets/4f198fcb-594d-4b07-9488-9eada16acbc5)
		Fig 10. Successful start of containers
		
3. **Verify running containers**
	
	After executing the last command you should be able to see the docker containers that are active with the following command:
		`docker ps`
	
	If the containers where successfully built you should see the following output (or similar):
	
	![Screenshot 2025-02-19 104235](https://github.com/user-attachments/assets/f02ea83e-b89a-4c36-b9ac-0c2fcf214348)
		Fig 11. Successful `docker ps` command
	
4. **Interacting with the Database and Python Program**
	In order to use the given python program you should execute the program in interactive mode using a docker command:
	
		`docker exec -it python_app python3 waterfall.py`
	
	The command `docker exec -it python_app python3 waterfall.py` allows you to run your Python script inside the **already running** Docker container named `python_app`. Instead of manually entering the container, this command lets you execute `waterfall.py` as if you were inside it. The `docker exec` part tells Docker to **run a command** inside a running container. The `-it` flag is actually two options combined: `-i` for **interactive mode**, which keeps the input open, and `-t` for **allocating a terminal**, making it behave like a normal command-line session.  (_“Use Containerized Databases,”_ 2024)
	
	You can also connect to the database if you wish to see how it is constructed or access it from MySQL instead of the program using:
	
		`docker exec -it db mysql -u moon -p`
	
	![Screenshot 2025-02-19 105216](https://github.com/user-attachments/assets/cdb7a6c6-0097-4a24-a152-213beedaee9c)
		Fig 12. Database structure inside MySQL

5. **Stopping and Restarting the Containers**
	To stop the containers, run:
		`docker-compose down`
## Code Execution

The following screenshots demonstrate how the menu works and how these operations are performed, they show all of the possible CRUD operations a system should have.

**Viewing initial list**

![first](https://github.com/user-attachments/assets/241fc12f-f13e-4d91-82be-96ab208aeaba)

**Adding new product**
	
![second](https://github.com/user-attachments/assets/7fbc32b9-15b2-4ffa-8e80-d92aff7dbd58)


![third](https://github.com/user-attachments/assets/466d0e76-3ebd-450c-8054-8a988a8e6c5e)


**Searching for a product**

![fourth](https://github.com/user-attachments/assets/60227f4d-b53c-4ab7-a788-e3f40942ed06)

**Updating product info and Deleting product**

![fifth](https://github.com/user-attachments/assets/1e3d1f49-02f2-4124-9800-68008a8e5c47)

![sixth](https://github.com/user-attachments/assets/8e3675ad-b919-4e12-8c19-84ec9d689477)

## References

* GeeksforGeeks. (2023, March 15). _Python Database Tutorial_. GeeksforGeeks. https://www.geeksforgeeks.org/python-database-tutorial/

* _IBM Developer_. (n.d.). https://developer.ibm.com/articles/waterfall-model-advantages-disadvantages/

* freeCodeCamp. (2020, August 31). _How to Create and Manipulate SQL Databases with Python_. freeCodeCamp.org. https://www.freecodecamp.org/news/connect-python-with-sql/

* Wikipedia contributors. (2025, February 13). _Entity–relationship model_. Wikipedia. https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model

* GeeksforGeeks. (2025, January 16). _Introduction of ER model_. GeeksforGeeks. https://www.geeksforgeeks.org/introduction-of-er-model/

* _“Use containerized databases.”_ (2024, October 24). Docker Documentation. https://docs.docker.com/guides/databases/
