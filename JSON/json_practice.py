import json

# the dumps and loads work for a string inside the files itself

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": [
                "johnsmith@bogusemail.com",
                "john.smith@work-place.com"
            ],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

data = json.loads(people_string)
print(data)
print(type(data))
print(type(data['people']))
print()

for person in data['people']:
    print(person['name'])
    person.pop('phone')
    
new_string = json.dumps(data, indent=2, sort_keys= True)
print(type(new_string))
print(new_string)