/**
 * LeetCode 344: Reverse String.
 *
 * Problem: https://leetcode.com/problems/reverse-string/
 *
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
public class P0344_ReverseString {
    public void reverseString(char[] s) {
        int left = 0;
        int right = s.length - 1;

        while (left < right) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;

            left++;
            right--;
        }
    }

    public static void main(String[] args) {
        P0344_ReverseString solution = new P0344_ReverseString();

        char[] first = new char[] {'h', 'e', 'l', 'l', 'o'};
        solution.reverseString(first);
        printArray(first); // Expected: [o, l, l, e, h]

        char[] second = new char[] {'H', 'a', 'n', 'n', 'a', 'h'};
        solution.reverseString(second);
        printArray(second); // Expected: [h, a, n, n, a, H]
    }

    private static void printArray(char[] s) {
        System.out.print("[");
        for (int i = 0; i < s.length; i++) {
            if (i > 0) {
                System.out.print(", ");
            }
            System.out.print(s[i]);
        }
        System.out.println("]");
    }
}
