import java.util.HashMap;
import java.util.Map;

/**
 * LeetCode 169: Majority Element.
 *
 * Problem: https://leetcode.com/problems/majority-element/
 *
 * Time: O(n)
 * Space: O(n)
 *
 * Note: Completed with assistance on 2026-06-19.
 */
public class P0169_MajorityElement {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();

        for (int number : nums) {
            int previousCount = counts.getOrDefault(number, 0);
            int updatedCount = previousCount + 1;
            counts.put(number, updatedCount);

            if (updatedCount > nums.length / 2) {
                return number;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        P0169_MajorityElement solution = new P0169_MajorityElement();

        System.out.println(solution.majorityElement(new int[] {3, 2, 3}));             // Expected: 3
        System.out.println(solution.majorityElement(new int[] {2, 2, 1, 1, 1, 2, 2})); // Expected: 2
    }
}
