# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []
        cur= head
        while cur.next is not None:
            cur = cur.next
            arr.append(cur.val)

        arr.sort()
        i =0
        curs = head
        while curs.next is not None:
            curs = curs.next
            curs.val = arr[i]
            i+=1
        return head

def printLink(head):
    result =[]
    curs=head
    while curs.next is not None:
        curs = curs.next
        result.append(curs.val)

    print(result)


if __name__ == '__main__':
    arr = [4,2,1,3]
    head = ListNode()
    cur=head
    for value in arr:
        print("appending----"+str(value))
        newNode = ListNode(val=value)

        cur.next=newNode
        cur = cur.next

    printLink(head)
    su = Solution()
    newhead = su.sortList(head)
    printLink(newhead)


