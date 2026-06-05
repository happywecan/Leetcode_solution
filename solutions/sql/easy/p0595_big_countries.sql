-- LeetCode 595: Big Countries
-- Problem: https://leetcode.com/problems/big-countries/
--
-- Table: World
--
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | name        | varchar |
-- | continent   | varchar |
-- | area        | int     |
-- | population  | int     |
-- | gdp         | bigint  |
-- +-------------+---------+
--
-- Goal:
-- Return the name, population, and area of countries that are considered big.
--
-- A country is big if:
-- - area is at least 3,000,000
-- - or population is at least 25,000,000
--
-- TODO: Write your query below.
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;