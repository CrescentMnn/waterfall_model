use waterfall_model_database;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    product_code VARCHAR(100) UNIQUE NOT NULL,
    category VARCHAR(100),
    quantity INT DEFAULT 0,
    purchase_price DECIMAL(10, 2),
    sale_price DECIMAL(10, 2),
    supplier VARCHAR(255)
);
