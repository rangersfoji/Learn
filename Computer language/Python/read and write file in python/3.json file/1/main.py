import json

'''
we will learn 4 mehods
1. json.load(f)   : load json data from file(or file-like object)
2. json.loads(s)  : Load Json data from a string
3. json.dump(j,f) : Write Json object to file(or file-like object)
4. json.dumps(j)  : Output Json object as string
'''


# load (json file --> dict)
# (for json file access)
'''
with open('data.json','r',encoding="utf-8") as read_jfile:
    movie = json.load(read_jfile)
    
print(movie) # data from data.json file
print(type(movie))  # ot = dictionary
print(f"direcotr : {movie['credits']['director']}")

# converted : json --> python
# object --> dict
# array --> list
# true --> True
# false --> False
# null --> None
# string --> str
# int --> int
# real number --> float
'''


# loads (json string--> dict)
# (for online website data store into string variable than convert into python dictionary)

value = """

            {
                "title" : "Tron: Legacy",
                "composer" : "Daft Punk",
                "release_year" : 2010,
                "budget" : 170000000,
                "actors" : null,
                "won_oscar" : false
            }

        """

print()
tron = json.loads(value)
print(tron)
print(f'type : {type(tron)}')



# dumps (dict --> json string)
new = json.dumps(tron,ensure_ascii=False)
print()
print(new)
print(f'type : {type(new)}')


# dump (dict --> json file)
movei2 = dict(
    title = 'Minority Report',
    director = 'Steven Spielaberg',
    composer = 'json williams',
    actors = ['tom cruise','colin farrell','samantha morton','max von sydow'],
    is_awesome = True,
    budget = 102000000,
    cinematographer = 'janusz Kami\u0144ski'
)

with open('result.json','w',encoding='utf-8') as write_jfile:
    json.dump(movei2,write_jfile,ensure_ascii=False)
    
    