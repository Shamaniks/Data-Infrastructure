CREATE USER 'client'@'127.0.0.1' IDENTIFIED BY 'Pa$$w0rd';
CREATE USER 'worker'@'127.0.0.1' IDENTIFIED BY 'Pa$$w0rd';
CREATE USER 'cashier'@'127.0.0.1' IDENTIFIED BY 'Pa$$w0rd';
CREATE USER 'administrator'@'127.0.0.1' IDENTIFIED BY 'Pa$$w0rd';

GRANT USAGE ON *.* TO 'client'@'127.0.0.1';
GRANT USAGE ON *.* TO 'worker'@'127.0.0.1';
GRANT USAGE ON *.* TO 'cashier'@'127.0.0.1';
GRANT USAGE ON *.* TO 'administrator'@'127.0.0.1';

GRANT SELECT, INSERT, UPDATE ON data_infrastructure.profile TO 'client'@'127.0.0.1';
GRANT SELECT, INSERT, UPDATE ON data_infrastructure.client TO 'client'@'127.0.0.1';
GRANT SELECT, INSERT ON data_infrastructure.purchase TO 'client'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.outlet TO 'client'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.product TO 'client'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.product_location TO 'client'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.product_order_connection TO 'client'@'127.0.0.1';

GRANT SELECT, INSERT ON data_infrastructure.purchase TO 'cashier'@'127.0.0.1';
GRANT SELECT, INSERT ON data_infrastructure.receipt TO 'cashier'@'127.0.0.1';
GRANT SELECT, UPDATE ON data_infrastructure.profile TO 'cashier'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.outlet TO 'cashier'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.job_title TO 'cashier'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.hall TO 'cashier'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.sector TO 'cashier'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.stand TO 'cashier'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.worker TO 'cashier'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.client TO 'cashier'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.product TO 'cashier'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.product_location TO 'cashier'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.product_order_connection TO 'cashier'@'127.0.0.1';

GRANT SELECT, INSERT, UPDATE, DELETE ON data_infrastructure.product TO 'worker'@'127.0.0.1';
GRANT SELECT, INSERT, UPDATE, DELETE ON data_infrastructure.product_location TO 'worker'@'127.0.0.1';
GRANT SELECT, INSERT ON data_infrastructure.receipt TO 'worker'@'127.0.0.1';
GRANT SELECT, INSERT ON data_infrastructure.purchase TO 'worker'@'127.0.0.1';
GRANT SELECT, INSERT ON data_infrastructure.request TO 'worker'@'127.0.0.1';
GRANT SELECT, INSERT ON data_infrastructure.supply TO 'worker'@'127.0.0.1';
GRANT SELECT, INSERT ON data_infrastructure.add_supply TO 'worker'@'127.0.0.1';
GRANT SELECT, INSERT ON data_infrastructure.product_order_connection TO 'worker'@'127.0.0.1';
GRANT SELECT, INSERT ON data_infrastructure.product_request_connection TO 'worker'@'127.0.0.1';
GRANT SELECT, INSERT ON data_infrastructure.request_supply_connection TO 'worker'@'127.0.0.1';
GRANT SELECT, UPDATE ON data_infrastructure.profile TO 'worker'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.outlet TO 'worker'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.job_title TO 'worker'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.hall TO 'worker'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.sector TO 'worker'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.stand TO 'worker'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.supplier TO 'worker'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.status TO 'worker'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.product_storage TO 'worker'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.worker TO 'worker'@'127.0.0.1';
GRANT SELECT ON data_infrastructure.client TO 'worker'@'127.0.0.1';

GRANT ALL PRIVILEGES ON data_infrastructure.* TO 'administrator'@'127.0.0.1';

FLUSH PRIVILEGES;
