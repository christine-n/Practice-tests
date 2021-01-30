def solution(S):
    occurrences = [0] * 26

    for i in range(len(S)):
        occurrences[ord(S[i]) - ord('a')] += 1

    best_char = 'a'
    best_res = 0

    for i in range(1, 26):
        if occurrences[i] >= best_res:
            best_char = chr(ord('a') + i)
            best_res = occurrences[i]

    return best_char


 if len(S) <1:
        return -1
    # initialize stack to empty
    stack = []
    # split the input by spaces
    split_s = S.split(' ')
    try:
        for i in split_s:
            if i.isdigit():
                # append digits
                stack.append(i)
            else:
                # operations
                if i == 'DUP':
                    stack.append(stack[-1])
                elif i == 'POP':
                    stack.remove(stack[-1])
                elif i == '-':
                    last = stack[-1]
                    second_last = stack[-2]
                    # pop the two
                    stack.remove(stack[-1])



                    stack.remove(stack[-1])
                    stack.append(int(last)-int(second_last))
                elif i == '+':
                    last = stack[-1]
                    second_last = stack[-2]
                    # pop the two
                    stack.remove(stack[-1])
                    stack.remove(stack[-1])
                    stack.append(int(last)+int(second_last))
    except Exception:
        return Exception

    if stack:
        return stack[-1]

    return -1





    <SearchBar filterText={this.state.filterText}/>