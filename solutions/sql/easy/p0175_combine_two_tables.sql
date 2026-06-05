-- LeetCode 175: Combine Two Tables
-- Problem: https://leetcode.com/problems/combine-two-tables/
--
-- Table: Person
--
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | personId    | int     |
-- | lastName    | varchar |
-- | firstName   | varchar |
-- +-------------+---------+
--
-- Table: Address
--
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | addressId   | int     |
-- | personId    | int     |
-- | city        | varchar |
-- | state       | varchar |
-- +-------------+---------+
--
-- Goal:
-- Return each person's firstName, lastName, city, and state.
-- If a person has no address, still return that person with null city/state.
--
-- TODO: Write your query below.
SELECT
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a
ON p.personId = a.personId
ORDER BY p.personId