number_list = [12, 18 ,24,27 ,35,45]
res = list(filter(lambda x: (x % 15 == 0), number_list))
print("Numbers that are divisible by 15 ",res)