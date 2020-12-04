n= [1, 2, 4, 5, 7, 8, 10, 11]
def filter1(num):

    if(num % 2) == 0:
        return False
    else:
        return True
out = filter(filter1, n)
print(list(out))