# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []
        while head.next is not None:
            arr.append(head.val)
            head=head.next
        arr.sort()
        print(arr)
