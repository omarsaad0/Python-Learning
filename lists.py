mylist = ["banana", "cherry", "apple"]
print(mylist)

#mylist2 = list()  creating an empty list and then we can append items
mylist2 = [5, 100, 25, 1, -5, -100]
print(mylist2)

#item = mylist[5]  #IndexError: list index out of range
item = mylist[-2]  # -1 is apple -2 is cherry -3 is banana
print(item)
print("")
for i in mylist:  # every element in the list = i then we print i every time
    print(i)
print("")
if "banana" in mylist:  #check if there is an item in the list or not
    print("yes")
else:
    print("no")
print("")

print(len(mylist))
print("")

mylist.append("lemon") #addin another elements
print(mylist)
mylist.insert(1,"blueberry") #insert an element in an exact index
print(mylist)
print("")

item_pop = mylist.pop() # saving the (index) element in the list to a variable and remove it from the list
print(item_pop)
print(mylist)
print("")

item_removed = mylist.remove("cherry") #remove the specified element
print(item_removed)
print(mylist)
print("")

#mylist.clear() #clears the list
#print(mylist)

mylist.reverse() #reverse the list
print(mylist)
print("")

#mylist2.sort() #sorting the list in ascending order
#print(mylist2)  #this will change the original list

new_list_sorted = sorted(mylist2)
print(mylist2)
print(new_list_sorted)
print("")

mylist3 = [0]*5
print(mylist3)
print("")

concatenate = mylist3 + mylist2 #adding 2 lists together
print(concatenate)
############################Slicing###############################
print("")
print("")

mylist4 = [1, 2 ,3 ,4 , 5, 6 ,7 ,8 ,9]
a = mylist4[1:5] #will take the 2nd element [1] and will not take the 5th element [5]
print(a)   #[2, 3, 4, 5]
a = mylist4[:5]
print(a)
a = mylist4[1:]
print(a)
a = mylist4[1:4:2] # steps >> 1st index = start, 2nd index = stop, 3rd index = step
print(a)     #[2, 4]
a = mylist4[::-1] # another way to reverse the list
print(a)     #[2, 4]
print("")

mylist4_copy = mylist4
mylist4_copy.append(100)
                            # the problem with this method that any change will affect both lists
print(mylist4_copy)
print(mylist4)

mylist4_real_copy = mylist4.copy()  #real copy does not affect the original one
mylist4_real_copy = list(mylist4)   #same as .copy
mylist4_real_copy = mylist4[:]      #slicing all the elements so doing the same as .copy
mylist4_real_copy.append("green")
print(mylist4_real_copy)
print(mylist4)
print("")

b = [i*5 for i in mylist4]  # another way of creating a list of another list
print(b)
##########################################################################################