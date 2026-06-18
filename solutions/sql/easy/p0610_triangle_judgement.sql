-- LeetCode 610: Triangle Judgement
-- Problem: https://leetcode.com/problems/triangle-judgement/
--
-- Table: Triangle
--
-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | x           | int  |
-- | y           | int  |
-- | z           | int  |
-- +-------------+------+
--
-- Goal:
-- Report whether the three line segments can form a triangle.
--
-- Concept:
-- Use CASE to return different text based on the triangle inequality rule.

SELECT
    x,
    y,
    z,
    CASE
        WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;
