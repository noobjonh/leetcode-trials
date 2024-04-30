class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for index in range(len(nums)):
            value = nums[index]
            hash_map[value] = index

        for index in range(len(nums)):
            value = nums[index]
            temp = target-value
            try:
                pos = hash_map[temp]
            except:
                pos = -1
            
            if pos == -1:
                continue
            elif not pos == -1 and not pos == index:
                return [index,pos]
                break

