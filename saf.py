def solution(S):
    # write your code in Python 3.6
    arr = S.split(" ")
    _stack = []
    print(arr)

    for i in range(len(arr)):
        sl = len(_stack)
        print(sl)
        if arr[i] == 'DUP':
            if sl > 0:
                _stack.append(_stack[sl - 1])
            else:
                return -1
        elif arr[i] == '+':
            print('stacklen {}'.format(sl))
            if sl > 1:
                _sum = int(_stack[sl - 2]) + int(_stack[sl - 1])
                _stack.pop()
                _stack.pop()
                _stack.append(_sum)
            else:
                return -1
        elif arr[i] == '-':
            if sl > 1:
                _sum = int(_stack[sl - 1]) - int(_stack[sl - 2])
                _stack.pop()
                _stack.pop()
                _stack.append(_sum)
            else:
                return -1
        elif arr[i] == 'POP':
                _stack.pop()
        else:
            _stack.append(arr[i])

    return _stack[len(_stack) - 1]


-- write your code in PostgreSQL 9.4


SELECT DISTINCT id, DATE_PART('second', date_left -  '2018-12-20 11:22:00'::timestamp)  FROM users_user WHERE (DATE_PART('second', date_left -  '2018-12-20 11:22:00'::timestamp)) > 0  ORDER BY id ASC ;



s = '13 DUP 4 POP 5 DUP + DUP + -'
print(solution(s))