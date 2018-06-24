# Leetcode690_employeeImportance.py

"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
    # Solution 1: use a hashmap to look up employee and its info quickly
    # and use depth-first search

    # O(n)

        emap = {employee.id: employee for employee in employees}
        employee = emap[id]
        total = employee.importance

        for id in employee.subordinates:
            total += self.getImportance(employees, id)

        return total
