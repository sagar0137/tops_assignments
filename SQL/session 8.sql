-- SQL Assignment 08

-- QUESTION 1
-- Create two tables in your SQL database: Users (user_id, username, city) and Orders (order_id, user_id,
-- product, amount). Insert at least 3 users and 5 orders, making sure some users have no orders.

CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50),
    city VARCHAR(50)
);


CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    product VARCHAR(100),
    amount DECIMAL(10,2)
);


-- Insert 3 users
INSERT INTO Users (user_id, username, city)
VALUES
(1, 'Sagar', 'Ahmedabad'),
(2, 'Rahul', 'Surat'),
(3, 'Priya', 'Vadodara');


-- Insert 5 orders
-- User 3 has no order
INSERT INTO Orders (order_id, user_id, product, amount)
VALUES
(101, 1, 'Pizza', 450),
(102, 1, 'Burger', 250),
(103, 2, 'Biryani', 300),
(104, 2, 'Cold Drink', 100),
(105, 1, 'Pasta', 350);



-- QUESTION 2
-- Write an SQL query using INNER JOIN to list all usernames and their ordered products, showing only
-- users who have placed at least one order


SELECT u.username,
       o.product
FROM Users AS u
INNER JOIN Orders AS o
ON u.user_id = o.user_id;



-- QUESTION 3
-- Write an SQL query using LEFT JOIN to display all usernames along with their ordered products.
-- For users who haven't placed any orders, show NULL for the product.

SELECT u.username,
       o.product
FROM Users AS u
LEFT JOIN Orders AS o
ON u.user_id = o.user_id;


-- QUESTION 4
-- Write an SQL query using RIGHT JOIN to show all orders and the corresponding username for each order.
-- If an order has a user_id that doesn't exist in the Users table, display NULL for the username.
--<br><br><em><strong>Hint:</strong> Try deleting one user and keeping their order to test this case.</em>

SELECT o.order_id,
       o.product,
       o.amount,
       u.username
FROM Users AS u
RIGHT JOIN Orders AS o
ON u.user_id = o.user_id;



-- QUESTION 5
-- Suppose you want to analyze food delivery data like Zomato. Create a CustomerSegments table (segment_id, 
--segment_name), and link it to Users with a foreign key. Write an SQL query to show each username,
-- their segment name, and total order amount (use JOINs as needed).

CREATE TABLE CustomerSegments (
    segment_id INT PRIMARY KEY,
    segment_name VARCHAR(50)
);


-- Add segment_id to Users
ALTER TABLE Users
ADD segment_id INT;


-- Add foreign key
ALTER TABLE Users
ADD CONSTRAINT fk_user_segment
FOREIGN KEY (segment_id)
REFERENCES CustomerSegments(segment_id);


-- Insert customer segments
INSERT INTO CustomerSegments (segment_id, segment_name)
VALUES
(1, 'Premium'),
(2, 'Regular'),
(3, 'New');


-- Assign segments to users
UPDATE Users
SET segment_id = 1
WHERE user_id = 1;

UPDATE Users
SET segment_id = 2
WHERE user_id = 2;

UPDATE Users
SET segment_id = 3
WHERE user_id = 3;


-- Show username, segment name,
-- and total order amount

SELECT u.username,
       cs.segment_name,
       COALESCE(SUM(o.amount), 0) AS total_order_amount
FROM Users AS u
JOIN CustomerSegments AS cs
ON u.segment_id = cs.segment_id
LEFT JOIN Orders AS o
ON u.user_id = o.user_id
GROUP BY u.user_id, u.username, cs.segment_name;