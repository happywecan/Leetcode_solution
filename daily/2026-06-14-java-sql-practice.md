# 2026-06-14

## Java Problem

- Number: 27
- Title: Remove Element
- Link: https://leetcode.com/problems/remove-element/
- Difficulty: Easy
- Language: Java
- Attempt type: guided practice

## SQL Problem

- Number: 610
- Title: Triangle Judgement
- Link: https://leetcode.com/problems/triangle-judgement/
- Difficulty: Easy
- Language: SQL
- Attempt type: guided practice

## Java Thinking

這題跟昨天的「把答案寫回陣列前面」很像。

差別是昨天要跳過重複值，今天要跳過指定的 `val`。

用兩個 index：

- `readIndex`：每一格都讀過，看目前數字是多少
- `writeIndex`：下一個要保留的數字要放的位置

如果 `nums[readIndex] == val`，代表這個數字要刪掉，所以什麼都不寫。
`readIndex` 還是會因為 `for` 迴圈繼續往右走。

如果 `nums[readIndex] != val`，代表這個數字要留下，就把它放到
`nums[writeIndex]`，然後 `writeIndex++`。

例如 `nums = [3, 2, 2, 3]`，`val = 3`：

- 看到第一個 `3`：要刪掉，跳過
- 看到 `2`：要留下，寫到第 0 格
- 看到第二個 `2`：要留下，寫到第 1 格
- 看到最後的 `3`：要刪掉，跳過

最後回傳 `2`，代表前兩格 `[2, 2]` 是答案。

## Java Pattern

```java
int writeIndex = 0;

for (int readIndex = 0; readIndex < nums.length; readIndex++) {
    if (nums[readIndex] != val) {
        nums[writeIndex] = nums[readIndex];
        writeIndex++;
    }
}

return writeIndex;
```

## SQL Thinking

三條邊要能組成三角形，任兩邊相加都要大於第三邊。

所以要同時滿足：

- `x + y > z`
- `x + z > y`
- `y + z > x`

只要其中一個不成立，就不能組成三角形。

SQL 裡可以用 `CASE` 做判斷：

- 條件成立時回傳 `'Yes'`
- 否則回傳 `'No'`

## SQL Pattern

```sql
SELECT
    x,
    y,
    z,
    CASE
        WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;
```

## Complexity

- Java time: O(n)
- Java space: O(1)
- SQL concept: `CASE` + triangle inequality

## Mistakes To Avoid

- Java: 相等於 `val` 的數字是跳過，不是把它設成 0。
- Java: 不管有沒有寫入，`readIndex` 都會繼續往右走。
- Java: 回傳的是保留下來的元素數量 `k`，不是被刪掉的數量。
- SQL: 三個不等式都要成立，所以要用 `AND`。
- SQL: 條件要是大於 `>`，不是大於等於 `>=`。
