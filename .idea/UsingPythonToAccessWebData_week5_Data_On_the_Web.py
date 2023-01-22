# Data on the Web
# With the HTTP Request/Response well understood and well supported,
# there was a natural move toward exchanging data between programs using these protocols
#
# We needed to come up with an agreed way to represent data going between applications and across networks
# There are two commonly used formats: XML and JSON

#eXtensible Markup language (XML)
#Primary purpose is to help information systems share structured data
#It started as a simplified subset of the Standard Generalized Markup Language(SGML),
#and is designed to be relatively human-legible

#White Space
# Line ends does not matter.
# White space is generally discarded on text elements. We indent only to be readable

# XML Terminology
# Tags indicate the beginning and ending of elements
# Attributes - Keyword/value paris on the opening tag of XML
# Serialize/De-Serialize - Convert data in one program into a common format that
# can be stored and/or transmitted between systems in a programming language-independent manner

#XML as a Tree
# a - b , c ( d-e)
# <a>
#  <b>X</b>
#  <c>
#    <d>Y</d>
#    <e>Z</e>
#  </c>
#  </b>

#XML Schema
#Describing a "contract" as to what is acceptable XML
#Description of the legal format of an XML document
#Expressed in terms of constraints on the structure and content of documents
#Often used to specify a "contract" between systems - "My system will
# only accept XML that conforms to this particular Schema."
# If a particular piece of XML meets the specification of the Schema
# it is aid to "validate"

import xml.etree.ElementTree as ET
data = '''<person>
<name>Chuck</name>
<phone type="intl"> +1 734 303 4456 </phone>
<email hide="yes"/></person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

import xml.etree.ElementTree as ET
input = ''' 
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text) #Name Brent
    print('Id', item.find('id').text) #Id 009
    print('Attribute', item.get("x")) #Attribute 7