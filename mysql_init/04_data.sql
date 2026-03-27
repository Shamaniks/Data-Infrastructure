SET NAMES 'utf8mb4';

INSERT INTO outlet (outlet_name, outlet_address)
VALUES
('FG-01', 'г. Москва, ул. Беговая, д. 17, стр. 8'),
('FG-02', 'г. Москва, ул. Комсомольская, д. 56, стр. 6');

INSERT INTO profile (login, password, surname, name, patronymic)
VALUES
('wk_IvanovII', 'Pa$$w0rd', 'Иванов', 'Иван', 'Иванович'),
('wk_PavlovPP', 'Pa$$w0rd', 'Павлов', 'Павел', 'Павлович'),
('wk_GlebovGG', 'Pa$$w0rd', 'Глебов', 'Глеб', 'Глебович'),
('wk_AlekseevAA', 'Pa$$w0rd', 'Алексеев', 'Алексей', 'Алексеевич'),
('wk_FedorovFF', 'Pa$$w0rd', 'Федоров', 'Федор', 'Федорович'),
('AndreevVA', 'Pa$$w0rd', 'Андреев', 'Виталий', 'Алексеевич'),
('MihailovaEA', 'Pa$$w0rd', 'Михайлова', 'Елена', 'Андреевна'),
('SergeevaBK', 'Pa$$w0rd', 'Сергеева', 'Валерия', 'Константиновна'),
('MihailovVO', 'Pa$$w0rd', 'Михайлов', 'Валентин', 'Олегович');

INSERT INTO job_title (job_title_name)
VALUES
('Старший кассир'),
('Кассир');

INSERT INTO hall (hall_name)
VALUES ('Мужская'), ('Женская'), ('Детская');

INSERT INTO sector (sector_number)
VALUES (1), (2), (3);

INSERT INTO stand (stand_number)
VALUES (1), (2), (3);

INSERT INTO supplier (supplier_name)
VALUES ('Вещи даром и не только');

INSERT INTO status (status_name)
VALUES ('В обработке'), ('В пути'), ('Доставлен');

INSERT INTO product_storage (storage_name, outlet_id, storage_address)
VALUES
('СП-01', 1, 'г. Москва, ул. Беговая, д. 19, к. 1'),
('СП-02', 1, 'г. Москва, ул. Беговая, д. 19, к. 2'),
('СП-03', 2, 'г. Москва, ул. Комсомольская, д. 52, к. 1'),
('СП-04', 2, 'г. Москва, ул. Комсомольская, д. 54, к. 1');

INSERT INTO worker (login, job_title_id, outlet_id)
VALUES
('wk_IvanovII', 1, 1),
('wk_PavlovPP', 2, 1),
('wk_GlebovGG', 2, 1),
('wk_AlekseevAA', 1, 2),
('wk_FedorovFF', 2, 2);

INSERT INTO client (login, phone, passport_series, passport_number, issue_date, card_number, email)
VALUES
('AndreevVA', '+79753514869', '49 62', '956384', '2021-05-03', '0324 6723 7235 7122', 'andreev_v_a@gmail.com'),
('MihailovaEA', '+79751245760', '41 78', '234577', '2019-11-18', '7223 7781 4325 9021', 'michailova_e_a@ya.ru'),
('SergeevaBK', '+79753514869', '49 62', '956384', '2021-05-03', '0324 6723 7235 7122', 'andreev_v_a@gmail.com'),
('MihailovVO', '+79751245760', '41 78', '234577', '2019-11-18', '7223 7781 4325 9021', 'michailova_e_a@ya.ru');

INSERT INTO product (article_number, product_document_url, price)
VALUES
('SP/0000001', '/path/to/image/prod_1.jpeg', 299.99),
('SP/0000002', '/path/to/image/prod_2.jpeg', 14000.00),
('SP/0000003', '/path/to/image/prod_3.jpeg', 450.00),
('SP/0000004', '/path/to/image/prod_4.jpeg', 1500.00),
('SP/0000005', '/path/to/image/prod_5.jpeg', 359.99);

