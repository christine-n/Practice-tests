def intToRoman(num):
    count = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C', 100],
             ['XC', 90], ['L', 50], ['XL', 40], ['X', 10], ['IX', 9],
             ['V', 5], ['IV', 4], ['I', 1]]
    result = ""
    for x in count:
        result += x[0] * (num // x[1])
        num = num % x[1]
    return result


def romanToInt(s):
    # "MMMCDXC" 3490
    mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num, temp = 0, 0

    for i, c in enumerate(s[0:-1]):
        if mapping[c] < mapping[s[i + 1]]:
            temp = mapping[c]
            print('yes', temp)
        else:
            num += (mapping[c] - temp)
            temp = 0

    return num + (mapping[s[-1]] - temp)


print(romanToInt('MMMCDXC'))
