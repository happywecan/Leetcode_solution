/**
 * LeetCode 283: Move Zeroes.
 *
 * Problem: https://leetcode.com/problems/move-zeroes/
 */
public class P0283_MoveZeroes {
    public void moveZeroes(int[] nums) {
        int writeIndex = 0;

        for (int number : nums) {
            if (number != 0) {
                nums[writeIndex] = number;
                writeIndex++;
            }
        }

        for (int i = writeIndex; i < nums.length; i++) {
            nums[i] = 0;
        }
    }

    public static void main(String[] args) {
        P0283_MoveZeroes solution = new P0283_MoveZeroes();

        int[] first = new int[] {0, 1, 0, 3, 12};
        solution.moveZeroes(first);
        printArray(first); // Expected: [1, 3, 12, 0, 0]

        int[] second = new int[] {0};
        solution.moveZeroes(second);
        printArray(second); // Expected: [0]
    }

    private static void printArray(int[] nums) {
        System.out.print("[");
        for (int i = 0; i < nums.length; i++) {
            if (i > 0) {
                System.out.print(", ");
            }
            System.out.print(nums[i]);
        }
        System.out.println("]");
    }
}
