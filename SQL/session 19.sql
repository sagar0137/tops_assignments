
-- SESSION 19 -
-- QUESTION 1
-- Run a SELECT query on a large 'orders' table (at least 10,000 rows) to find all orders for a specific user_id and measure the query execution time.


-- Check number of rows
SELECT COUNT(*) AS total_orders
FROM orders;


-- Query before creating the index
SELECT *
FROM orders
WHERE user_id = 101;


-- In MySQL Workbench, check execution time
-- from the Action Output / query execution details.



-- QUESTION 2
-- Create an index on the user_id column of the 'orders' table and re-run the same SELECT query to measure the new execution time


CREATE INDEX idx_user_id
ON orders(user_id);


-- Run the same query again
SELECT *
FROM orders
WHERE user_id = 101;


-- Compare the execution time before and after
-- creating the index.



-- QUESTION 3
-- Use the EXPLAIN PLAN command to analyze how your SELECT query runs before and after adding the index, and write down the key differences you observe in the output


-- Before index:
EXPLAIN
SELECT *
FROM orders
WHERE user_id = 101;


-- After index:
EXPLAIN
SELECT *
FROM orders
WHERE user_id = 101;


-- Look at important columns such as:
-- type
-- possible_keys
-- key
-- rows
-- Extra


-- QUESTION 4
--Write a query for a 'products' table that avoids a full table scan by using an index on the 'category' column to fetch all products in a specific category.


CREATE INDEX idx_category
ON products(category);


-- Fetch products from a specific category

SELECT *
FROM products
WHERE category = 'Electronics';


-- Check whether MySQL uses the index

EXPLAIN
SELECT *
FROM products
WHERE category = 'Electronics';


-- QUESTION 5
-- Suppose your SELECT query on the 'orders' table is still slow even after adding an index. Use EXPLAIN PLAN and research at least one more optimization technique (other than indexing) using an AI tool like ChatGPT or Copilot, and describe how you would apply it.


-- Example technique: Select only required columns
-- instead of using SELECT *.

-- Less optimized:
SELECT *
FROM orders
WHERE user_id = 101;


-- More optimized:
SELECT order_id,
       user_id,
       order_date,
       total_amount
FROM orders
WHERE user_id = 101;


-- Another useful technique is filtering rows
-- as early as possible and avoiding unnecessary
-- calculations/functions on indexed columns.