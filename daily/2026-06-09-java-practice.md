# 2026-06-09

## Java Problem

- Number: 136
- Title: Single Number
- Link: https://leetcode.com/problems/single-number/
- Difficulty: Easy
- Language: Java
- Attempt type: guided practice

## First Thought

Use a `HashSet` or `HashMap` to count which value appears once.

That works, but it uses extra memory. The problem asks for linear time and
constant extra space, so we should look for a way to cancel duplicate values.

## Final Approach

Use XOR.

- `x ^ x = 0`
- `x ^ 0 = x`
- XOR order does not matter

Every duplicated value cancels itself out, and the only value left is the
single number.

Example:

```text
[4, 1, 2, 1, 2]

0 ^ 4 = 4
4 ^ 1 = 5
5 ^ 2 = 7
7 ^ 1 = 6
6 ^ 2 = 4
```

Answer: `4`

## Java Pattern

```java
int result = 0;

for (int number : nums) {
    result ^= number;
}

return result;
```

## Complexity

- Time: O(n)
- Space: O(1)

## Mistake To Avoid

Do not use addition or subtraction to cancel values. XOR is safer because it
does not depend on numeric size or risk integer overflow for this cancellation
pattern.

## Review Next

Practice one more bit-manipulation easy problem, or compare this with a
`HashMap` counting solution to understand the memory tradeoff.
