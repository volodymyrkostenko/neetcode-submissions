# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        array = []

        while head:
            array.append(head.val)
            head = head.next


        i = 0
        j = len(array) - 1

        print(array)

        while i <= j:
            print(i, j)
            if array[i] != array[j]:
                return False
            
            j -= 1
            i += 1
        
        return True
        