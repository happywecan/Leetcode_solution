/**
 * LeetCode 26: Remove Duplicates from Sorted Array.
 *
 * Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
 */
public class P0026_RemoveDuplicatesFromSortedArray {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        int writeIndex = 1;

        for (int readIndex = 1; readIndex < nums.length; readIndex++) {
            if (nums[readIndex] != nums[readIndex - 1]) {
                nums[writeIndex] = nums[readIndex];
                writeIndex++;
            }
        }

        return writeIndex;
    }

    public static void main(String[] args) {
        P0026_RemoveDuplicatesFromSortedArray solution =
                new P0026_RemoveDuplicatesFromSortedArray();

        int[] first = new int[] {1, 1, 2};
        int firstLength = solution.removeDuplicates(first);
        printPrefix(first, firstLength); // Expected: [1, 2]

        int[] second = new int[] {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        int secondLength = solution.removeDuplicates(second);
        printPrefix(second, secondLength); // Expected: [0, 1, 2, 3, 4]
    }

    private static void printPrefix(int[] nums, int length) {
        System.out.print("[");
        for (int i = 0; i < length; i++) {
            if (i > 0) {
                System.out.print(", ");
            }
            System.out.print(nums[i]);
        }
        System.out.println("]");
    }
}
