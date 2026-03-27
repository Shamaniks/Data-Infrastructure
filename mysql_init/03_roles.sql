CREATE USER 'client'@'%' IDENTIFIED BY 'Pa$$w0rd';
CREATE USER 'worker'@'%' IDENTIFIED BY 'Pa$$w0rd';
CREATE USER 'cashier'@'%' IDENTIFIED BY 'Pa$$w0rd';
CREATE USER 'administrator'@'%' IDENTIFIED BY 'Pa$$w0rd';

GRANT USAGE ON *.* TO 'client'@'%';
GRANT USAGE ON *.* TO 'worker'@'%';
GRANT USAGE ON *.* TO 'cashier'@'%';
GRANT USAGE ON *.* TO 'administrator'@'%';

GRANT SELECT, INSERT, UPDATE ON data_infrastructure.profile TO 'client'@'%';
GRANT SELECT, INSERT, UPDATE ON data_infrastructure.client TO 'client'@'%';
GRANT SELECT, INSERT ON data_infrastructure.purchase TO 'client'@'%';
GRANT SELECT ON data_infrastructure.outlet TO 'client'@'%';
GRANT SELECT ON data_infrastructure.product TO 'client'@'%';
GRANT SELECT ON data_infrastructure.product_location TO 'client'@'%';
GRANT SELECT ON data_infrastructure.product_order_connection TO 'client'@'%';

GRANT SELECT, INSERT ON data_infrastructure.purchase TO 'cashier'@'%';
GRANT SELECT, INSERT ON data_infrastructure.receipt TO 'cashier'@'%';
GRANT SELECT, UPDATE ON data_infrastructure.profile TO 'cashier'@'%';
GRANT SELECT ON data_infrastructure.outlet TO 'cashier'@'%';
GRANT SELECT ON data_infrastructure.job_title TO 'cashier'@'%';
GRANT SELECT ON data_infrastructure.hall TO 'cashier'@'%';
GRANT SELECT ON data_infrastructure.sector TO 'cashier'@'%';
GRANT SELECT ON data_infrastructure.stand TO 'cashier'@'%';
GRANT SELECT ON data_infrastructure.worker TO 'cashier'@'%';
GRANT SELECT ON data_infrastructure.client TO 'cashier'@'%';
GRANT SELECT ON data_infrastructure.product TO 'cashier'@'%';
GRANT SELECT ON data_infrastructure.product_location TO 'cashier'@'%';
GRANT SELECT ON data_infrastructure.product_order_connection TO 'cashier'@'%';

GRANT SELECT, INSERT, UPDATE, DELETE ON data_infrastructure.product TO 'worker'@'%';
GRANT SELECT, INSERT, UPDATE, DELETE ON data_infrastructure.product_location TO 'worker'@'%';
GRANT SELECT, INSERT ON data_infrastructure.receipt TO 'worker'@'%';
GRANT SELECT, INSERT ON data_infrastructure.purchase TO 'worker'@'%';
GRANT SELECT, INSERT ON data_infrastructure.request TO 'worker'@'%';
GRANT SELECT, INSERT ON data_infrastructure.supply TO 'worker'@'%';
GRANT SELECT, INSERT ON data_infrastructure.add_supply TO 'worker'@'%';
GRANT SELECT, INSERT ON data_infrastructure.product_order_connection TO 'worker'@'%';
GRANT SELECT, INSERT ON data_infrastructure.product_request_connection TO 'worker'@'%';
GRANT SELECT, INSERT ON data_infrastructure.request_supply_connection TO 'worker'@'%';
GRANT SELECT, UPDATE ON data_infrastructure.profile TO 'worker'@'%';
GRANT SELECT ON data_infrastructure.outlet TO 'worker'@'%';
GRANT SELECT ON data_infrastructure.job_title TO 'worker'@'%';
GRANT SELECT ON data_infrastructure.hall TO 'worker'@'%';
GRANT SELECT ON data_infrastructure.sector TO 'worker'@'%';
GRANT SELECT ON data_infrastructure.stand TO 'worker'@'%';
GRANT SELECT ON data_infrastructure.supplier TO 'worker'@'%';
GRANT SELECT ON data_infrastructure.status TO 'worker'@'%';
GRANT SELECT ON data_infrastructure.product_storage TO 'worker'@'%';
GRANT SELECT ON data_infrastructure.worker TO 'worker'@'%';
GRANT SELECT ON data_infrastructure.client TO 'worker'@'%';

GRANT ALL PRIVILEGES ON data_infrastructure.* TO 'administrator'@'%';

FLUSH PRIVILEGES;
