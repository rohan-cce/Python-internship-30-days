list1=[1,2,3,5,9]

print("appending 7 to the list ")
print("List before = ",list1)
list1.append(7)
print("List after =",list1)

print("Deleting 2 from the list")
print("List before = ",list1)
list1.remove(2)
print("List after =",list1)

largest,smallest=max(list1),min(list1)

print("Largest is {} , Smallest is {}".format(largest,smallest))
