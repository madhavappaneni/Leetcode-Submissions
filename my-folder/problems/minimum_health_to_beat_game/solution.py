class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        m = max(damage)
        s = sum(damage)

        return s - min(m, armor) + 1
            
