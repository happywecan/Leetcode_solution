# LeetCode Practice Log

Daily data-structure and algorithm practice in Python.

This repository is a public learning log. It records reviewed solutions,
implementation notes, and older drafts so progress remains visible over time.
The goal is consistent practice and clear reasoning, not a claim that every
solution was written without references or tooling assistance.

## Repository Structure

```text
solutions/python/       Reviewed LeetCode solutions
solutions/java/         Reviewed Java LeetCode solutions
solutions/sql/          Reviewed SQL solutions
tests/                  Regression tests for reviewed solutions
daily/                  Daily practice notes
dsa/udemy/              Data-structure course exercises
scripts/new_problem.py   Creates a daily note and solution template
```

## Reviewed Solutions

| # | Problem | Difficulty | Solution |
| ---: | --- | --- | --- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | [Python](solutions/python/easy/p0001_two_sum.py) / [Java](solutions/java/easy/P0001_TwoSum.java) |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Easy | [Python](solutions/python/easy/p0009_palindrome_number.py) |
| 13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | Easy | [Python](solutions/python/easy/p0013_roman_to_integer.py) |
| 14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | Easy | [Python](solutions/python/easy/p0014_longest_common_prefix.py) |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | [Python](solutions/python/easy/p0020_valid_parentheses.py) / [Java](solutions/java/easy/P0020_ValidParentheses.java) |
| 35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | [Python](solutions/python/easy/p0035_search_insert_position.py) |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | [Python](solutions/python/easy/p0121_best_time_to_buy_and_sell_stock.py) |
| 136 | [Single Number](https://leetcode.com/problems/single-number/) | Easy | [Python](solutions/python/easy/p0136_single_number.py) |
| 182 | [Duplicate Emails](https://leetcode.com/problems/duplicate-emails/) | Easy | [SQL](solutions/sql/easy/p0182_duplicate_emails.sql) |
| 183 | [Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/) | Easy | [SQL](solutions/sql/easy/p0183_customers_who_never_order.sql) |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | [Python](solutions/python/easy/p0217_contains_duplicate.py) / [Java](solutions/java/easy/P0217_ContainsDuplicate.java) |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | [Python](solutions/python/easy/p0242_valid_anagram.py) |
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | [Python](solutions/python/easy/p0283_move_zeroes.py) / [Java](solutions/java/easy/P0283_MoveZeroes.java) |
| 344 | [Reverse String](https://leetcode.com/problems/reverse-string/) | Easy | [Python](solutions/python/easy/p0344_reverse_string.py) |
| 704 | [Binary Search](https://leetcode.com/problems/binary-search/) | Easy | [Java](solutions/java/easy/P0704_BinarySearch.java) |
| 876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy | [Python](solutions/python/easy/p0876_middle_of_the_linked_list.py) |

## Daily Workflow

### Python

Create a Python template for the day's problem:

```bash
python3 scripts/new_problem.py 3 longest-substring-without-repeating-characters medium
```

Place reviewed Python solutions here:

```text
solutions/python/<difficulty>/p<number>_<problem_slug>.py
```

Example:

```text
solutions/python/easy/p0001_two_sum.py
```

### Java

Place reviewed Java solutions here:

```text
solutions/java/<difficulty>/P<number>_<ProblemName>.java
```

Example:

```text
solutions/java/easy/P0001_TwoSum.java
```

Use one class per file. Keep the explanation, time complexity, and space
complexity near the implementation.

### Practice Loop

Then:

1. Write down the initial approach before looking up a solution.
2. Choose Python or Java and implement or review the algorithm.
3. Record complexity and mistakes in `daily/YYYY-MM-DD-<problem>.md`.
4. Add tests when promoting a solution into `solutions/python/`.
5. Commit the daily progress.

```bash
python3 -m unittest discover -s tests -v  # Run when Python solutions changed
git add .
git commit -m "Practice: <problem name>"
git push origin main
```

Java can start with direct compilation:

```bash
javac solutions/java/<difficulty>/<FILE>.java
java -cp solutions/java/<difficulty> <CLASS_NAME>
```

When the Java solution count grows, add a small Maven or Gradle test project.
Do not add build tooling before it solves a real maintenance problem.

### SQL

Place reviewed SQL solutions here:

```text
solutions/sql/<difficulty>/p<number>_<problem_slug>.sql
```

Example:

```text
solutions/sql/easy/p0175_combine_two_tables.sql
```

Each file should include the problem link, the final query, and a short note
about the SQL concept used, such as `LEFT JOIN`, `GROUP BY`, or a window
function.

## Assistance Policy

References, discussions, and AI tools may be used for review. Daily notes
should state whether a solution was solved independently, completed after a
hint, or reviewed with assistance. The useful signal is the reasoning,
correction process, and ability to explain the final implementation.
