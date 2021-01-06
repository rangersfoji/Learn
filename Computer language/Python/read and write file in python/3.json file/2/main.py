import json
from urllib.request import urlopen

# j_string --> p_string
"""
people_string = '''
        {
            "people" :
            [
                {
                    "name" : "john smith",
                    "phone" :  3155557164,
                    "emails" : ["johnsmith@bogusemail.com","john.smith@work-place.com"],
                    "has_license" : false
                },

                {
                    "name" : "jane doe",
                    "phone" :  5605555153,
                    "emails" : null,
                    "has_license" : true
                }
            ]
        }
    '''

py_people = json.loads(people_string,encoding='utf-8')
print(py_people)
print(type(py_people)) # ot = dict

print('\n')
for person in py_people['people']:
    del person['has_license']
    print(person['name'])
    print(person)
"""


# p_string --> j_string
'''
j_string = json.dumps(py_people,ensure_ascii=False,indent=2) # indent for readable text (play with it)
# you can use sort_keys = True for dumps
print(j_string)
print(type(j_string))
'''


# j_file --> p_dict
'''
with open('data.json','r') as read_file:
    data = json.load(read_file)

    for state in data['states']:

        del state['area_codes']

        with open('result.json','w') as write_file:
            write_data = json.dump(data,write_file,indent=3)
'''

# J-string --> p_dict
'''
with urlopen('http://citibikenyc.com/stations/json') as responce:
    source = responce.read().decode('utf-8')
    
data = json.loads(source)
del data['executionTime']
res = {}

for i in data['stationBeanList']:
    
    del i['id']
    del i['availableDocks']
    del i['totalDocks']
    del i['latitude']
    del i['longitude']
    del i['statusValue']
    del i['statusKey']
    del i['city']
    del i['postalCode']
    del i['location']
    del i['altitude']
    del i['landMark']
    
   
with open('test.json','w') as write_f:
    json.dump(data,write_f,indent=3,ensure_ascii=False,sort_keys=True)
'''


