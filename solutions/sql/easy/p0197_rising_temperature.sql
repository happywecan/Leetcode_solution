-- LeetCode 197: Rising Temperature
-- Problem: https://leetcode.com/problems/rising-temperature/
--
-- Table: Weather
--
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | recordDate    | date    |
-- | temperature   | int     |
-- +---------------+---------+
--
-- Goal:
-- Return the ids of dates whose temperature is higher than the previous day.
--
-- Concept:
-- Use a self join to compare each row with the row from one day before.

SELECT today.id
FROM Weather today
JOIN Weather yesterday
ON DATEDIFF(today.recordDate, yesterday.recordDate) = 1
WHERE today.temperature > yesterday.temperature;