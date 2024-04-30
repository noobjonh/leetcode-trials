class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def linked_list_to_list(head):
            result = []
            current = head
            while current:
                result.append(current.val)
                current = current.next
            return result
        ll1 = linked_list_to_list(l1)
        ll2 = linked_list_to_list(l2)
        ln1 = ""
        ln2 = ""
        lans = []
        for i in range(len(ll1) -1,-1,-1):
            ln1 = ln1+str(ll1[i])

        for i in range(len(ll2) -1,-1,-1):
            ln2 = ln2+str(ll2[i])
        
        answer = str(int(ln1) + int(ln2))

        for i in answer:
            i = int(i)
            lans.insert(0,i)
        
        def list_to_linked_list(lst):
            if not lst:
                return None

            head = ListNode(lst[0])
            current = head

            for val in lst[1:]:
                current.next = ListNode(val)
                current = current.next

            return head

        finAns = list_to_linked_list(lans)
        return finAns        

