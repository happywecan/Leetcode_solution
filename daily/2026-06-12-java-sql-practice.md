# 2026-06-12

## Java Problem

- Number: 141
- Title: Linked List Cycle
- Link: https://leetcode.com/problems/linked-list-cycle/
- Difficulty: Easy
- Language: Java
- Attempt type: guided practice

## SQL Problem

- Number: 595
- Title: Big Countries
- Link: https://leetcode.com/problems/big-countries/
- Difficulty: Easy
- Language: SQL
- Attempt type: guided practice

## Extra SQL Problem

- Number: 1148
- Title: Article Views I
- Link: https://leetcode.com/problems/article-views-i/
- Difficulty: Easy
- Language: SQL
- Attempt type: guided practice

## Java Thinking

We need to know whether a linked list eventually points back to an earlier node.

Use two pointers:

- `slow`: moves one node at a time
- `fast`: moves two nodes at a time

If there is a cycle, the fast pointer will eventually catch the slow pointer.
If there is no cycle, the fast pointer will reach `null`.

## Java Pattern

```java
ListNode slow = head;
ListNode fast = head;

while (fast != null && fast.next != null) {
    slow = slow.next;
    fast = fast.next.next;

    if (slow == fast) {
        return true;
    }
}

return false;
```

## SQL Thinking

We need countries that are considered big by either area or population.

That means the condition is:

- `area >= 3000000`
- or `population >= 25000000`

Because either condition is enough, use `OR`.

## SQL Pattern

```sql
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;
```

## Extra SQL Thinking

We need authors who viewed their own articles.

That means the value in `author_id` must be the same as the value in
`viewer_id` on the same row.

Because the same author can view more than one own article, use `DISTINCT`.
Because the problem asks for ascending order, use `ORDER BY id`.

## Extra SQL Pattern

```sql
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;
```

## Complexity

- Java time: O(n)
- Java space: O(1)
- SQL concept: `WHERE` + `OR`
- Extra SQL concept: `DISTINCT` + column comparison + `ORDER BY`

## Mistakes To Avoid

- Java: Compare node references with `slow == fast`, not node values.
- Java: Check `fast != null && fast.next != null` before moving two steps.
- SQL: Use `OR`, not `AND`, because a country only needs to satisfy one rule.
- Extra SQL: Use `DISTINCT`, or the same author id may appear more than once.
