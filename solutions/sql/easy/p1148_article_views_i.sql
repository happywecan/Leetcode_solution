-- LeetCode 1148: Article Views I
-- Problem: https://leetcode.com/problems/article-views-i/
--
-- Table: Views
--
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | article_id    | int     |
-- | author_id     | int     |
-- | viewer_id     | int     |
-- | view_date     | date    |
-- +---------------+---------+
--
-- Goal:
-- Return the ids of authors who viewed at least one of their own articles.
-- Results should be sorted by id in ascending order.
--
-- Concept:
-- Use WHERE to compare two columns in the same row, DISTINCT to remove
-- duplicate author ids, and ORDER BY to sort the result.


SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;
