dict1 = {
    'value':11
}
dict2 = dict1
print("Before values are updated")
print("dict1=",dict1)
print("dict2=",dict2)

print("dict1 value points to:",id(dict1))
print("dict2 value points to:",id(dict2))

dict2['value']=22

print("After values are updated")
print("dict1=",dict1)
print("dict2=",dict2)

print("dict1 value points to:",id(dict1))
print("dict2 value points to:",id(dict2))
