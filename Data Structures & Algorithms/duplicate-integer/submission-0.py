from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newc = Counter(nums)
        for count in newc.values():
            if count >= 2:
                return True
        return False