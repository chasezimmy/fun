# Leetcode : https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    """ Nonsense solution for fun """
    def magic(self, l):
        return int(''.join(map(str, l)))


    def iterate(self, node):
        cur = node
        
        while cur.next is not None:
            yield cur.val
            cur = cur.next
        yield cur.val

    def add_two_numbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = [_ for _ in self.iterate(l1)]
        l2 = [_ for _ in self.iterate(l2)]
        print(l1, l2)
        return [int(d) for d in str(self.magic(l1[::-1]) + self.magic(l2[::-1]))][::-1]


class SolutionTwo:

    def add_two_numbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = l1
        q = l2
        carry = 0
        sum_list = []

        while p is not None or q is not None:
            if not p:
                p_val = 0
            else:
                p_val = p.val

            if not q:
                q_val = 0
            else:
                q_val = q.val

            if p is not None:
                p = p.next
            if q is not None:
                q = q.next

            sum = p_val + q_val + carry
            carry = sum // 10
            sum_list.append(sum % 10)
        if carry:
            sum_list.append(carry)
        return sum_list
