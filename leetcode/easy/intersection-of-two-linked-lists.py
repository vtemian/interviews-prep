# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        pointA, pointB = headA, headB

        while pointA != pointB:
            pointA = pointA.next if pointA else headB
            pointB = pointB.next if pointB else headA

        return pointA
