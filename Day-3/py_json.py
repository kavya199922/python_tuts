#loading  json data from file
#serialization:json=>python dict
#read data (json) from a file:
# convert:python(dict)
import json
with open('dat_json.json','r') as f:
    data=json.load(f)
print((data))

str1='''
{
     "23": {
          "name": "Jonas",
          "email": "jonas23@gmail.com",
          "role": "manager"
     },
     "47": {
          "name": "Martha",
          "email": "martha47@gmail.com",
          "role": "Team Lead"
     }
}
'''


# print((json.loads(str1)))
# #deserialization:python->JSON
#
#
person_dict = {
    'name': 'Bob',
     'age': 12,
     'children': None,
    'ismarried':False
}
person_json = json.dumps(person_dict)

# Output: {"name": "Bob", "age": 12, "children": null}
print((person_json))


#write to a file


person_dict = {
    "name": "Bob",
    "languages": ["English", "Fench"],
    "married": True,
     "age": 45
}

with open('person1.json', 'w') as json_file:
  json.dump(person_dict, json_file)