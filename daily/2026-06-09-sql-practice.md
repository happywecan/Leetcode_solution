# 2026-06-09 SQL

## SQL Problem

- Number: 197
- Title: Rising Temperature
- Link: https://leetcode.com/problems/rising-temperature/
- Difficulty: Easy
- Language: SQL
- Attempt type: guided practice

## Table

`Weather`

| Column | Meaning |
| --- | --- |
| `id` | row id |
| `recordDate` | date of the weather record |
| `temperature` | temperature on that date |

## Goal

Return the `id` for each day where the temperature is higher than the previous
day.

## Thinking

We need to compare two rows from the same table:

- one row is `today`
- one row is `yesterday`

That means this is a self join.

## Final Query

```sql
SELECT today.id
FROM Weather today
JOIN Weather yesterday
ON DATEDIFF(today.recordDate, yesterday.recordDate) = 1
WHERE today.temperature > yesterday.temperature;
```

## Why It Works

`DATEDIFF(today.recordDate, yesterday.recordDate) = 1` keeps only pairs where
`today` is exactly one day after `yesterday`.

Then:

```sql
WHERE today.temperature > yesterday.temperature
```

keeps only the rows where the temperature increased.

## Key Pattern

When one row must be compared with another row in the same table, use a self
join:

```sql
FROM SomeTable a
JOIN SomeTable b
ON ...
```

## Review Next

Practice reading aliases out loud:

- `today` means the current row we might return
- `yesterday` means the row one day before it
