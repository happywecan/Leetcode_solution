# 2026-06-11

## Java Problem

- Number: 344
- Title: Reverse String
- Link: https://leetcode.com/problems/reverse-string/
- Difficulty: Easy
- Language: Java
- Attempt type: guided practice

## SQL Problem

- Number: 584
- Title: Find Customer Referee
- Link: https://leetcode.com/problems/find-customer-referee/
- Difficulty: Easy
- Language: SQL
- Attempt type: guided practice

## Java Thinking

We need to reverse the array in place, so we should not create another array.

Use two pointers:

- `left`: starts at the first character
- `right`: starts at the last character

At each step:

```text
swap s[left] and s[right]
move left one step right
move right one step left
```

Stop when `left >= right`, because every pair has already been swapped.

## Java Pattern

```java
int left = 0;
int right = s.length - 1;

while (left < right) {
    char temp = s[left];
    s[left] = s[right];
    s[right] = temp;

    left++;
    right--;
}
```

## SQL Thinking

We need customers who were not referred by customer `2`.

The tricky part is `NULL`:

- `referee_id <> 2` keeps values like `1`, `3`, and `4`
- `referee_id <> 2` does not keep `NULL`
- So we must add `OR referee_id IS NULL`

## SQL Pattern

```sql
SELECT name
FROM Customer
WHERE referee_id <> 2 OR referee_id IS NULL;
```

## Complexity

- Java time: O(n)
- Java space: O(1)
- SQL concept: `WHERE` + `NULL` handling

## Mistakes To Avoid

- Java: Do not use a new array; the problem asks for in-place mutation.
- Java: Move both pointers after each swap, or the loop will not progress.
- SQL: Do not write only `referee_id <> 2`, because that excludes `NULL` rows.
