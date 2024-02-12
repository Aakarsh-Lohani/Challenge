#https://leetcode.com/problems/merge-k-sorted-lists/description/
"""
23. Merge k Sorted Lists
Hard

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            head = point = ListNode(0)
            while l1 and l2:
                if l1.val <= l2.val:
                    point.next = l1
                    l1 = l1.next
                else:
                    point.next = l2
                    l2 = l1
                    l1 = point.next.next
                point = point.next
            if not l1:
                point.next=l2
            else:
                point.next=l1
            return head.next

        def merge(lists, left, right):
            if left == right:
                return lists[left]
            mid = left + (right - left) // 2
            l1 = merge(lists, left, mid)
            l2 = merge(lists, mid+1, right)
            return mergeTwoLists(l1, l2)

        return merge(lists, 0, len(lists)-1) if lists else None
    
    