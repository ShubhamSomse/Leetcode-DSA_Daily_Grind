# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # First pass: store node values in a list
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        # Second pass: calculate twin sums and find maximum
        max_sum = 0
        left, right = 0, len(values) - 1
        while left < right:
            twin_sum = values[left] + values[right]
            max_sum = max(max_sum, twin_sum)
            left += 1
            right -= 1
        
        return max_sum