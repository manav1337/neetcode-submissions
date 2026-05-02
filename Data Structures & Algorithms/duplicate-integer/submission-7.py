class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = {}

        for i in range(0 , len(nums)):
            if nums[i] in result:
                return True
            else :
                result[nums[i]] = True
        return False
                
