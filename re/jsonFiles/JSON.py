import json
my_JSON = """
        {
        "employees":
        [
        {
            "name": "Jason Ogola",
            "age": 55,
            "career": "Buisnessman",
            "ailmeny": null,
            "married": true
        },
        {
            "name": "Kevin Mugo",
            "age" : "45",
            "career": "Doctor",
            "ailment": "athsma",
            "married": false
        }
    ]
}"""

people = json.loads(my_JSON)

#print(people)
"""for peps in people['employees']:
    print(peps["career"])"""

#changing people back to a json string using the dump key word
for peps in people['employees']:
    del(peps["career"])

people2 = json.dumps(people, indent=2)

#print(people2)

#open our json file
with open('countries.json') as f:
    data = json.load(f)
    for objects in data['countries']:
        print(objects['{:s}'.format("country")]+"----president is "+ objects['{:s}'.format("president")])

        



