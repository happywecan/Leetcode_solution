/**
 * LeetCode 27: Remove Element.
 *
 * Problem: https://leetcode.com/problems/remove-element/
 */
public class P0027_RemoveElement {
    public int removeElement(int[] nums, int val) {
        int writeIndex = 0;

        for (int readIndex = 0; readIndex < nums.length; readIndex++) {
            if (nums[readIndex] != val) {
                nums[writeIndex] = nums[readIndex];
                writeIndex++;
            }
        }

        return writeIndex;
    }

    public static void main(String[] args) {
        P0027_RemoveElement solution = new P0027_RemoveElement();

        int[] first = new int[] {3, 2, 2, 3};
        int firstLength = solution.removeElement(first, 3);
        printPrefix(first, firstLength); // Expected: [2, 2]

        int[] second = new int[] {0, 1, 2, 2, 3, 0, 4, 2};
        int secondLength = solution.removeElement(second, 2);
        printPrefix(second, secondLength); // Expected: [0, 1, 3, 0, 4]
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
