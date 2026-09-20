-- SESSION 18 

-- QUESTION 1
-- Create a SQL view named TopRatedRestaurants that selects the restaurant name, average rating, and total number
-- of reviews from a table of Zomato-style restaurant reviews, showing only restaurants with an average rating above 4.0.


CREATE VIEW TopRatedRestaurants AS
SELECT
    r.restaurant_name,
    AVG(rr.rating) AS average_rating,
    COUNT(rr.review_id) AS total_reviews
FROM Restaurants AS r
INNER JOIN RestaurantReviews AS rr
    ON r.restaurant_id = rr.restaurant_id
GROUP BY r.restaurant_id, r.restaurant_name
HAVING AVG(rr.rating) > 4.0;


-- Check the view
SELECT *
FROM TopRatedRestaurants;


-- QUESTION 2
-- Update the TopRatedRestaurants view to also include the city column from the original restaurants table by 
--joining the relevant tables.<br><br><em><strong>Hint:</strong> Use an INNER JOIN to combine data from both tables 
--in your view definition.</em>


CREATE OR REPLACE VIEW TopRatedRestaurants AS
SELECT
    r.restaurant_name,
    r.city,
    AVG(rr.rating) AS average_rating,
    COUNT(rr.review_id) AS total_reviews
FROM Restaurants AS r
INNER JOIN RestaurantReviews AS rr
    ON r.restaurant_id = rr.restaurant_id
GROUP BY r.restaurant_id,
         r.restaurant_name,
         r.city
HAVING AVG(rr.rating) > 4.0;


-- Check updated view
SELECT *
FROM TopRatedRestaurants;


-- QUESTION 3
-- Try to update the average rating column directly through the TopRatedRestaurants view and observe what error or 
--limitation occurs. Write down the exact error message and explain why this happens based on SQL view limitations


UPDATE TopRatedRestaurants
SET average_rating = 5.0
WHERE restaurant_name = 'Restaurant A';


-- This will generally fail because
-- average_rating is calculated using AVG().
-- It is not a directly stored column.


-- QUESTION 4
-- Create a view called DailyOrderSummary that shows, for each date, the total number of food orders and the total 
--revenue from a Swiggy-style orders table. Ensure the view only includes dates from the last 30 days.<br><br><em><strong>
--Constraint:</strong> Use WHERE and GROUP BY clauses in your view definition.</em>


CREATE OR REPLACE VIEW DailyOrderSummary AS
SELECT
    DATE(order_date) AS order_date,
    COUNT(order_id) AS total_orders,
    SUM(total_amount) AS total_revenue
FROM SwiggyOrders
WHERE order_date >= CURDATE() - INTERVAL 30 DAY
GROUP BY DATE(order_date);


-- Check the view
SELECT *
FROM DailyOrderSummary
ORDER BY order_date DESC;



-- QUESTION 5
-- List 3 good practices you should follow when creating SQL views for analytics dashboards, and for each, give a
-- one-line example related to a Flipkart sales reporting scenario.


-- Practice 1:
-- Select only the columns required by the dashboard.
-- Example: Flipkart sales dashboard should return
-- date, product, category, quantity and revenue,
-- instead of SELECT *.


-- Practice 2:
-- Use meaningful and consistent column names.
-- Example: Use total_revenue instead of an unclear
-- name such as col5 in a Flipkart sales report.


-- Practice 3:
-- Filter data when appropriate to improve performance.
-- Example: A Flipkart dashboard showing recent sales
-- can filter the view to the last 30 or 90 days.