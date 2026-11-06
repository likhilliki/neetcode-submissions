
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for num in nums:
            total |= num
        total = total * (1 << (n - 1))
        return total

        