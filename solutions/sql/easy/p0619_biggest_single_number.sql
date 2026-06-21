-- LeetCode 619: Biggest Single Number
-- Problem: https://leetcode.com/problems/biggest-single-number/
--
-- Table: MyNumbers
--
-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | num         | int  |
-- +-------------+------+
--
-- Goal:
-- Return the largest number that appears exactly once. Return NULL if no
-- number appears exactly once.
--
-- Concept:
-- GROUP BY and HAVING find numbers that appear once. The outer MAX returns
-- the largest one and naturally returns NULL when the inner query is empty.

SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS single_numbers;
