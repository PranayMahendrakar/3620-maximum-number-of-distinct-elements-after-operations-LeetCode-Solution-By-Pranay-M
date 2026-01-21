class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        # Greedily assign the smallest possible value to each element
        # Each nums[i] can become nums[i] - k to nums[i] + k
        
        prev = float('-inf')  # Last value we assigned
        distinct = 0
        
        for num in nums:
            # The range for this number is [num - k, num + k]
            # We want to pick the smallest value > prev
            low = num - k
            high = num + k
            
            # The value we assign must be > prev and in [low, high]
            # Pick max(prev + 1, low) if it's <= high
            val = max(prev + 1, low)
            
            if val <= high:
                prev = val
                distinct += 1
            # If val > high, we can't assign a distinct value
        
        return distinct