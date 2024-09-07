from typing import Optional

def list_to_linkedlist(lst):
    if not lst:  # Verifica se a lista está vazia
        return None
    
    head = ListNode(lst[0])  # Cria o primeiro nó (cabeça)
    current = head
    
    for value in lst[1:]:  # Itera sobre o resto da lista
        current.next = ListNode(value)
        current = current.next
    
    return head



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        
        # Itera comparando valor e próximo nó
        current_self = self
        current_other = other
        while current_self and current_other:
            if current_self.val != current_other.val:
                return False
            current_self = current_self.next
            current_other = current_other.next
        
        # Certifica-se de que ambos chegaram ao final
        return current_self is None and current_other is None


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cont = 1
        n1 = 0
        while l1 is not None:
            n1 += l1.val * cont
            cont *= 10
            l1 = l1.next

        cont = 1

        n2 = 0
        while l2 is not None:
            n2 += l2.val * cont
            cont *= 10
            l2 = l2.next

        n_sum = n1 + n2

        arr = []
        cont = 10
        i = 0
        while int(n_sum) != 0:
            arr.append(int(n_sum%cont))
            print(arr[i])
            i=i+1
            n_sum/=cont


        return list_to_linkedlist(list(arr))
