CREATE TABLE IF NOT EXISTS outlet (
    outlet_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    outlet_name VARCHAR(10) NOT NULL,
    outlet_address VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS profile (
    login VARCHAR(20) PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    patronymic VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS job_title (
    job_title_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    job_title_name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS hall (
    hall_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    hall_name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS sector (
    sector_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    sector_number INT NOT NULL
);

CREATE TABLE IF NOT EXISTS stand (
    stand_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    stand_number INT NOT NULL
);

CREATE TABLE IF NOT EXISTS supplier (
    supplier_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS status (
    status_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    status_name VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS product_storage (
    storage_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    storage_name VARCHAR(10) NOT NULL,
    outlet_id INT NOT NULL,
    storage_address VARCHAR(255) NOT NULL,
    FOREIGN KEY (outlet_id) REFERENCES outlet(outlet_id)
);

CREATE TABLE IF NOT EXISTS worker (
    login VARCHAR(20) PRIMARY KEY,
    job_title_id INT NOT NULL,
    outlet_id INT NOT NULL,
    FOREIGN KEY (login) REFERENCES profile(login),
    FOREIGN KEY (job_title_id) REFERENCES job_title(job_title_id),
    FOREIGN KEY (outlet_id) REFERENCES outlet(outlet_id)
);

CREATE TABLE IF NOT EXISTS client (
    login VARCHAR(20) PRIMARY KEY,
    phone VARCHAR(20) NOT NULL,
    passport_series VARCHAR(10) NOT NULL,
    passport_number VARCHAR(10) NOT NULL,
    issue_date DATE NOT NULL,
    card_number VARCHAR(25) NOT NULL,
    email VARCHAR(255),
    FOREIGN KEY (login) REFERENCES profile(login)
);

CREATE TABLE IF NOT EXISTS product (
    product_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    article_number VARCHAR(20) NOT NULL,
    product_document_url TEXT NOT NULL, 
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS purchase (
    order_number VARCHAR(20) PRIMARY KEY,
    client_login VARCHAR(20) NOT NULL,
    cashier_login VARCHAR(20) NOT NULL,
    order_formation_timestamp DATETIME NOT NULL, 
    FOREIGN KEY (client_login) REFERENCES client(login),
    FOREIGN KEY (cashier_login) REFERENCES worker(login)
);

CREATE TABLE IF NOT EXISTS receipt (
    order_number VARCHAR(20) PRIMARY KEY,
    receipt_number VARCHAR(20) NOT NULL,
    receipt_formation_timestamp DATETIME NOT NULL,
    total_amount DECIMAL(15, 2) NOT NULL,
    contributed_amount DECIMAL(15, 2) NOT NULL,
    change_amount DECIMAL(15, 2) NOT NULL,
    FOREIGN KEY (order_number) REFERENCES purchase(order_number)
);

CREATE TABLE IF NOT EXISTS request (
    request_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    request_number VARCHAR(20),
    login VARCHAR(20) NOT NULL,
    request_formating_date DATE NOT NULL,
    FOREIGN KEY (login) REFERENCES profile(login)
);

CREATE TABLE IF NOT EXISTS supply (
    supply_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    supply_number VARCHAR(20),
    supplier_id INT NOT NULL,
    supply_formating_timestamp DATETIME NOT NULL,
    status_id INT NOT NULL,
    supply_cost DECIMAL(15, 2) NOT NULL,
    FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id),
    FOREIGN KEY (status_id) REFERENCES status(status_id)
);

CREATE TABLE IF NOT EXISTS add_supply (
    add_supply_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    supply_id INT NOT NULL,
    add_supply_number VARCHAR(30) NOT NULL,
    product_id INT NOT NULL,
    add_supply_cost DECIMAL(16, 2) NOT NULL,
    FOREIGN KEY (supply_id) REFERENCES supply(supply_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

CREATE TABLE IF NOT EXISTS product_request_connection (
    connection_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    product_id INT NOT NULL,
    FOREIGN KEY (request_id) REFERENCES request(request_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

CREATE TABLE IF NOT EXISTS request_supply_connection (
    connection_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    supply_id INT NOT NULL,
    FOREIGN KEY (request_id) REFERENCES request(request_id),
    FOREIGN KEY (supply_id) REFERENCES supply(supply_id)
);

CREATE TABLE IF NOT EXISTS product_order_connection (
    connection_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    order_number VARCHAR(20) NOT NULL,
    product_id INT NOT NULL,
    product_quantity INT NOT NULL,
    product_cost DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_number) REFERENCES purchase(order_number),
    FOREIGN KEY (product_id) REFERENCES product(product_id)
);

CREATE TABLE IF NOT EXISTS product_location (
    location_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    outlet_id INT NOT NULL,
    product_id INT NOT NULL,
    hall_id INT NOT NULL,
    sector_id INT NOT NULL,
    stand_id INT NOT NULL,
    product_quantity INT NOT NULL,
    FOREIGN KEY (outlet_id) REFERENCES outlet(outlet_id),
    FOREIGN KEY (product_id) REFERENCES product(product_id),
    FOREIGN KEY (hall_id) REFERENCES hall(hall_id),
    FOREIGN KEY (sector_id) REFERENCES sector(sector_id),
    FOREIGN KEY (stand_id) REFERENCES stand(stand_id)
);
