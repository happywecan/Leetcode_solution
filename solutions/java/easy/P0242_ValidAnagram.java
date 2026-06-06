/**
 * LeetCode 242: Valid Anagram.
 *
 * Problem: https://leetcode.com/problems/valid-anagram/
 */
public class P0242_ValidAnagram {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }

        int [] counts = new int[26];

        for (int i = 0; i < s.length(); i++) {
            char letter = s.charAt(i);
            int index = letter - 'a';
            counts[index] = counts[index] + 1;
        }

        for (int i = 0; i < t.length(); i++) {
            char letter = t.charAt(i);
            int index = letter - 'a';
            counts[index] = counts[index] - 1;
        }

        for (int i = 0; i < counts.length; i++) {
            if (counts[i] != 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        P0242_ValidAnagram solution = new P0242_ValidAnagram();
        System.out.println(solution.isAnagram("anagram", "nagaram")); // Expected: true
        System.out.println(solution.isAnagram("rat", "car"));         // Expected: false
    }
}
