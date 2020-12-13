number_list = [12, 18 ,24,27 ,35,45]
res = list(filter(lambda x: (x % 9 == 0), number_list))
print("Numbers that are divisible by 9 ",res)