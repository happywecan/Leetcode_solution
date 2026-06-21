# 2026-06-19 - Isomorphic Strings

## Problem

- Number: 205
- Title: Isomorphic Strings
- Link: https://leetcode.com/problems/isomorphic-strings/
- Difficulty: Easy
- Language: Java
- Attempt type: completed with assistance

## Main Idea

兩個字串同構，代表每個字元都必須維持固定而且一對一的對應。

以 `s = "egg"`、`t = "add"` 為例：

1. `e` 對應 `a`
2. 第一個 `g` 對應 `d`
3. 第二個 `g` 仍然對應 `d`

因此結果是 `true`。

只建立 `s → t` 的對應還不夠。例如 `"badc"` 和 `"baba"` 中，`a` 與
`d` 都會想對應到 `a`。所以還要建立 `t → s` 的反向對應，確保不同字元
不會共用同一個目標字元。

## Final Pattern

```java
Map<Character, Character> sToT = new HashMap<>();
Map<Character, Character> tToS = new HashMap<>();

for (int i = 0; i < s.length(); i++) {
    char source = s.charAt(i);
    char target = t.charAt(i);

    if (sToT.containsKey(source) && sToT.get(source) != target) {
        return false;
    }

    if (tToS.containsKey(target) && tToS.get(target) != source) {
        return false;
    }

    sToT.put(source, target);
    tToS.put(target, source);
}
```

## Complexity

- Time: O(n)
- Space: O(k)，`k` 是不同字元的數量

## Mistakes To Avoid

- 只檢查單向映射，漏掉兩個來源字元對應到同一個目標字元。
- 遇到已存在的字元時直接覆蓋舊映射，應先確認新舊映射是否一致。
- 忘記兩個字串長度不同時不可能同構。
- 把「字元出現次數相同」誤認為同構；同構還要求位置上的對應一致。
