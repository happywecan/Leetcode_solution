# 2026-06-08

## Java Problem

- Number: 283
- Title: Move Zeroes
- Link: https://leetcode.com/problems/move-zeroes/
- Difficulty: Easy
- Language: Java
- Attempt type: guided practice

## SQL Problem

- Number: 183
- Title: Customers Who Never Order
- Link: https://leetcode.com/problems/customers-who-never-order/
- Difficulty: Easy
- Language: SQL
- Attempt type: guided practice

## Review

- Java: Use a write pointer to keep the next position for a non-zero value.
  After all non-zero values are copied forward, fill the remaining positions
  with zeroes.
- SQL: Start from all customers, connect matching orders, then keep only the
  customers whose matching order side is missing.

## Complexity

- Java time: O(n)
- Java space: O(1)
- SQL concept: `LEFT JOIN` + `IS NULL`
