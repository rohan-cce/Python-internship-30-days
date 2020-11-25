cities_south_india={"Tamilnadu":"Chennai",
              "Tamilnadu":"Coimbatore",
              "Karnataka":"Bangalore",
              "Andhra_pradesh":"Vizag"
              }
cities_north_india={"Maharastra":"Mumbai",
                    "Rajastan":"Jaipur",
                    "Delhi":"Delhi"
                    }
cities_south_india.update(cities_north_india)
cities_india = cities_south_india.copy()

print(cities_india)
