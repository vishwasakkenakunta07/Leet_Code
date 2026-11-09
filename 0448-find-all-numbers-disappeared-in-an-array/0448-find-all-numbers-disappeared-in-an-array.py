class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # Step 1: Mark visited numbers
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        # Step 2: Find missing numbers
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result