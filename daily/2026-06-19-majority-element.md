# 2026-06-19 - Majority Element

## Problem

- Number: 169
- Title: Majority Element
- Link: https://leetcode.com/problems/majority-element/
- Difficulty: Easy
- Language: Java
- Attempt type: completed with assistance

## Main Idea

使用 `HashMap` 記錄每個數字出現的次數。

每讀到一個數字，就把它目前的次數加一。如果新的次數大於陣列長度的一半，
這個數字就是多數元素，可以立刻回傳。

例如 `nums = [3, 2, 3]`：

1. 讀到 `3`，次數變成 `1`。
2. 讀到 `2`，次數變成 `1`。
3. 再讀到 `3`，次數變成 `2`。
4. 因為 `2 > 3 / 2`，所以答案是 `3`。

## Final Pattern

```java
Map<Integer, Integer> counts = new HashMap<>();

for (int number : nums) {
    int previousCount = counts.getOrDefault(number, 0);
    int updatedCount = previousCount + 1;
    counts.put(number, updatedCount);

    if (updatedCount > nums.length / 2) {
        return number;
    }
}
```

`getOrDefault(number, 0)` 的意思是：

- Map 裡已經有 `number`：取得原本的次數。
- Map 裡還沒有 `number`：先使用預設值 `0`。

## Complexity

- Time: O(n)
- Space: O(n)

## Mistakes To Avoid

- 新數字第一次出現時，初始次數應該從 `0 + 1` 變成 `1`。
- 更新後要把新次數存回 `HashMap`。
- 題目要求「超過一半」，所以判斷要使用 `>`，不是 `>=`。
- `nums.length / 2` 是整數除法，這正好符合題目的判斷方式。
