import mysql.connector as mysql

pythonDataTypes = [
    ("int", 6),
    ("float", "7.5"),
    ("complex", "5-2j"),
    ("str", "BestEnlist"),
    ("list", "[1,3,7,9,11]"),
    ("tuple", "(1,3,5,7,9,11)"),
    ("bool", "True"),
    ("set", "{1,3,5,7,9,11}"),
    ("dict", "{'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}")
]

conn = mysql.connect(host="localhost", user="root",
                     password="", database="", port="3308")

cursor = conn.cursor()

insert_query = "INSERT INTO datatypes(datatype,example) VALUES(%s, %s)"

cursor.executemany(insert_query, pythonDataTypes)

conn.commit()

if cursor:
    print("Data inserted successfully")
    select_query = "SELECT * FROM datatypes"
    cursor.execute(select_query)
    for data in cursor:
        print(data)
else:
    print("Error")

conn.close()
