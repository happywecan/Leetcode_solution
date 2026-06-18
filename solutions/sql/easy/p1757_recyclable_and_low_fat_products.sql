-- LeetCode 1757: Recyclable and Low Fat Products
-- Problem: https://leetcode.com/problems/recyclable-and-low-fat-products/
--
-- Table: Products
--
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | product_id  | int     |
-- | low_fats    | enum    |
-- | recyclable  | enum    |
-- +-------------+---------+
--
-- Goal:
-- Return the ids of products that are both low fat and recyclable.
--
-- Concept:
-- Use WHERE with AND because both conditions must be true.

SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
