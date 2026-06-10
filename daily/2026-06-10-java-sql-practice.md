# 2026-06-10

## Java Problem

- Number: 206
- Title: Reverse Linked List
- Link: https://leetcode.com/problems/reverse-linked-list/
- Difficulty: Easy
- Language: Java
- Attempt type: guided practice

## SQL Problem

- Number: 577
- Title: Employee Bonus
- Link: https://leetcode.com/problems/employee-bonus/
- Difficulty: Easy
- Language: SQL
- Attempt type: guided practice

## Java Thinking

We need to reverse the direction of every `next` pointer.

Use three references:

- `previous`: the node that should come before `current`
- `current`: the node we are changing now
- `nextNode`: the original next node, saved before we change the link

For each node:

```text
save next
current.next = previous
move previous forward
move current forward
```

When `current` becomes `null`, `previous` is the new head.

## Java Pattern

```java
ListNode previous = null;
ListNode current = head;

while (current != null) {
    ListNode nextNode = current.next;
    current.next = previous;
    previous = current;
    current = nextNode;
}

return previous;
```

## SQL Thinking

We need employees whose bonus is less than `1000`, and employees with no bonus
also count.

That means:

- Start from `Employee`
- Use `LEFT JOIN` to keep employees even when they do not have a row in `Bonus`
- Keep rows where `bonus < 1000` or `bonus IS NULL`

## SQL Pattern

```sql
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b
ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
```

## Complexity

- Java time: O(n)
- Java space: O(1)
- SQL concept: `LEFT JOIN` + `IS NULL`

## Mistakes To Avoid

- Java: Do not overwrite `current.next` before saving the original next node.
- SQL: Do not use `INNER JOIN`, because employees without bonus rows would be
  removed too early.
