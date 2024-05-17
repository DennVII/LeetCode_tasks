class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def createList(self, arr):
        head = None
        iter = None
        for a in arr:
            if not head:
                head = ListNode(a)
                iter = head
            else:
                iter.next = ListNode(a)
                iter = iter.next
        return head
            
    
    def printList(self, lst):
        while lst:
            print(lst.val)
            lst = lst.next


    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = None
        iter = None
        while list1 and list2:
            if not head:
                iter = ListNode(list1.val if list1.val < list2.val else list2.val)
                head = iter
            else:
                iter.next = ListNode(list1.val if list1.val < list2.val else list2.val)
                iter = iter.next
            if list1.val < list2.val:
                list1 = list1.next
            else:
                list2 = list2.next

        if list1:
            if not head:
                head = list1
            else:
                iter.next = list1

        if list2:
            if not head:
                head = list2
            else:
                iter.next = list2

        return head
