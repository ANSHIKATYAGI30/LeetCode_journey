# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):

    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        dummy.next = head

        groupPrev = dummy

        while True:

            # Find kth node
            kth = groupPrev

            for _ in range(k):

                kth = kth.next

                if not kth:
                    return dummy.next

            groupNext = kth.next

            # Reverse group
            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:

                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect reversed group
            temp = groupPrev.next

            groupPrev.next = kth

            groupPrev = temp
