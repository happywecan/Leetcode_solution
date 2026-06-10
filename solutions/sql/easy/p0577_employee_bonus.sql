-- LeetCode 577: Employee Bonus
-- Problem: https://leetcode.com/problems/employee-bonus/
--
-- Table: Employee
--
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | empId       | int     |
-- | name        | varchar |
-- | supervisor  | int     |
-- | salary      | int     |
-- +-------------+---------+
--
-- Table: Bonus
--
-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | empId       | int  |
-- | bonus       | int  |
-- +-------------+------+
--
-- Goal:
-- Return the name and bonus of each employee whose bonus is less than 1000.
-- Employees without a bonus should also be returned.
--
-- Concept:
-- Use LEFT JOIN to keep employees with no matching bonus row.

SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b
ON e.empid = b.empid
WHERE b.bonus IS NULL OR b.bonus<1000;

