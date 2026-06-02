/**
 * LeetCode 704: Binary Search.
 *
 * Problem: https://leetcode.com/problems/binary-search/
 */
public class P0704_BinarySearch {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int middle = left + (right - left) / 2;

            if (nums[middle] == target) {
                return middle;
            }

            if (nums[middle] < target) {
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        P0704_BinarySearch solution = new P0704_BinarySearch();
        System.out.println(solution.search(new int[] {-1, 0, 3, 5, 9, 12}, 9)); // Expected: 4
        System.out.println(solution.search(new int[] {-1, 0, 3, 5, 9, 12}, 2)); // Expected: -1
    }
}
