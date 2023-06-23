class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        first, second, third = False, False, False

        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            first = first or (triplet[0] == target[0])
            second = second or (triplet[1] == target[1])
            third = third or (triplet[2] == target[2])

            
            if first and second and third:
                return True
        
        return False