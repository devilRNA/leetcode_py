# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sortFunc(head: ListNode, tail: ListNode) -> ListNode:
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sortFunc(head, mid), sortFunc(mid, tail))

        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        return sortFunc(head, None)






def printLink(head):
    result = []
    curs = head
    while curs.next is not None:
        curs = curs.next
        result.append(curs.val)

    print(result)


if __name__ == '__main__':
    arr = [4, 2, 1, 3]
    head = ListNode()
    cur = head
    for value in arr:
        print("appending----" + str(value))
        newNode = ListNode(val=value)

        cur.next = newNode
        cur = cur.next
    printLink(head)
    su = Solution()
    newhead = su.sortList(head)
    printLink(newhead)
