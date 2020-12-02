import re
results = re.finditer(r"([0-9]{1,3})", "123 456 789")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))