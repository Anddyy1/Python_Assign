my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)

my_list.extend([50, 60, 70])

my_list.remove(70)

my_list.sort()

index_30 = my_list.index(30)
print(f"Index of 30 is: {index_30}")

print(my_list)
