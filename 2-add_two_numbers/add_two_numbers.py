#!/usr/bin/env python


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        root = None
        p = root
        carry = 0
        while l1 is not None or l2 is not None or carry > 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            val = int((val1 + val2 + carry) % 10)
            carry = int((val1 + val2 + carry) / 10)
            new_node = ListNode(val)
            if root is None:
                root = new_node
                p = root
            else:
                p.next = new_node
                p = p.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return root


if __name__ == "__main__":
    l1 = ListNode(5)
    l2 = ListNode(5)

    solution = Solution()
    l3 = solution.addTwoNumbers(l1, l2)

    while l3 is not None:
        print(l3.val)
        l3 = l3.next
