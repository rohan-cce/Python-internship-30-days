list1 = [12,25,83,92,56,18,35] 

even_count = len(list(filter(lambda x: (x%2 == 0) , list1))) 
  
print("Even numbers in the list: ", even_count) 