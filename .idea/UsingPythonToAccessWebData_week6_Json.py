import json

data = '''
{
"name":"Chuck",
"phone":{
    "type":"intl",
    "number":"+1 734 303 4456"
    },
    "email":{
        "hide":"yes"
    }
}'''
#json.loads => it parses and converts from the JSON syntax into a python
info =json.loads(data)

print('Name:', info["name"]) #Name: Chuck
print('Hide:', info["email"]["hide"]) #Hide: yes
