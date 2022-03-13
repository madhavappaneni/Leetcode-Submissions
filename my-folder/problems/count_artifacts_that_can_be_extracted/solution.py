class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        count = 0
        dig_set = set()
        for element in dig:
            dig_set.add(str(element[-0]) + ":" + str(element[1]))
        
        for artifact in artifacts:
            start_x, start_y, end_x, end_y = artifact
            dug = True
            for i in range(start_x, end_x + 1):
                for j in range(start_y, end_y + 1):
                    dug = dug and str(i)+ ":" +str(j) in dig_set
            if dug == True:
                count += 1
        return count
    
    
    