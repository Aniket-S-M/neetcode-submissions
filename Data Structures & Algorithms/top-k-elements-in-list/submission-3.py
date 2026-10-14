from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nnums = Counter(nums)
        
        # Sort the items by frequency (value) from highest to lowest
        sorted_items = sorted(nnums.items(), key=lambda x: x[1], reverse=True)
        
        # Extract just the keys for the top k items
        return [key for key, value in sorted_items[:k]]