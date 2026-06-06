-- LeetCode 181: Employees Earning More Than Their Managers
-- Problem: https://leetcode.com/problems/employees-earning-more-than-their-managers/
--
-- Table: Employee
--
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- | salary      | int     |
-- | managerId   | int     |
-- +-------------+---------+
--
-- Goal:
-- Return the names of employees whose salary is greater than their manager's salary.
-- The output column should be named Employee.

SELECT e.name AS Employee
FROM Employee e
JOIN Employee m
ON e.managerId = m.id
WHERE e.salary > m.salary;
