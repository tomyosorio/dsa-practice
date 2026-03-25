class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_ind = {}
        res = []

        for i in range(0, len(nums)):
            nums_ind[nums[i]] = i

        for i in range(0, len(nums)):
            if (target - nums[i]) in nums_ind and i != nums_ind[target - nums[i]]:
                res.append(i)
                res.append(nums_ind[target - nums[i]])
                break
        
        return res