# Dictionaries
# Dictionaries are used to store data values in keys:value pairs.
# They are unordered, mutable(changeable) & don't allow duplicate keys.

# infor={
#     "name":"Waseem Akram",
#     "Age":26,
#     "Type":"AI Developer",
#     "Learning":"Machine Learning"
# }
# print(infor)

# Nested Tuples
student={
    "name":"Waseem Akram",
    "Subjects":{"physics":34,
                "checm": 23,
                "Math":24}
}

print(student["Subjects"]["Math"])

# Keys in Dictonaries

# print(student.keys())

#  convert in list 

# print(list(student.keys()))

# find length of dictionary or list

# print(len(student))

# return all values in dictonary

# print(student.values)

# use dist.get("key") to get the value of that key. we use dist["key"] as well but this is better practive
# to avoid the errors when we handle big level of data while working in real projects.

# print(student["name2"]) <---- This will show the errror.

# print(student.get("na2me")) <---- This will show the none. the purpose to use this let say we have a website and
# and we catch some errors so this don't mean the entire website is shut down instead only the specific error
# area is shut down so that's why we use method to build stabilize systems. We also have some try catch and other
# methods to handle the errors.

#  we use update to udpate the data in dictionaries e.g.
list_new={"City":"Lahore","Car Model":"Porsche"}
student.update(list_new)


# >----------------------< For create empty dictionary we use
# dict={}

# print(student) <-------------- This'll print all the updated dictionary details.

# Set in Python
#  Set is the collection of unordered items. Each item in the set must be unique & immutable.
#  We cannot store dictionaries and list in Set because they're mutable

collection={1,2,3,4,5,"hello",5,5,"hello"} # it will ignore duplicate values
# print(collection)
# print(type(collection))
# print(len(collection))
# >----------------------< For create empty dictionary we use
# dict={} but for create empty set we use set_1=Set()

# Sets Method

# set.add , set.remove we use this to add the values and remove the values from set.
# print("Hello Im -----------------------------")
# collection.pop()
# print(collection)
# print(len(collection))

# collection.pop()
# print(collection)
# print(len(collection))
 
#   Union & intersection methods in sets.

coolection2={2,1,1,1,1,3,4,5,"hello,","waseem"}
print("Union of colleciton :",collection.union(coolection2))
print("Union of colleciton :",collection.intersection(coolection2))

