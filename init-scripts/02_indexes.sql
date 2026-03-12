CREATE INDEX index_login_password ON profile (login, password);
CREATE INDEX index_full_name ON profile (surname, name, patronymic);
CREATE INDEX index_job_title_name ON job_title (job_title_name);

CREATE INDEX index_phone ON client (phone);
CREATE INDEX index_card_number ON client (card_number);
CREATE INDEX index_email ON client (email);
CREATE INDEX index_passport ON client (passport_series, passport_number, issue_date);

CREATE INDEX index_article_number ON product (article_number);
CREATE INDEX index_product_doc_url ON product (product_document_url(100));

CREATE INDEX index_outlet_name ON outlet (outlet_name);
CREATE INDEX index_storage_name ON product_storage (storage_name);
CREATE INDEX index_hall_name ON hall (hall_name);
CREATE INDEX index_sector_number ON sector (sector_number);
CREATE INDEX index_stand_number ON stand (stand_number);

CREATE INDEX index_receipt_number ON receipt (receipt_number);

CREATE INDEX index_request_number ON request (request_number);
CREATE INDEX index_supplier_name ON supplier (supplier_name);
CREATE INDEX index_status_name ON status (status_name);
CREATE INDEX index_supply_number ON supply (supply_number);
CREATE INDEX index_add_supply_number ON add_supply (add_supply_number);

CREATE INDEX index_location_quantity ON product_location (product_quantity);
