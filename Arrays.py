import array as arr

array1 = arr.array("i", [1, 3, 5, 4, 1, 8, 0])
print("Original array = "+str(array1))

print("Number of occurence of the number 8 in the said array = "+str(array1.count(8)))

array1.reverse()
print("Reversed order of the items = ")
print(str(array1))