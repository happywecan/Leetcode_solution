import java.util.HashMap;
import java.util.Map;

/**
 * LeetCode 205: Isomorphic Strings.
 *
 * Problem: https://leetcode.com/problems/isomorphic-strings/
 *
 * Time: O(n)
 * Space: O(k), where k is the number of distinct characters.
 *
 * Note: Completed with assistance on 2026-06-19.
 */
public class P0205_IsomorphicStrings {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

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

        return true;
    }

    public static void main(String[] args) {
        P0205_IsomorphicStrings solution = new P0205_IsomorphicStrings();

        System.out.println(solution.isIsomorphic("egg", "add"));     // Expected: true
        System.out.println(solution.isIsomorphic("foo", "bar"));     // Expected: false
        System.out.println(solution.isIsomorphic("badc", "baba"));   // Expected: false
    }
}
