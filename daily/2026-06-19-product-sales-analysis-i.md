# 2026-06-19 - Product Sales Analysis I

## Problem

- Number: 1068
- Title: Product Sales Analysis I
- Link: https://leetcode.com/problems/product-sales-analysis-i/
- Difficulty: Easy
- Language: SQL
- Attempt type: solved after a hint

## Main Idea

`Sales` 表提供銷售年份和價格，`Product` 表提供商品名稱。
兩張表都有 `product_id`，因此使用它連接同一項商品的資料。

## Final Query

```sql
SELECT
    p.product_name,
    s.year,
    s.price
FROM Sales AS s
JOIN Product AS p
    ON s.product_id = p.product_id;
```

## SQL Concept

- `JOIN`：保留兩張表中能成功配對的資料。
- `ON`：指定兩張表的配對條件。
- `s` 和 `p`：表格別名，用來標示欄位來源。

## Mistakes To Avoid

- 使用兩張表共同的 `product_id` 作為連接條件。
- `product_name` 來自 `Product`。
- `year` 和 `price` 來自 `Sales`。
- 不要省略 `ON` 條件，否則會產生錯誤的資料組合。
