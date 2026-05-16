#list
#tuples
#set
#dictionaries

fruits=['apple','banana','carrot','banana']
# print(fruits)
print(fruits[0])
print(fruits[-1])

# for adding element
fruits.append("orange")
print(fruits)
# for insert element at the place which u  give location and then goes
fruits.insert(1,"grapes")
print(fruits)
# for remove elemnt
fruits.remove("banana")
print(fruits)
# for remove last item
fruits.pop()
print(fruits)


# for sequence
fruits.sort()
print(fruits)

# looping through list
for fruit in fruits:
    print(fruit)

# tuples  can be unchangeble and not modified
colors=("red","green","yellow","purple")
print(colors)
print(colors[1])

# tuple methods
numbers= (1,2,3,4,5,6,6,7,7,8,8)
print(numbers.count(6))
print(numbers.index(7))

# set store unique unorder value and no dupliaction
my_set={1,2,3,4,5,5,6,7,8,9}
print(my_set)

# funtions in set
my_set.add(18)
my_set.remove(6)
print(my_set)

A={1,2,3}
b={3,4,5}
print(A.union(b))
print(A.intersection(b))
print(A.difference(b))

# dictionary:store data as key:value pairs
student={
    "name":"Ali",
    "age":"22",
    "course":"data science"
}
print(student)

# Access value
print(student["name"])

# other method also
print(student.get("age"))

# methods of dictionarry

student["age"] = 23
print(student)
student["city"]= "japan"
print(student)
print(student.pop("course"))
print(student)

# looping in dictionary
for key, value in student.items():
    print(key, ":", value)