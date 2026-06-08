-- LeetCode 183: Customers Who Never Order
-- Problem: https://leetcode.com/problems/customers-who-never-order/
--
-- Table: Customers
--
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- +-------------+---------+
--
-- Table: Orders
--
-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | id          | int  |
-- | customerId  | int  |
-- +-------------+------+
--
-- Goal:
-- Return the names of customers who never placed an order.
--
-- Expected output column name:
-- Customers
--
-- Hint:
-- Start from Customers, then find rows that have no matching order.
--
SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.customerId IS NULL;
