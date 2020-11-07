def selection_sort(items):
    """
    Sorts a list of items into ascending order using the
    selection sort algoright.
    """
    for step in range(len(items)):
        # Find the location of the smallest element in
        # items[step:].
        location_of_smallest = step
        for location in range(step + 1, len(items)):
            # TODO: determine location of smallest
            if items[location] < items[step]:
                location_of_smallest = location
        # TODO: Exchange items[step] with items[location_of_smallest]
        items[step], items[location_of_smallest] = items[location_of_smallest], items[step]
    return items

# mylist = input('Enter the list values to sort:   ').split()
# mylist = [int(x) for x in mylist]
mylist = [4, 3, 5, 2, 9]
selection_sort(mylist)
print('Sorted list::')
print(mylist)
