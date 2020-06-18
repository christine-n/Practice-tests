def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1
        # print('J {} key_item {}'.format(j, key_item))

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        print(j, key_item)
        print(array)
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            # print(j, array[j + 1], array[j],    key_item)
            array[j + 1] = array[j]
            print(array)
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item

    return array


# mylist = input('Enter the list values to sort:   ').split()
# mylist = [int(x) for x in mylist]
mylist = [1, 2, 8, 4, 5]
insertion_sort(mylist)
print('Sorted list::')
print(mylist)