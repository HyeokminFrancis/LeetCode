class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximumPoints = []
        for i, num in enumerate(nums):
            maximumPoints.append(i + num)

        currIdx = 0
        numsLen = len(nums)
        while True:
            if maximumPoints[currIdx] >= numsLen -1:
                return True
            jumpRange = nums[currIdx]
            jumpPoints = maximumPoints[currIdx + 1 : currIdx + jumpRange + 1]
            jumpPoints = jumpPoints[::-1]

            if len(jumpPoints) == 0:
                return False
            
            newCurrIdx = currIdx +  len(jumpPoints) - jumpPoints.index(max(jumpPoints)) 
            
            
            currIdx = newCurrIdx
            
        
        
        
        