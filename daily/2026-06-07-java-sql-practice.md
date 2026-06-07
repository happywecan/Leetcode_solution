# 2026-06-07

## Java Problem

- Number: 20
- Title: Valid Parentheses
- Link: https://leetcode.com/problems/valid-parentheses/
- Difficulty: Easy
- Language: Java
- Attempt type: guided practice

## SQL Problem

- Number: 182
- Title: Duplicate Emails
- Link: https://leetcode.com/problems/duplicate-emails/
- Difficulty: Easy
- Language: SQL
- Attempt type: guided practice

## Review

- Java: Use a stack to remember the closing bracket expected by each opening
  bracket. A closing bracket is valid only when it matches the latest expected
  closing bracket.
- SQL: Use `GROUP BY` to collect identical emails and `HAVING` to filter groups
  whose count is greater than one.

## Complexity

- Java time: O(n)
- Java space: O(n)
- SQL concept: `GROUP BY` + `HAVING COUNT(*)`
