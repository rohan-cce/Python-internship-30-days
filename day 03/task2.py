cities_south_india={"Tamilnadu":"Coimbatore",
                    "andhra_pradesh":"vizag",
                    "karnataka":"bangalore",
                    "goa":"panaji",
                    "Delhi":"Delhi"
                    }

print("Dictionary before deleting element = \n")

for key,value in cities_south_india.items():
    print("Key : {} , Value : {}".format(key,value))

print()

cities_south_india.pop('Delhi')

print("Dictionary after deleting element = \n")

for key,value in cities_south_india.items():
    print("Key : {} , Value : {}".format(key,value))
