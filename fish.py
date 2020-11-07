def solution(A, B):
    # B -> direction
    # A -> size

    for d in range(len(B)):
        if B[d] == 0 and B[d - 1] == 0:
            if A[d - 1] < A[d]:
                A.pop(d - 1)


def isBalanced(s):
    if len(s) % 2 != 0:
        return False

    stack = []

    # Traversing the Expression
    for char in s:
        if char in ["(", "{", "["]:

            # Push the element in the stack
            stack.append(char)
        else:

            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            print(current_char)
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    # Check Empty Stack
    if stack:
        return False
    return True


def main():
    print(isBalanced('{[()]{}}'))


if __name__ == '__main__':
    main()