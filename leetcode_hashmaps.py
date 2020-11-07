"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""


def longestSubstring():
    s = "abcabcbb"
    # s = "aab"
    # count = counter = 0
    # _map = {}
    # for i in range(len(s)):
    #     if s[i] not in _map:
    #         _map[s[i]] = s[i]
    #         counter += 1
    #         print(_map, counter)
    #     else:
    #         _map.clear()
    #         counter = 0
    #     count = max(count, counter)
    # return count

	# Creating a set to store the last positions of occurrence
    seen = {}
    maximum_length = 0

    # starting the inital point of window to index 0
    start = 0

    for end in range(len(s)):

        # Checking if we have already seen the element or not
        if s[end] in seen:

            # If we have seen the number, move the start pointer
            # to position after the last occurrence
            start = max(start, seen[s[end]] + 1)

        # Updating the last seen value of the character
        seen[s[end]] = end
        maximum_length = max(maximum_length, end-start + 1)
    return maximum_length


print(longestSubstring())