import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

/**
 * LeetCode 20: Valid Parentheses.
 *
 * Problem: https://leetcode.com/problems/valid-parentheses/
 */
public class P0020_ValidParentheses {
    public boolean isValid(String s) {
        // Time: O(n), Space: O(n)
        Map<Character, Character> pairs = new HashMap<>();
        pairs.put('(', ')');
        pairs.put('[', ']');
        pairs.put('{', '}');

        Deque<Character> stack = new ArrayDeque<>();

        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);

            if (pairs.containsKey(current)) {
                stack.push(pairs.get(current));
            } else {
                if (stack.isEmpty() || stack.pop() != current) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }

    public static void main(String[] args) {
        P0020_ValidParentheses solution = new P0020_ValidParentheses();
        System.out.println(solution.isValid("()"));       // Expected: true
        System.out.println(solution.isValid("()[]{}"));   // Expected: true
        System.out.println(solution.isValid("(]"));       // Expected: false
        System.out.println(solution.isValid("([)]"));     // Expected: false
        System.out.println(solution.isValid("{[]}"));     // Expected: true
    }
}