INSERT INTO purchase (order_number, client_login, cashier_login, order_formation_timestamp)
VALUES
('ЗкП-000000001-23', 'AndreevVA', 'wk_PavlovPP', '2023-09-01 10:46:23'),
('ЗкП-000000002-23', 'MihailovaEA', 'wk_GlebovGG', '2023-09-01 10:59:01'),
('ЗкП-000000003-23', 'MihailovaEA', 'wk_PavlovPP', '2023-09-02 15:43:25'),
('ЗкП-000000004-23', 'AndreevVA', 'wk_FedorovFF', '2023-09-02 17:20:26'),
('ЗкП-000000005-23', 'SergeevaBK', 'wk_FedorovFF', '2023-09-02 18:00:23'),
('ЗкП-000000006-23', 'MihailovVO', 'wk_PavlovPP', '2023-09-03 10:43:25');

INSERT INTO receipt (order_number, receipt_number, receipt_formation_timestamp, total_amount, contributed_amount, change_amount)
VALUES
('ЗкП-000000001-23', 'КЧ-0000000001', '2023-09-01 11:05:04', 19319.98, 20000.00, 680.00),
('ЗкП-000000002-23', 'КЧ-0000000002', '2023-09-01 11:10:34', 17063.99, 17500.00, 436.00),
('ЗкП-000000003-23', 'КЧ-0000000003', '2023-09-02 16:28:20', 1620.00, 1700.00, 80.00),
('ЗкП-000000004-23', 'КЧ-0000000004', '2023-09-02 16:28:20', 1620.00, 1700.00, 80.00),
('ЗкП-000000005-23', 'КЧ-0000000005', '2023-09-02 17:25:19', 35111.99, 35500.00, 388.00),
('ЗкП-000000006-23', 'КЧ-0000000006', '2023-09-03 18:11:41', 3600.00, 3600.00, 0.00);

INSERT INTO request (request_number, login, request_formating_date)
VALUES
('ЗяП-00000001', 'wk_AlekseevAA', '2023-08-25'),
('ЗяП-00000002', 'wk_IvanovII', '2023-08-25');

INSERT INTO supply (supply_number, supplier_id, supply_formating_timestamp, status_id, supply_cost)
VALUES
('ЗП-0000000001-23', 1, '2023-08-30 11:02:00', 1, 50000.00),
('ЗП-0000000002-23', 1, '2023-08-30 12:40:00', 1, 40500.00);

INSERT INTO add_supply (supply_id, add_supply_number, product_id, add_supply_cost)
VALUES (2, 'ЗП-0000000001-23/1', 5, 3700.00);

INSERT INTO product_location (outlet_id, product_id, hall_id, sector_id, stand_id, product_quantity)
VALUES
(1, 1, 1, 1, 3, 450),
(1, 2, 1, 1, 2, 500),
(1, 3, 1, 1, 3, 191),
(2, 3, 2, 1, 3, 197),
(1, 4, 3, 2, 3, 126),
(2, 4, 1, 3, 1, 174),
(2, 5, 1, 1, 1, 454);

INSERT INTO product_order_connection (order_number, product_id, product_quantity, product_cost)
VALUES
('ЗкП-000000001-23', 1, 2, 599.98),
('ЗкП-000000001-23', 2, 1, 14000.00),
('ЗкП-000000001-23', 4, 1, 1500.00),
('ЗкП-000000002-23', 1, 1, 219.99),
('ЗкП-000000002-23', 2, 1, 14000.00),
('ЗкП-000000003-23', 3, 3, 1350.00),
('ЗкП-000000004-23', 2, 2, 28000.00),
('ЗкП-000000004-23', 3, 2, 900.00),
('ЗкП-000000004-23', 5, 1, 359.99),
('ЗкП-000000005-23', 4, 2, 3000.00),
('ЗкП-000000006-23', 1, 2, 599.98),
('ЗкП-000000006-23', 2, 1, 14000.00),
('ЗкП-000000003-23', 3, 2, 900.00),
('ЗкП-000000006-23', 4, 2, 3000.00);

INSERT INTO product_request_connection (request_id, product_id)
VALUES (1, 1), (1, 3), (2, 2);

INSERT INTO request_supply_connection (request_id, supply_id)
VALUES (1, 1), (2, 1);
