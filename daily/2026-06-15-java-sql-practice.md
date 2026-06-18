# 2026-06-15

## Java Problem

- Number: 88
- Title: Merge Sorted Array
- Link: https://leetcode.com/problems/merge-sorted-array/
- Difficulty: Easy
- Language: Java
- Attempt type: guided practice

## SQL Problem

- Number: 1757
- Title: Recyclable and Low Fat Products
- Link: https://leetcode.com/problems/recyclable-and-low-fat-products/
- Difficulty: Easy
- Language: SQL
- Attempt type: guided practice

## Java Thinking

直覺上，兩個陣列都已經排序好了，所以我們只需要一直拿「目前最大的數字」放到最後面。

這題的陷阱是 `nums1` 前面有真正資料，後面有空位。如果從前面開始合併，可能會把 `nums1` 還沒比較的數字覆蓋掉。因此比較安全的做法是從後面開始放：

- `first` 指向 `nums1` 真正資料的最後一個位置
- `second` 指向 `nums2` 的最後一個位置
- `write` 指向 `nums1` 最後一個可寫入的位置

每次比較 `nums1[first]` 和 `nums2[second]`，誰比較大就放到 `nums1[write]`，然後對應的指標往左移。

例如 `nums1 = [1, 2, 3, 0, 0, 0]`、`nums2 = [2, 5, 6]`：

- 先比較 `3` 和 `6`，放 `6` 到最後
- 再比較 `3` 和 `5`，放 `5`
- 再比較 `3` 和 `2`，放 `3`
- 最後補上剩下的 `2`

## Java Pattern

```java
int first = m - 1;
int second = n - 1;
int write = m + n - 1;

while (second >= 0) {
    if (first >= 0 && nums1[first] > nums2[second]) {
        nums1[write] = nums1[first];
        first--;
    } else {
        nums1[write] = nums2[second];
        second--;
    }
    write--;
}
```

## SQL Thinking

這題要找同時符合兩個條件的產品：

- `low_fats = 'Y'`
- `recyclable = 'Y'`

因為兩個條件都必須成立，所以使用 `AND`。如果用 `OR`，就會把「只有低脂」或「只有可回收」的產品也選進來，答案會太多。

## SQL Pattern

```sql
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
```

## Complexity

- Java time: O(m + n)
- Java space: O(1)
- SQL concept: `WHERE` + `AND`

## Mistakes To Avoid

- Java: 不要從前面開始寫入，否則可能覆蓋 `nums1` 還沒比較的資料。
- Java: 迴圈只需要檢查 `second >= 0`，因為如果 `nums2` 都放完，剩下的 `nums1` 原本就在正確位置。
- Java: 要先確認 `first >= 0`，才能讀 `nums1[first]`。
- SQL: 這題需要兩個條件同時成立，不能用 `OR`。
- SQL: 字串值要寫成 `'Y'`，不要寫成沒有引號的 `Y`。
