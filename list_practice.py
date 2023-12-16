print("helloworld")

mylist = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
]
print(mylist)


# Use and manipulate lists (arrays) including:
# Append
mylist.append(-1)
print(mylist)


# Insert

mylist.insert(5, 1000)
print(mylist)
mylist.insert(1, "Ishaan")
print(mylist)
# Remove

mylist.remove("Ishaan")
print(mylist)

# Change

mylist[5] = 99
print(mylist)
# Length

print(f"length of the list is {len(mylist)}")

# For loops over a list

for x in mylist:
    if x % 2 == 0:
        print(x)
print([x for x in mylist if x%2 == 1])
