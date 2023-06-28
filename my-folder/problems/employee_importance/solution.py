"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        adjList = defaultdict(list)
        weights = defaultdict(int)

        for employee in employees:
            adjList[employee.id].extend(employee.subordinates)
            weights[employee.id] = employee.importance
        
        def dfs(node):
            ans = weights[node]
            for nei in adjList[node]:
                ans += dfs(nei)
            return ans
        
        return dfs(id)
                
            