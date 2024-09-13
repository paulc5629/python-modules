#Exercise 6 Task 1
Enya = {
    "first_name":"Enya",
    "last_name":"Ryan",
    "age": 28,
    "location": "Glasgow"
}

Paul = {
    "first_name":"Paul",
    "last_name":"Callaghan",
    "age": 32,
    "location": "London"
}

people=[Enya,Paul]

for person in people:
    print(f"{person['first_name']} {person['last_name']} is {person['age']} years old and lives in {person['location']}.")
