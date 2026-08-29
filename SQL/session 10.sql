-- Question 1
--Create two tables: AppOrders (for orders placed via a food delivery app like Zomato) and InStoreOrders (for direct restaurant orders), each with columns: order_id, customer_name, amount, and order_date. Insert at least 3 sample records into each table.

-- creating table AppOrders and table table InStoreOrders
CREATE TABLE AppOrders (
    order_id INT,
    customer_name VARCHAR(50),
    amount DECIMAL(10,2),
    order_date DATE
);

CREATE TABLE InStoreOrders (
    order_id INT,
    customer_name VARCHAR(50),
    amount DECIMAL(10,2),
    order_date DATE
);

-- insertin values in both table --

INSERT INTO AppOrders (order_id, customer_name, amount, order_date)
VALUES
(101, 'Rahul', 450.00, '2026-08-25'),
(102, 'Priya', 600.00, '2026-08-26'),
(103, 'Amit', 350.00, '2026-08-27');


INSERT INTO InStoreOrders (order_id, customer_name, amount, order_date)
VALUES
(201, 'Neha', 500.00, '2026-08-25'),
(202, 'Rohit', 750.00, '2026-08-26'),
(203, 'Sneha', 400.00, '2026-08-27');

-- checking the values of both table 

SELECT * FROM AppOrders;

SELECT * FROM InStoreOrders;

-- Question 2 

--Write a SQL query using UNION to combine all unique customer names from both AppOrders and InStoreOrders tables into a single list.
SELECT customer_name
FROM AppOrders

UNION

SELECT customer_name
FROM InStoreOrders;

-- Question 3
--Write a SQL query using UNION ALL to display every order (including duplicates if any) from both AppOrders and InStoreOrders, showing order_id, customer_name, amount, and order_date

SELECT order_id, customer_name, amount, order_date
FROM AppOrders

UNION ALL

SELECT order_id, customer_name, amount, order_date
FROM InStoreOrders;

-- Question 4
--Demonstrate the difference between UNION and UNION ALL by adding a duplicate customer_name in both tables, then running both queries and noting the difference in the result count.<br><br><em><strong>Hint:</strong> UNION removes duplicates, UNION ALL does not.</em>

-- adding new values to the table instoreorder
INSERT INTO InStoreOrders (order_id, customer_name, amount, order_date)
VALUES
(204, 'Rahul', 550.00, '2026-08-28');

-- checking total data of this table 
SELECT * FROM InStoreOrders;

-- testing again both method 
-- UNION test
SELECT customer_name
FROM AppOrders

UNION

SELECT customer_name
FROM InStoreOrders;

-- UNION ALL test
SELECT customer_name
FROM AppOrders

UNION ALL

SELECT customer_name
FROM InStoreOrders;