"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """

        store = {}

        for employee in employees:
            store[employee.id] = {
                'importance': employee.importance,
                'subordinates': employee.subordinates,
            }

        importance = 0
        queue = [id]

        while queue:
            id = queue.pop()
            importance += store[id]['importance']

            queue.extend(store[id]['subordinates'])

        return importance
