class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        T_i20 = 0
        T_i21 = float('-inf')
        T_i10 = 0
        T_i11 = float('-inf')

        for price in prices:
            T_i20 = max(T_i20, T_i21 + price)
            T_i21 = max(T_i21, T_i10 - price)
            T_i10 = max(T_i10, T_i11 + price)
            T_i11 = max(T_i11, -price)
        
        return T_i20
