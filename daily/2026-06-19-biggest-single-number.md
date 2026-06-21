# 2026-06-19 - Biggest Single Number

## Problem

- Number: 619
- Title: Biggest Single Number
- Link: https://leetcode.com/problems/biggest-single-number/
- Difficulty: Easy
- Language: SQL
- Attempt type: completed with assistance

## Main Idea

題目要找的不是最大數字，而是「只出現一次的數字中最大的一個」。

假設資料是 `8, 8, 3, 3, 1, 4, 5, 6`：

1. 用 `GROUP BY num` 將相同數字放在同一組。
2. 用 `HAVING COUNT(*) = 1` 留下 `1, 4, 5, 6`。
3. 外層使用 `MAX(num)`，得到 `6`。

如果沒有任何數字只出現一次，內層查詢會是空集合，而外層 `MAX` 會回傳
`NULL`，正好符合題目要求。

## Final Query

```sql
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS single_numbers;
```

## SQL Concept

- `GROUP BY`：把相同的數字分成一組。
- `COUNT(*)`：計算每個數字出現幾次。
- `HAVING`：根據分組後的統計結果篩選群組。
- 子查詢：先取得單一數字，再讓外層查詢取最大值。
- `MAX`：空集合經過聚合後會得到 `NULL`。

## Mistakes To Avoid

- 直接寫 `MAX(num)`，這只會找整張表的最大值。
- 使用 `WHERE COUNT(*) = 1`；聚合條件必須寫在 `HAVING`。
- 在同一層同時要求「只出現一次」和取最大值，容易混淆分組層級。
- 用 `ORDER BY num DESC LIMIT 1` 時忽略空集合必須回傳一列 `NULL`。
