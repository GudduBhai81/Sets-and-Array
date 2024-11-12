my_set = {1, 2, 3}
print(my_set)

my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

my_set = set([1, 2, 3, 2])
print(my_set,"\n")

num_et = set([0, 1, 2, 3, 5])
print("Original set =")
print(num_et)
num_et.pop()
print("After removing the first element from the said set = ")
print(num_et,"\n")
num_et.add(8)
print("After adding the first element from the said set = ")
print(num_et,"\n")