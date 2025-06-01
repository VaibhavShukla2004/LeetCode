class Solution(object):
    def check(self, nums):
        incorrect = 0
        for i in range(len(nums)) :
            if nums[i] > nums[(i + 1)%len(nums)] :
                incorrect += 1
        
        return incorrect <= 1