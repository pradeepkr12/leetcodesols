class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_val(l1):
    i = 0
    res = 0
    while l1 != None:
        res += (10 ** i)*l1.val
        l1 = l1.next
        i += 1
    return res

def ret_list(val):
    v1 = val%10
    head = ListNode(v1)
    val = val // 10
    nextnode = head
    while val > 0:
        v1 = val%10
        node = ListNode(v1)
        nextnode.next = node
        nextnode = nextnode.next
        val = val // 10
    return head


list1 = ListNode(2, ListNode(4, ListNode(3)))
list2 = ListNode(5, ListNode(6, ListNode(4)))
