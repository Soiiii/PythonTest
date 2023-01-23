#JavaScript Object notation
#Json represents data as nested "lists" and "dictionaries"
import json
data = '''{
"name": "Chuck",
"phone" : {
    "type": "intl",
    "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
        }
    }'''
info = json.loads(data)
print('Name:', info["name"]) #Name: Chuck
print('Hide:', info["email"]["hide"]) #Hide: yes

import json
input = '''[
    {"id" : "001",
    "x": "2",
    "name" : "Chuck"
    },
    {"id" : "009",
    "x" : "7",
    "name" : "Chuck"
    }
]'''

info = json.loads(input)
print('User count:', len(info)) #User count: 2
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
# Name Chuck
# Id 001
# Attribute 2
# Name Chuck
# Id 009
# Attribute 7