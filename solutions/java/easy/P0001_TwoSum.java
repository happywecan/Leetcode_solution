import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * LeetCode 1: Two Sum.
 *
 * Problem: https://leetcode.com/problems/two-sum/
 */
public class P0001_TwoSum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int number = nums[i];
            int complement = target - number;

            if (numMap.containsKey(complement)) {
                return new int[] {numMap.get(complement), i};
            }

            numMap.put(number, i);
        }

        return new int[] {};
    }

    public static void main(String[] args) {
        P0001_TwoSum solution = new P0001_TwoSum();
        System.out.println(Arrays.toString(solution.twoSum(new int[] {2, 7, 11, 15}, 9))); // Expected: [0, 1]
        System.out.println(Arrays.toString(solution.twoSum(new int[] {3, 2, 4}, 6)));       // Expected: [1, 2]
    }
}
