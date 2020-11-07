"""
Given anon-emptystring, encode the string such that its encoded length is the shortest.
The encoding rule is:k[encoded_string], where theencoded_stringinside the square brackets is being repeated exactlyktimes.
Note:
k will be a positive integer and encoded string will not be empty or have extra space.
You may assume that the input string contains only lowercase English letters. The string's length is at most 160.
If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them is fine.
Input: "abbbabbbcabbbabbbc"
Output: "2[2[abbb]c]"
Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can
"""


"""
STRING DECODE:: https://techdevguide.withgoogle.com/paths/advanced/compress-decompression/#!
Your input is a compressed string of the format number[string] and the decompressed output form should be the string written number times. For example:
The input
3[abc]4[ab]c
Would be output as
abcabcabcababababc
"""


def solve(s):
    print(s)
    n = len(s)
    digit = 0
    new_string = ''
    part = ''
    left = 0
    for i in range(n):
        print(part)
        if s[i] == '[':
            digit = int(s[i - 1])
            left = i + 1
        elif s[i] == ']':
            part = s[left:i]
            print(part)
            new_string += (part * digit)
            print(new_string)
            digit = 0
        else:
            pass
    return new_string


def decomp(text, start=0, times=1):
    for i in range(start, times):
        # i = start
        while i < len(text) and text[i] != ']':
            # Emit letters as themselves.
            if text[i].islower():
                yield text[i]
            # If it's not a letter, it must be digit(s).  Convert to integer.
            else:
                sub_times = 0

                while text[i].isdigit():
                    sub_times = sub_times * 10 + int(text[i])
                    i += 1
                i += 1  # Skip past open-bracket
                    # Start an iterator over the sub-chunk.
                for item in decomp(text, i, sub_times):
                    # Iterator generates many characters, and then at the very end,
                    # it generates an integer.  Provide characters up to our caller,
                    # and use the integer to advance our index 'i' to end-of-chunk.
                    if isinstance(item, str):
                        yield item
                    else:
                        i = item
                # Advance 'i' to the next letter, or skip the close-bracket, whichever.
                i += 1
                # Don't emit the trailing integer if we are doing the outermost call.  This
                # test could be moved to the decompress() call instead; we would check there
                # to see if the result item was basestring or int, just as we do above, but
                # I suspect that check would be more expensive than a simple integer
                # comparison here, where the type is known.
    if start > 0:
        yield i

def decompress(s):
    for letter in decomp(s):
        print(letter)


print(decompress('3[abc]4[ab]c'))
