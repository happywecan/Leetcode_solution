import java.util.Arrays;

/**
 * LeetCode 88: Merge Sorted Array.
 *
 * Problem: https://leetcode.com/problems/merge-sorted-array/
 */
public class P0088_MergeSortedArray {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        // nums1 前 m 個位置才是真正的數字，所以 first 從 nums1 的最後一個有效數字開始。
        int first = m - 1;

        // second 從 nums2 的最後一個數字開始。
        int second = n - 1;

        // nums1 後面有空位，可以從最右邊開始放目前最大的數字。
        int write = m + n - 1;

        // 只要 nums2 還有數字沒放進 nums1，就繼續合併。
        while (second >= 0) {
            // 如果 nums1 目前的數字比較大，就把它放到 write 的位置。
            if (first >= 0 && nums1[first] > nums2[second]) {
                nums1[write] = nums1[first];
                first--;
            } else {
                // 否則放 nums2 目前的數字。
                // first < 0 時，也代表 nums1 的有效數字都用完了，只能繼續放 nums2。
                nums1[write] = nums2[second];
                second--;
            }

            // 每放好一個數字，下一次就往左邊一格寫。
            write--;
        }
    }

    public static void main(String[] args) {
        P0088_MergeSortedArray solution = new P0088_MergeSortedArray();

        int[] first = new int[] {1, 2, 3, 0, 0, 0};
        solution.merge(first, 3, new int[] {2, 5, 6}, 3);
        System.out.println(Arrays.toString(first)); // Expected: [1, 2, 2, 3, 5, 6]

        int[] second = new int[] {1};
        solution.merge(second, 1, new int[] {}, 0);
        System.out.println(Arrays.toString(second)); // Expected: [1]

        int[] third = new int[] {0};
        solution.merge(third, 0, new int[] {1}, 1);
        System.out.println(Arrays.toString(third)); // Expected: [1]
    }
}
