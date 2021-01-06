89.
    labeled break and continue in python 
    python do not have this but we can create

      example:
        while True:
        	main_break = False

        	for i in range(10):
        		print(i)
        		if i == 5:
        			main_break = True
        			break

        	if main_break:
        		break
          
        # but in for loop if you used   for i in range  then  
        # 	  in nasted for loop use    for j in range 

90. update method in dectionry:
    dic = dict(
        name = 'karan',
        age = 17
        roll = 27)

    more_info = dict(
        address= 'c/9 vijay flats',
        pincode = 380004)

    dic.update(more_info)
    print(dic)

    ot = {'name': 'karan', 'age': 17, 'roll': 27, 'address': 'c/9 vijay flats', 'pincode': 380004}


    more_info = dict(name = 'neel')
    dic.update(more_info)
    print(dic)

    ot = {'name': 'neel', 'age': 17, 'roll': 27, 'address': 'c/9 vijay flats', 'pincode': 380004}

    if key are same than it will update the value of key

91. dictionary more methods:

    1.fromkeys
    d = dic(name = 'nuknown',age = 'unknown')  # default value 'unknown' 
            if different key --> same value then


    d = dict.fromkeys(['name','age','height'],'unknown')
                or
    d = dict.fromkeys(('name','age','height'),'unknown')
    print(d)
    ot = {'name': 'unknown', 'age': 'unknown', 'height': 'unknown'} 


    d = dict.fromkeys("abc",'unknown')
    print(d)
    ot = {'a': 'unknown', 'b': 'unknown', 'c': 'unknown'}


    d = dict.fromkeys(range(1,11),'unknown')
    print(d)
    ot = {1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown', 5: 'unknown', 6: 'unknown', 7: 'unknown', 8: 'unknown', 9: 'unknown', 10: 'unknown'}


    d = dict.fromkeys(['name','age'], ['apple','pineapple'])
    print(d)
    ot = {'name': ['apple', 'pineapple'], 'age': ['apple', 'pineapple']}


    2. get method (useful)

    d = dict(name='karan',age=17)
    print(d['address'])  
    ot = error!


    print(d.get('address'))
    ot = None
    print(d.get('name'))
    ot = karan 


    if 'name' in d:
        print('present')
        or
    if d.get('address'):
        print('present')
    else:
        print('not present')

    here : if None means if False thay

    user = dict(name = 'karan',age = 17)
    print(uesr.get('address','not found !')) # retrun value



    3. clear

    d.clear()
    print(d)
    ot = {}


    4. copy

    d1 = d.copy()
    print(d1)

    5. len , count ....

    count:

    d = dict.fromkeys(['name','age'], ['apple','pineapple'])
    print(d['name'].count('apple'))


92. set (data type):

    snordered collection of unique items

    note : set can store [flot,int,string,tuple]
           set can not store [list,dictionary,set]
    s = {1,2,3,2}
    print(s)
    ot = {1,2,3}


    use : (remove duplicate)
    ls = [1,2,5,5,5,6,6,4,3,2,1,1,5,6,9,8,8,8,7,7]
    s = set(ls)
    print(s)

    ot = {1, 2, 3, 4, 5, 6, 7, 8, 9}


    how i use : 
    ls = [1,2,5,5,5,6,6,4,3,2,1,1,5,6,9,8,8,8,7,7]
    ls = list(set(ls))
    print(ls)


    methods : 

    1. add

    s = {1,2,3}
    s.add(4)
    s.add(5)
    s.add(4)
    print(s)

    ot = {1,2,3,4,5}

    2. remove

    s.remove(3)
    print(s)
    ot = {1,2,4,5}

    3. discard

    s.remove(8)
    print(s)
    ot = error

    s.discard(8)
    print(s)
    ot = ot = {1,2,3,4,5}

    4. clear

    s.clear()

    5. copy

    s1 = s.copy()

    6. more

    ls = [1,485,5,85,8,87,87,56,44,5,56,5,56,84,84,5,54,4,84,8,6,5,55]
    ls = list(set(ls))
    print(ls)

    ot = [1, 4, 5, 485, 6, 8, 44, 84, 85, 54, 87, 56, 55]  # because list and set = 'uordered collection'

    solution:

    ls = [1,485,5,85,8,87,87,56,44,5,56,5,56,84,84,5,54,4,84,8,6,5,55]
    ls = list(set(ls))
    ls.sort()
    print(ls)

    ot = [1, 4, 5, 6, 8, 44, 54, 55, 56, 84, 85, 87, 485]


    7. 
    s = {1,1.0,2.3,'string'}
    print(s)
    ot = {1,2.3,'string'}

    s = {1,1.1,2.3,'string'}
    print(s)
    ot = {1,1.1,2.3,'string'}

    8. 

    s = {'a','b','c'}
    if 'a' in s:
        print('present')
    ot = present

    for i in s:
        print(i)
    ot = c
         a
         b

    7. use of set

        1. remove duplicate
            ls = [1,2,3,3]
            ls = list(set(ls))
            print(ls)
            ot = [1,2,3]

        2. math (union , intersectoin)
            
            s1 = {1,2,3,4}
            s2 = {3,4,5,6}

            union:
            s3 = s1 | s2
            print(s3)
            ot = {2,2,3,4,5,6}


            intersectoin:
            s3 = s1 & s2
            print(s3)
            ot = {3,4}

93. list comprehension

    1.
    squares = []
    for i in range(1,11):
        sqaures.append(i**2)
    print(squares)
    ot = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    vs 

    squares2 = [i**2 for i in range(1,11)]
    print(squares2)
    ot = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    2.
    ls = [-i for i in range(1,11)]
    print(ls)
    ot = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

    3.
    ls = ['karan','neel','nikhil']
    f = [i[0] for i in ls]
    print(f)
    ot = ['k', 'n', 'n']


94. if  with list comprehension

    1. 
    ls = list(range(1,11))
    even = [i for i in ls if i%2 == 0]
    print(even)
    ot = [2, 4, 6, 8, 10]

    2.
    odd = [i for i in range(1,11) if i%0 != 0]
    print(odd)
    ot = [1, 3, 5, 7, 9]

    3.
    ls = [True,1,2,5,98,9.80,9.0,81,'kran','alsdkf',[1,2,5],dict(name = 'neel',age=16)]

    def filter_nums(list):
        return [str(i) for i in list if (type(i) == float or type(i) == int) ]

    print(filter_nums(ls))
    ot = ['1', '2', '5', '98', '9.8', '9.0', '81']

95. if and else with list comprehension:

    ls = list(range(1,11))
    l2 = [-i if(i%2 != 0) else i*2 for i in ls]
    print(ls,'\n',l2)
    ot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
          [-1, 4, -3, 8, -5, 12, -7, 16, -9, 20]

96. nasted list comprehension:

    res = [[1,2,3],[2,3,4],[4,5,6]]
    ls = [[i for i in range(1,4)] for j in range(3)]
    print(ls)
    ot = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

97. dictionary comprehension:

    # square dictionary like {1:1,2:4,3:9...}
    square = {i:i**2 for i in range(1,11)}
    print(square)
    ot = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

    dic = {f'square of {i}':i**2 for i in range(1,11)}
    print(dic)
    ot = {'square of 1': 1, 'square of 2': 4, 'square of 3': 9, 'square of 4': 16,
         'square of 5': 25, 'square of 6': 36, 'square of 7': 49, 'square of 8': 64, 
         'square of 9': 81, 'square of 10': 100}

    name = input('enter your name : ')
    dic = {i:name.count(i) for i in name.uppeer()}
    print(dic)
    ot = enter your name : karan
        {'K': 0, 'A': 0, 'R': 0, 'N': 0}

98. if else with dictionary comprehension:

    d = {i: ('odd' if(i %2 != 0) else 'even') for i in range(1,11) }
    print(d)
    ot = {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd',
          8: 'even', 9: 'odd', 10: 'even'}

99. set comprehension (rare case ma use thay)

    s = {i**2 for i in range(1,11)}
    print(s)
    ot = {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}

    names = ['karan','neel','dhaval','meet','dinesh','mitali','kiran','nikhil']
    first = {i[0] for i in names}
    print(first)
    ot = {'m', 'k', 'd', 'n'}

100. intro to *args
    '''
    make flexible functions with it
    *operateor or *args  (like overloading in java)

    '''
    def total(a,b):
      return a+b
    print(total(1+2+3))
    ot = error


    def all_total(*args): # professionl use 'args' you can write anything but use args
      print(args)


    def total(*args):
        print('args : ',args,'  , type: ',type(args))

    total(1,2,3,5,'karan',9,'aldskf')
    ot = args :  (1, 2, 3, 5, 'karan', 9, 'aldskf')   , type:  <class 'tuple'>

    --------------------
    def total(*args):
        total = 0
        for i in args:
            total += args
        return total

    print(total(1,2,3))
    ot = 6

    # here '*' is responsible for this not 'args'


101. *args with normal perameter

    def multiply(num , *args):
        res = 1
        for i in args:
            res *= i
        return res

    print(multiply(2,3,2))
    ot = 6  # because here first 2 is normal perameter

    # here you have to pass at least one value because of one normal perameter
    # if you don't want to pass argument in args then it won't give error!

102. *args as argument

    def multiply(*args):
        res = 1
        for i in args:
            res *= i
        return res 

    ls = [2,3,4]
    print(multiply(ls))
    ot = [2,3,4]

    solution:
    print(multiply(*ls))
    ot = 24

    # here '*' unpack the list
    # you can do this with tuple,set,list



    def Power(power,*args):
    if args:
        return [i**power for i in args]
    else:
        return 'hey!! you didn\' pass args'

    ls = [1,2,3]
    power = 2
    print(Power(power,*ls))



103. **kwargs (double star operator)

    # kwargs as a perameter
    def func(**kwargs):
        print(kwargs)
        print(type(kwargs))

    func(first_name = 'karan',last_name = 'patel')

    ot = 
    {'first_name': 'karan', 'last_name': 'patel'}
    <class 'dict'>

    * --> tuple , ** --> dictionary

    def func(**kwargs):
        for i , j in kwargs.items():
            print(f"key : ",i,"value : ",j)

    func(first = 'karan',last = 'patel')
    ot = key :  first ,value :  karan
         key :  last ,value :  patel


    ------------
    # kwargs with normal perameter
    def func(name,**kwargs):

    ----------
    # dectionary unpacking
    def func(**kwargs):
        for i , j in kwargs.items():
            print(i,j)

    d = dict(name = 'karan',age = 12, address = 'c/9 vijay flats')
    func(**d)



104. function with all types of perameter

