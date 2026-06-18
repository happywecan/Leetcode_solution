-- LeetCode 1068: Product Sales Analysis I
-- Problem: https://leetcode.com/problems/product-sales-analysis-i/
--
-- Table: Sales
--
-- +------------+-------+
-- | Column     | Type  |
-- +------------+-------+
-- | sale_id    | int   |
-- | product_id | int   |
-- | year       | int   |
-- | quantity   | int   |
-- | price      | int   |
-- +------------+-------+
--
-- Table: Product
--
-- +--------------+---------+
-- | Column       | Type    |
-- +--------------+---------+
-- | product_id   | int     |
-- | product_name | varchar |
-- +--------------+---------+
--
-- Goal:
-- Return product_name, year, and price for every sale.
--
-- Concept:
-- Join Sales and Product using their shared product_id.
--
-- Practice status: Solved after a hint on 2026-06-19.

SELECT
    p.product_name,
    s.year,
    s.price
FROM Sales AS s
JOIN Product AS p
    ON s.product_id = p.product_id;
