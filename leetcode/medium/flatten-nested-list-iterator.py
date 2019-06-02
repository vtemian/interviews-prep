# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """

        self.idx = 0
        self.store = []

        def unnester(element):
            if isinstance(element, list):
                for el in element:
                    unnester(el)
            elif element.isInteger():
                self.store.append(element.getInteger())
            else:
                unnester(element.getList())

        unnester(nestedList)

    def next(self):
        """
        :rtype: int
        """

        if self.idx >= len(self.store):
            return None

        result = self.store[self.idx]
        self.idx += 1

        return result

    def hasNext(self):
        """
        :rtype: bool
        """

        return self.idx < len(self.store)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
