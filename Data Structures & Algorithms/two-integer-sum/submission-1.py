class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=dict()
        for i,num in enumerate(nums):
            need=target-num
            if need in l:
                return [l[need],i]
            l[num]=i
