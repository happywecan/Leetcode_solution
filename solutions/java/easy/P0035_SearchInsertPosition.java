/**
 * LeetCode 35: Search Insert Position.
 *
 * Problem: https://leetcode.com/problems/search-insert-position/
 */
public class P0035_SearchInsertPosition {
    public int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length;

        while (left < right) {
            int middle = left + (right - left) / 2;

            if (nums[middle] < target) {
                left = middle + 1;
            } else {
                right = middle;
            }
        }

        return left;
    }

    public static void main(String[] args) {
        P0035_SearchInsertPosition solution = new P0035_SearchInsertPosition();
        System.out.println(solution.searchInsert(new int[] {1, 3, 5, 6}, 5)); // Expected: 2
        System.out.println(solution.searchInsert(new int[] {1, 3, 5, 6}, 2)); // Expected: 1
        System.out.println(solution.searchInsert(new int[] {1, 3, 5, 6}, 7)); // Expected: 4
        System.out.println(solution.searchInsert(new int[] {1, 3, 5, 6}, 0)); // Expected: 0
    }
}
