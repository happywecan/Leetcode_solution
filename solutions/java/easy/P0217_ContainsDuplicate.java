import java.util.HashSet;
import java.util.Set;

/**
 * LeetCode 217: Contains Duplicate.
 *
 * Problem: https://leetcode.com/problems/contains-duplicate/
 */
public class P0217_ContainsDuplicate {
    public boolean containsDuplicate(int[] nums) {
        // Time: O(n), Space: O(n)
        Set<Integer> seen = new HashSet<>();
        for (int number : nums) {
            if (!seen.add(number)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        P0217_ContainsDuplicate solution = new P0217_ContainsDuplicate();
        System.out.println(solution.containsDuplicate(new int[] {1, 2, 3, 1}));
        System.out.println(solution.containsDuplicate(new int[] {1, 2, 3, 4}));
    }
}
