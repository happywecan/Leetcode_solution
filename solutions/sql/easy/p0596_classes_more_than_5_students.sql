-- LeetCode 596: Classes More Than 5 Students
-- Problem: https://leetcode.com/problems/classes-more-than-5-students/
--
-- Table: Courses
--
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | student     | varchar |
-- | class       | varchar |
-- +-------------+---------+
--
-- Goal:
-- Return all classes that have at least five students.
--
-- Concept:
-- GROUP BY collects rows with the same class, and HAVING filters groups after
-- counting their students.

SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;
