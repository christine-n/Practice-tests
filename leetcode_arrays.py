def maxArea():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    n = len(height)
    max_area = 0

    # for i in range(n):
    #     for j in range(n):
    #         if height[i] <= height[j]:
    #             area = height[i] * (j - i)
    #             max_area = max(max_area, area)
    #         else:
    #             area = height[j] * (j - i)
    #             max_area = max(max_area, area)
    # return max_area
    i = 0
    j = n - 1
    while i < j:
        max_area = max((j - i) * min(height[i], height[j]), max_area)
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
    return max_area


# print(maxArea())


"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


def threeSum():
    nums = [-1, 0, 1, 2, -1, -4]
    n = len(nums)
    nums.sort()
    print(nums)
    # [-4, -1, -1, 0, 1, 2]
    arrs = []
    for i in range(n):
        left = i + 1
        right = n - 1

        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]
            if three_sum == 0:
                arrs.append([nums[i], nums[left], nums[right]])
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
            elif nums[i] + (nums[left] + nums[right]) < 0:
                left += 1
            else:
                right -= 1

    return arrs


print(threeSum())
