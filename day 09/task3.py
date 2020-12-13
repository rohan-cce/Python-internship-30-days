number_list = [3,6,9,12,15]
n = 3
print("List before multiplication ", number_list)
print("Given number ", n)
final_number=list(map(lambda number:number*n,number_list))
print("List after multiplication")
print(' '.join(map(str,final_number)))