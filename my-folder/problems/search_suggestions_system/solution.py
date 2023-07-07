class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        currSearchWord = ""
        products.sort()

        res = []
        
        for c in searchWord:
            currSearchWord += c
            i = bisect.bisect_left(products, currSearchWord)
            res.append([product for product in products[i:i+3] if product.startswith(currSearchWord)])
        
        return res
