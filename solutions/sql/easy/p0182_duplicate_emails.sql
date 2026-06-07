-- LeetCode 182: Duplicate Emails
-- Problem: https://leetcode.com/problems/duplicate-emails/
--
-- Table: Person
--
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | email       | varchar |
-- +-------------+---------+
--
-- Goal:
-- Return all email addresses that appear more than once.
-- The output column should be named Email.
--
-- Concept:
-- GROUP BY collects rows with the same email, and HAVING filters groups after
-- aggregation.

SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;

