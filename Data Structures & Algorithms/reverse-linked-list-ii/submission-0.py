# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
# Edge case: if the list is empty or no reversal is needed
        if not head or left == right:
            return head
# Use a dummy node to seamlessly handle reversing from the first node (left = 1)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
# 1. Advance 'prev' to the node right before the 'left' position
        for _ in range(left - 1):
            prev = prev.next
# 'curr' marks the start of the sublist to be reversed
        curr = prev.next
# 2. Reverse the sublist link-by-link up to the 'right' position
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next

        