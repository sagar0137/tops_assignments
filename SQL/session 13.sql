
-- SESSION 13 

-- Create a table called Orders with columns: order_id, user_id, order_amount, and app_name (e.g., 'Zomato', 'Swiggy', 'Flipkart'). Insert at least 10 sample records with different users and apps. Write an SQL query using the OVER() function to display each order's amount along with the total order amount for all orders


CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    order_amount DECIMAL(10,2),
    app_name VARCHAR(50)
);


-- Insert 10 sample orders
INSERT INTO Orders (order_id, user_id, order_amount, app_name)
VALUES
(1, 101, 450.00, 'Zomato'),
(2, 102, 700.00, 'Swiggy'),
(3, 101, 300.00, 'Zomato'),
(4, 103, 1200.00, 'Flipkart'),
(5, 102, 550.00, 'Swiggy'),
(6, 104, 900.00, 'Zomato'),
(7, 103, 650.00, 'Flipkart'),
(8, 101, 800.00, 'Swiggy'),
(9, 104, 400.00, 'Zomato'),
(10, 102, 1000.00, 'Flipkart');


-- Display each order's amount along with
-- total amount of all orders
SELECT order_id,
       user_id,
       order_amount,
       app_name,
       SUM(order_amount) OVER() AS total_order_amount
FROM Orders;



-- QUESTION 2
-- Using the Orders table, write an SQL query to show each user's order_id, order_amount, and the average order_amount for that user using the OVER(PARTITION BY user_id) clause.<br><br><em><strong>Hint:</strong> Use AVG(order_amount) OVER(PARTITION BY user_id) to get the per-user average.</em>


SELECT user_id,
       order_id,
       order_amount,
       AVG(order_amount) OVER(
           PARTITION BY user_id
       ) AS user_average_order
FROM Orders;



-- QUESTION 3
-- Suppose you have a table called Playlist with columns: song_id, user_id, and duration_sec. Write an SQL query to display each song's duration, and the total duration of songs added by each user using SUM(duration_sec) OVER(PARTITION BY user_id).


CREATE TABLE Playlist (
    song_id INT,
    user_id INT,
    duration_sec INT
);


-- Insert sample playlist data
INSERT INTO Playlist (song_id, user_id, duration_sec)
VALUES
(101, 1, 240),
(102, 1, 300),
(103, 1, 210),
(104, 2, 250),
(105, 2, 320),
(106, 3, 200),
(107, 3, 280),
(108, 3, 350);


-- Display each song duration and
-- total duration for that user
SELECT song_id,
       user_id,
       duration_sec,
       SUM(duration_sec) OVER(
           PARTITION BY user_id
       ) AS total_user_duration
FROM Playlist;



-- QUESTION 4
-- Given a table named MovieRatings with columns: rating_id, user_id, movie_name, and rating (1-5), write an SQL query to show each rating, the average rating per movie, and the difference between the user's rating and the movie's average rating using window functions.<br><br><em><strong>Hint:</strong> Use AVG(rating) OVER(PARTITION BY movie_name) and subtract it from the user's rating.</em>


CREATE TABLE MovieRatings (
    rating_id INT PRIMARY KEY,
    user_id INT,
    movie_name VARCHAR(100),
    rating DECIMAL(2,1)
);


-- Insert sample ratings
INSERT INTO MovieRatings (rating_id, user_id, movie_name, rating)
VALUES
(1, 101, 'Dangal', 5),
(2, 102, 'Dangal', 4),
(3, 103, 'Dangal', 3),
(4, 104, 'KGF', 5),
(5, 105, 'KGF', 4),
(6, 106, 'KGF', 4),
(7, 107, 'Pushpa', 5),
(8, 108, 'Pushpa', 3),
(9, 109, 'Pushpa', 4);


-- Display user's rating, movie average,
-- and difference from movie average
SELECT rating_id,
       user_id,
       movie_name,
       rating,
       AVG(rating) OVER(
           PARTITION BY movie_name
       ) AS movie_average_rating,

       rating - AVG(rating) OVER(
           PARTITION BY movie_name
       ) AS rating_difference

FROM MovieRatings;
