def merge(left, right):
    print(left, right)
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # [5, 3, 7, 8, 1,  3, 56, 7, 2, 3, 0]
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        print('Res {}'.format(result))

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            print('right')
            result += left[index_left:]
            break

        if index_left == len(left):
            print('here')
            result += right[index_right:]
            break

    return result


def merge_sort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))


# mylist = input('Enter the list values to sort:   ').split()
# mylist = [int(x) for x in mylist]
# mylist = [5, 3, 7, 8, 1, 3, 56, 7, 2, 3, 0]
# mylist = [5, 4, 2, 3, 1]
mylist = [1,2,3,4,5]
sorted_list = merge_sort(mylist)
print('Sorted list::')
print(sorted_list)
