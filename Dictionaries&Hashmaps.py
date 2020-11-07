def  countTriplets():
    """
    https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

    You are given an array and you need to find number of tripets of indices  such that the elements at those indices are in geometric progression for a given common ratio  and .

    For example, . If , we have  and  at indices  and .

    Function Description

    Complete the countTriplets function in the editor below. It should return the number of triplets forming a geometric progression for a given  as an integer.

    countTriplets has the following parameter(s):

    arr: an array of integers
    r: an integer, the common ratio
    """

    arr = [1, 2, 2, 4]
    r = 2
    n = len(arr)
    count = 0
    dict = {}
    dictPairs = {}

    for i in reversed(arr):
            if i*r in dictPairs:
                    count += dictPairs[i*r]
            if i*r in dict:
                    dictPairs[i] = dictPairs.get(i, 0) + dict[i*r]

            dict[i] = dict.get(i, 0) + 1

    return count



def sherlockAndAnagrams():
    s = 'abba'
    # print(s)
    # abba
    if len(s) == 1:
        print(0)
    arr = list(s)
    n = len(arr)
    mydict = {}
    for i in range(n):
        if not arr[i] in mydict:
            mydict[arr[i]] = 1
        mydict[arr[i]] += 1

    return mydict

    # if isAnagram(s)


print(countTriplets())