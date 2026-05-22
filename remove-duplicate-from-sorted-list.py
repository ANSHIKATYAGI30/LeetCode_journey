class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        current = head

        while current and current.next:

            # Duplicate found
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
