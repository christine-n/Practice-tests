def pairTargetSum():
    """
    A function that takes in a non empty array, and a target sum and returns the pair if there are two integers that adds up to the target sum. Return empty array if no pair.
    """
    arr = [1,2,4,6,8]
    arr.sort()
    t_sum = 11
    n = len(arr)
    # O(N^2)
    # for i in range(n):
    #     for j in range(n):
    #         if (arr[i] + arr[j] == t_sum):
    #             return arr[i], arr[j]

    left = 0
    right = n - 1
    while left < right:
        if arr[left] + arr[right] == t_sum:
            return [arr[left], arr[right]]
        elif arr[left] + arr[right] < t_sum:
            left += 1
        else:
            right -= 1

    return []


def uniqueString():
    """
    Implement an algorithm to determine if a string has all unique characters. What if you
    cannot use additional data structures?
    """
    s = 'powerpuff'

    if len(s) > 128:
        return False
    char_counts = {}
    # For every character, check if it exists
    for i in range(0, len(s)):
        if s[i] not in char_counts:
            char_counts[s[i]] = 1
        else:
            return False
    print(char_counts)
    return True


def checkPermutation():
    """
    Check Permutation: Given two strings, write a method to decide if one is a permutation of the
    other.
    """
    s1 = "dat"
    s2 = "tap"
    # If they are not of the same length, cannot be a permutation:
    if len(s1) != len(s2):
        return False

    # Sort the strings and see if they are equal:
    arr_s1 = list(s1)
    arr_s2 = list(s2)
    return arr_s1.sort() == arr_s2.sort()


def URLify():
    """
    URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
    has sufficient space at the end to hold the additional characters, and that you are given the "true"
    length of the string. (Note: If implementing in Java, please use a character array so that you can
    perform this operation in place.)
    EXAMPLE
    Input: "Mr John Smith ", 13
    Output: "Mr%20John%20Smith"
    """
    n = 13
    return s[:n].replace(' ', '%20')


def palindromePermutation():
    """
    Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
    A palindrome is a word or phrase that is the same forwards and backwards. A permutation
    is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
    EXAMPLE
    Input: Tact Coa
    Output: True (permutations: "taco cat", "atco eta", etc.)
    """

def oneAway():
    """
    One Away: There are three types of edits that can be performed on strings: insert a character,
    remove a character, or replace a character. Given two strings, write a function to check if they are
    one edit (or zero edits) away.
    EXAMPLE
    pale, ple -> true
    pales, pale -> true
    pale, bale -> true
    pale, bake -> false
    """


def stringCompression():
    """
    String Compression: Implement a method to perform basic string compression using the counts
    of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
    "compressed" string would not become smaller than the original string, your method should return
    the original string. You can assume the string has only uppercase and lowercase letters (a - z).
    """
    s = 'aabcccccaaa'
    if len(s) == 0:
        return s
    compressedString = ''
    counter = 0
    for i in range(len(s)):
        counter += 1
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            compressedString += s[i]
            compressedString += str(counter)
            counter = 0
    if len(compressedString) > len(s):
        return s
    return compressedString


def rotateMatrix():
    """
    Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
    bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
    """


def zeroMatrix():
    """
    Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
    column are set to 0.
    """
    matrix = [[1,2,3],[0,2,6],[9,8,0]]
    zero_cells = {}
    for i in range(len(matrix)):
        print(matrix[i])
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                print(matrix[i][j])
                zero_cells[i] = j
    print(zero_cells)
    for key, value in zero_cells.items:
        print(key)

    return zero_cells


def stringRotation():
    """
    String Rotation:Assume you have a method isSubstring which checks if one word is a substring
    of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
    call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
    """
    print('many')
    return ''


def isSubstring():
    print('test')


def main():
    print(pairTargetSum())


if __name__ == '__main__':
    main()
