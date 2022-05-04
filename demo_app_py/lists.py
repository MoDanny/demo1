demo_list = ["Omega", "abc", "xyz", "Omega"]
element = demo_list[0]
print(demo_list)
print (element)
print(demo_list[2])
demo_list.append("Theta")
demo_list.append("Epsilon")
print(demo_list)
demo_list.remove("Omega")
print(demo_list)
demo_list.remove("Omega")
print(demo_list)

print ("********************************************** Sets")
demo_set = {"abc", "xyz", "Omega"}
print (demo_set)

for element in demo_set:
    print(element)

demo_set.add("Salbei")
print (demo_set)
try:
    demo_set.remove("Omega")
except KeyError:
    print("notinlist")
print (demo_set)

print("Hallo Welt".replace("Welt", "Elch"))


print ("********************************************** Dictionary")
demo_dict = {"days":10,
             "hours":4,
             "Notb": 666}

print(demo_dict)
print(type(demo_dict))