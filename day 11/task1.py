def merge(l1, l2): 
      
    m = [(l1[i], l2[i]) for i in range(0, len(l1))] 
    return m 
      
# Driver code 
l1 = [1, 2, 3] 
l2 = ['a', 'b', 'c'] 
print(merge(l1, l2)) 