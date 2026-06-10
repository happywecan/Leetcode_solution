/**
 * LeetCode 206: Reverse Linked List.
 *
 * Problem: https://leetcode.com/problems/reverse-linked-list/
 */
public class P0206_ReverseLinkedList {
    public ListNode reverseList(ListNode head) {
        ListNode previous = null;
        ListNode current = head;

        while (current != null) {
            ListNode nextNode = current.next;
            current.next = previous;
            previous = current;
            current = nextNode;
        }

        return previous;
    }

    public static void main(String[] args) {
        P0206_ReverseLinkedList solution = new P0206_ReverseLinkedList();

        ListNode first = buildList(new int[] {1, 2, 3, 4, 5});
        printList(solution.reverseList(first)); // Expected: 5 -> 4 -> 3 -> 2 -> 1

        ListNode second = buildList(new int[] {1, 2});
        printList(solution.reverseList(second)); // Expected: 2 -> 1

        ListNode third = buildList(new int[] {});
        printList(solution.reverseList(third)); // Expected: empty line
    }

    private static ListNode buildList(int[] values) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        for (int value : values) {
            current.next = new ListNode(value);
            current = current.next;
        }

        return dummy.next;
    }

    private static void printList(ListNode head) {
        ListNode current = head;

        while (current != null) {
            if (current != head) {
                System.out.print(" -> ");
            }
            System.out.print(current.val);
            current = current.next;
        }

        System.out.println();
    }

    static class ListNode {
        int val;
        ListNode next;

        ListNode(int val) {
            this.val = val;
        }
    }
}
