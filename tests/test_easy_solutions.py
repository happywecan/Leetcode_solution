import unittest

from solutions.python.easy.p0001_two_sum import Solution as TwoSum
from solutions.python.easy.p0009_palindrome_number import Solution as PalindromeNumber
from solutions.python.easy.p0013_roman_to_integer import Solution as RomanToInteger
from solutions.python.easy.p0014_longest_common_prefix import Solution as LongestCommonPrefix
from solutions.python.easy.p0020_valid_parentheses import Solution as ValidParentheses
from solutions.python.easy.p0035_search_insert_position import Solution as SearchInsertPosition
from solutions.python.easy.p0121_best_time_to_buy_and_sell_stock import Solution as BestStockProfit
from solutions.python.easy.p0136_single_number import Solution as SingleNumber
from solutions.python.easy.p0217_contains_duplicate import Solution as ContainsDuplicate
from solutions.python.easy.p0283_move_zeroes import Solution as MoveZeroes
from solutions.python.easy.p0344_reverse_string import Solution as ReverseString
from solutions.python.easy.p0876_middle_of_the_linked_list import ListNode, Solution as MiddleNode


class EasySolutionTests(unittest.TestCase):
    def test_two_sum(self) -> None:
        self.assertEqual(TwoSum().twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_palindrome_number(self) -> None:
        solution = PalindromeNumber()
        self.assertTrue(solution.isPalindrome(121))
        self.assertFalse(solution.isPalindrome(-121))

    def test_roman_to_integer(self) -> None:
        self.assertEqual(RomanToInteger().romanToInt("MCMXCIV"), 1994)

    def test_longest_common_prefix(self) -> None:
        self.assertEqual(LongestCommonPrefix().longestCommonPrefix(["flower", "flow", "flight"]), "fl")

    def test_valid_parentheses(self) -> None:
        solution = ValidParentheses()
        self.assertTrue(solution.isValid("()[]{}"))
        self.assertFalse(solution.isValid("(]"))

    def test_search_insert_position(self) -> None:
        solution = SearchInsertPosition()
        self.assertEqual(solution.searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(solution.searchInsert([1, 3, 5, 6], 2), 1)

    def test_best_time_to_buy_and_sell_stock(self) -> None:
        solution = BestStockProfit()
        self.assertEqual(solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(solution.maxProfit([7, 6, 4, 3, 1]), 0)

    def test_single_number(self) -> None:
        self.assertEqual(SingleNumber().singleNumber([4, 1, 2, 1, 2]), 4)

    def test_contains_duplicate(self) -> None:
        solution = ContainsDuplicate()
        self.assertTrue(solution.containsDuplicate([1, 2, 3, 1]))
        self.assertFalse(solution.containsDuplicate([1, 2, 3, 4]))

    def test_move_zeroes(self) -> None:
        nums = [0, 1, 0, 3, 12]
        MoveZeroes().moveZeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_reverse_string(self) -> None:
        value = ["h", "e", "l", "l", "o"]
        ReverseString().reverseString(value)
        self.assertEqual(value, ["o", "l", "l", "e", "h"])

    def test_middle_of_the_linked_list(self) -> None:
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        middle = MiddleNode().middleNode(head)
        self.assertIsNotNone(middle)
        self.assertEqual(middle.val, 3)


if __name__ == "__main__":
    unittest.main()
