class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maximumAmount = 0
        while(left < right):
            leftHeight = height[left]
            rightHeight = height[right]
            maximumAmount = max(maximumAmount, min(leftHeight, rightHeight) * (right - left))
            if(leftHeight < rightHeight):
                left += 1
            else:
                right -= 1
                
        return maximumAmount
        