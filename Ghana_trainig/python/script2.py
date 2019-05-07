#!/anaconda3/bin/python

mol_weight = {"H":1, "He":4, "Li":7}
print(mol_weight["Li"])
print(mol_weight["H"],mol_weight["He"])

dict1 = {"key1":"value1", "key2":"value2"}
print(dict1["key2"])

# Another dictionary 
dict2 = dict(val1=2, val2=6.2, name="Fred Masoka", country="Ghana" )
print(dict2["name"])

# print dictionary keys
print(dict2.keys())
# print dictionary values
print(dict2.values())
# print key-value pairs
print(dict2.items())
# print the length/size of the dictionary
print(len(dict2))
# change country from "Ghana" to "Kenya"
dict2["country"] = "Kenya"
print(dict2)
# Add a new key-value pair
dict2["age"] = 30
print(dict2)
# Delete a key-value pair
del dict2["val2"]
print(dict2)
# Delete another key-value pair
mykey = "val1"
if mykey in dict2.keys():
    del dict2[mykey]
    print("Deleted key",mykey)
else:
    print("{} key is not found in {}".format(mykey,dict2.keys()))
print(dict2)
















