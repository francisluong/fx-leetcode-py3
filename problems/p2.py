import math
from leet.linklist import ListNode
from typing import List, Optional

"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""


def val(node) -> int:
    return node.val if node else 0


def sum_mod_10(v1: int, v2: int, carryover: Optional[int] = 0) -> (int, int):
    sum = v1 + v2 + carryover
    return divmod(sum, 10)


class Solution:
    def brute_naive(
        self,
        l1: ListNode,
        l2: ListNode,
    ) -> ListNode:
        # lists may not be same length
        # and we have to factor for carryover
        result_node = None
        prev_node = None
        carryover = 0
        while l1 or l2 or carryover:
            # get new sum and carryover, and create a new node
            carryover, sum = sum_mod_10(val(l1), val(l2), carryover=carryover)
            new_node = ListNode(sum)
            # link to previous node if we can
            if prev_node:
                prev_node.next = new_node
            # prep next iteration
            result_node = result_node or new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            prev_node = new_node
        # handle case where l1 and l2 were None
        result_node = result_node or ListNode()
        return result_node

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        return self.brute_naive(l1, l2)
