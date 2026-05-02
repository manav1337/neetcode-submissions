class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_result = {}
        result = []

        for i in range(len(nums)):
            b = target - nums[i]
            if(b in dict_result):
                result.append(dict_result[b])
                result.append(i)
                return result
            else:
                dict_result[nums[i]] = i
        
        return []
            



        