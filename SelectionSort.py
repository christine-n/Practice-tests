def selsort(myarray, r):
	for x in range(r):
		minimum = x
		for y in range(x + 1, r):
			if myarray[y] < myarray[minimum]:
				minimum = y
		(myarray[x], myarray[minimum]) = (myarray[minimum], myarray[x])

mylist = input('Enter the list values to sort:   ').split()
mylist = [int(x) for x in mylist]
selsort(mylist, len(mylist))
print('Sorted list::')
print(mylist)
