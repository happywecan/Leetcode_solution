/**
 * LeetCode 136: Single Number.
 *
 * Problem: https://leetcode.com/problems/single-number/
 *
 * Time: O(n)
 * Space: O(1)
 *
 * Note: Reviewed with assistance on 2026-06-09.
 */
public class P0136_SingleNumber {
    public int singleNumber(int[] nums) {
        int result = 0;

        for (int number : nums) {
            result ^= number;
        }

        return result;
    }

    public static void main(String[] args) {
        P0136_SingleNumber solution = new P0136_SingleNumber();

        System.out.println(solution.singleNumber(new int[] {2, 2, 1}));       // Expected: 1
        System.out.println(solution.singleNumber(new int[] {4, 1, 2, 1, 2})); // Expected: 4
        System.out.println(solution.singleNumber(new int[] {1}));             // Expected: 1
    }
}
