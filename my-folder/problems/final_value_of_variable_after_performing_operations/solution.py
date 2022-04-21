class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        output = 0
        for op in operations:
            if op in ["++X","X++"]:
                output += 1
            else:
                output -= 1
                
        return output