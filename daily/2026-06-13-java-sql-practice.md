# 2026-06-13

## Java Problem

- Number: 26
- Title: Remove Duplicates from Sorted Array
- Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
- Difficulty: Easy
- Language: Java
- Attempt type: guided practice

## SQL Problem

- Number: 596
- Title: Classes More Than 5 Students
- Link: https://leetcode.com/problems/classes-more-than-5-students/
- Difficulty: Easy
- Language: SQL
- Attempt type: guided practice

## Java Thinking

題目給的是已排序陣列，所以重複的數字一定會靠在一起。

我們只需要保留每一段重複數字的第一個值。可以用兩個位置：

- `readIndex`：一路往右看目前的數字
- `writeIndex`：下一個不重複數字要放的位置

如果 `nums[readIndex]` 跟前一格不同，代表遇到新的數字，就把它寫到
`writeIndex`，再把 `writeIndex` 往右移。

例如 `[0, 0, 1, 1, 2]`：

- 第一個 `0` 已經保留
- 第二個 `0` 跟前一格一樣，跳過
- 第一個 `1` 跟前一格不同，放到前面
- 第二個 `1` 跳過
- `2` 跟前一格不同，放到前面

最後前 `k` 個位置就是答案。

## Java Pattern

```java
int writeIndex = 1;

for (int readIndex = 1; readIndex < nums.length; readIndex++) {
    if (nums[readIndex] != nums[readIndex - 1]) {
        nums[writeIndex] = nums[readIndex];
        writeIndex++;
    }
}

return writeIndex;
```

## SQL Thinking

題目要找「至少 5 位學生」的課程。

每一列代表一位學生選了一門課，所以要先用 `GROUP BY class` 把同一門課分成
同一組，再用 `COUNT(student)` 計算每一組有幾位學生。

因為 `WHERE` 是在分組前過濾資料，不能直接用來判斷每組的人數。分組後的條件要
寫在 `HAVING`。

## SQL Pattern

```sql
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;
```

## Complexity

- Java time: O(n)
- Java space: O(1)
- SQL concept: `GROUP BY` + `HAVING` + `COUNT`

## Mistakes To Avoid

- Java: 不要另外建立新陣列，題目要求在原陣列前段改出答案。
- Java: 回傳的是不重複元素數量 `k`，不是整個陣列。
- Java: 因為陣列已排序，判斷是否重複只要跟前一格比較。
- SQL: 聚合後的條件要用 `HAVING COUNT(...) >= 5`，不是 `WHERE COUNT(...) >= 5`。
- SQL: 題目是至少 5 位學生，所以條件要包含等於 5。
