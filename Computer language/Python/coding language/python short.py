pwd 
ls
clear 
cd c://
mkdir "new folder" 
mkdir 1 2 3 4 = to 1 2 3 4 eva char folder bane .
cd .. 
touch "new file.txt" 
touch "new file.py" 
touch "new file.java" 
touch new_file.py 
rm new_file.py 
rm -rf new_folder
code hello.py
python hello.py 
mv old_file.py new_file.py 
mv file.py path ex.c/new_folder 
cp copyfile.py path jyamove karavo che 
^ arrow e last code laci de.


6. 
   print("hello world")
   print('hello world')
   "" and '' nu stuff like
                    ' "" ' and " '' "  right
                    " "" " and ' '' ' wrong

7. escape sequences : 
    1. \' = '
    2. \" = "
    3. \\ = \
    4. \n = new line  - aama vachhe space chodso to new line ma lakhan pela space aavase. 
    5. \t = tab  - tab button dabavie etli space chode. 
    6. \b = backspace 

8. comments :
   1. comments e user mate hoy.
   2. # ni pachalnu comment aave.
   3. ctr + / aakhi line ne comment karava mate. and uncomment karava mate pan.
   4. multiline ne comment karava mate '''  and  ''' ni vachhe lakhay.

9. escape sequences as a normal text :
   1. \' = \\'
   2. \" = \\"
   3. \\ = \\\\
   4. \t = \\t
   5. \b = \\b 

12. raw string : 
    print(r"line a \n line b") emna em print mate


14. python as a calculator :
   
    
    1. +  addition(saravalo)
    2. -  subtration (badabaki)
    3. *  multiplication (gunakar)
    4. /  float devision (bhagakar)    -  2.5 and 2.0
    5. // integer devision (bhagakar)  - 2 and 3  [0.2 = 0 ]
    6. %  modulo (shesh)
    7. ** exponent (gat)  
    8. round  =  print(round (2**0.5,4) )
    9. precedence rule and associativity rule  : 

        precedence rule :   1. ()
                            2. **   (gat)
                            3. *,/,//,%
                            4. +,-

        associativity rule : 1. ()  ma highest   ex. be () ma je moto te pela
                             2. **  ma right to left  ex. print(2**2**3)  = 256 
                             3. *,/,//,%  ma left to right.
                             4. +,-  ma left to right

15 variable
  variable ma su lai shakay [sting, int , float , koi pan number] 


16.  (string concatention) 
      first_name = "karan " 
      last_name = "patel" 
       
      full_name = first_name + " "+ last_name  
      print (full_name)  
      output = karan patel
                                                                
17.  user input 
   name = input("please enter your name : ") 
   print ( "hello " + name )         # input function hamesha input string ma j lese  


18. int () function

   number1 = str(4) 
   number2 = float("4") 
   number3 = int("33") 
   print(number2 + number3) 
   output = 77.0 [ matalb int + float thay pan final output float ma aave ] 
 
19. more about variable
  
  name, age = "karan ", 24 
  print ("hello"+ name + "your age is "+ str(age)) 
 
  x=y=z=1 
  print(x+y+z) 
  output = 3 
 
20. more than one input in one line
 
 name = input ("enter your name : ") 
 age = input ("enter your age : ") 
  
 [ aana badle ek j line ma] 
 name,age = input ("enter your name and age").split()   
 print (name) 
 print (age) 
 out put = enter your name and age karan 24 [default 'space' and  .split(",") ] 
 
21. string formmating 
       python 3
       print ("hello {} your age is {} " .format(name, age)) 

       python 3.6 <=
       print(f"hello {name} your age is {age}")  [f""  string ni agal f lagavanu na bhulta] 
 
22. string indexing 
    name = 'karan'
    name[0] = k 
    name[-1] = n


23. string slicing
    name = 'karan'
    name[0:2] = ka 
    name[2:-1] = ran 

24. step argument 
    "karanpatel"[0:5:1] output = karan  
    "karanpatel"[0:5:2] output = krn  
    "karanpatel"[0::2] output = krnae  
    "karanpatel"[0::3] output = kaal  
    "karanpatel"[::-1] output = letapnarak 
    "karanpatel" [4::-1] output = narak 
    "karanpatel"[-1::-1] output = letapnarak  
    "karanpatel"[::-1] output = letapnarak
 
25. string methods part 1
  name = 'karan'

  len(name)
  name.lower()
  name.upper()
  name.title()
  name.count('a') # case sensitive
  
 
26. strip method and solve precious problem of spaces  
  name = '    karan    '
  name.lstrip() = 'karan   '
  name.rstrip() = '   karan'
  name.strip() = 'karan'


27. replace and find method 
  string = "she is beautiful and she is good dancer." 

  print(string.replace(" ","_"))  
  print(string.replace("is","was",1))  
  print(string.find("is"))   output = 4
  print(string.find("is",5))  output = 25  
  print(string.find("is", string.find(is) + 1))   output = 26 
      

 
28. center method with programm

  name = "karan" 
  print(name.center(7,"*"))    output = *karan*   
  print(name.center(9,"*"))
                     
29. string are immutable

30. more assignment operator       
  +=
  *=
  /=
  -=

31. if statement
  age = int(input('enter your age : '))
  if age > 12:
    print('you are teenage.')

 
32. pass statement
 if True :
  pass    # pass means kai nahi
 
33. else statement
  age = int(input('enter your age : '))
  if age > 12:
    print('you are teenage.')
  else :
    print('you are child')
  

34. random int
  import rendom 
  winning_num =  random.randint(1,50)     [ ahi (1,50) no matalab 1 and 50 and temni vacheeno thay ema 1 and 50 pan aave] ]    


35. tutorial and , or operator

   'and'

   name = "karan" 
   age = 17 
   if name == "karan" and age == 17 :  
      print("condition true.") 
   else :  
      print("condition false.") 
 
  
  'or'

   name = "karan" 
   age = 17 
   if name == "karan" or age == 17 :  
      print("condition true.") 
   else :  
      print("condition false.") 


37. if...elif...else statement
 age = int(input("enetr your age : ")) 
    
 if 0<age<= 3 : 
       print("ticket prince : free.") 
 elif 3<age<=10: 
       print("ticket price : 150") 
 elif 10<age<=60: 
       print("ticket price : 250") 
 elif 0==age or 0>age: 
     print("you enter invalid value.") 
 else: 
       print("ticket price : 200") 
 
38. in keyword
  name = "karan" 
  if "a" in name :    or if "a" in "karan" :  
      print("a is present in name.") 
  else: 
        print("not present.") 
  output = present 
 
39. check empty or not (important)
  name = "abc" 
  if name :         [ ahi if name : no matalb aa statement e check kare che k name empty che k nahi jo name empty hoy to hello print nahi thay nahitar jo kai pan hase to print hello thai jase.] 
      print("hello") 


  name = input('enter your name : ')
  while len(name)<1:
    name = input('enter your name : ').strip().title()
   
40. tutorial (while loop)

    i = 1  
    while i<= 10: 
        print("hello world.") 
        i = i + 1 

 
    i = 1  
    while i<= 10: 
        print(f"{i} hello world.") 
        i = i + 1 


41. sum of numbers program using while loop 
   total = 0 
   i = 1 
 
   while i<= 10: 
     total += i 
     i += 1  
     
   print(total) 
 

44. infinite loop : 
    while True:
      print('hellow')


45. for loop : 
 
   for i in range(10):    
     print('hello world')


   #
   1 thi 10 no sum

   total = 0
   for i in range (1,11) : 
     total += i

  #

  name = input("enter your name : ")
  tv = ""
  for i in range (0,len(name)) : 
    if name[i] not in tv : 
      print(f" {name[i]} : {name.count(name[i])}")


49. break and continue :

 for i in range(1,11) : 
  if i == 5 : 
    break
  print(i)


 for i in range (1,11) :
   if i == 5 :
     continue
  print(i)

50. exercise : 
      
      sikhava jevu : game_over = False
                     while not  game_over : 
                        if winning_number == user_number : 
                            print(f"winner winner !!!  , you guessed the number in {i} times.")
                            game_over = True 


52. step argument in range function : 

        for i in range (1,11,2):
            print(i)
 
        out put :  1
                   3
                   5..
                   9


        for i in range (0,11,2):
            print(i)
 
        out put :  0
                   2
                   4..
                   10


        for i in range (10 , 0 , -1 ) : 
              print(i)

        output : 10
                 9
                 8..
                 1

                 fo 0 sudhi javu hoy to (10 , -1 , -1)

        for i in range (1,-11,-1) :
           print(i)


        out put : 1
                  0
                  -1
                  -2...
                  -10        


53. for loop and string :

  other laguage : 
    name = "karan"
    for i in range (len(name)):
        print(name[i])
                
    output : k
            a
            r
            a
            n

    python :
        name = "karan"
                for i in name: 
                  print(i)


            output : k
                      a
                      r
                      a
                      n




                          
                    


54.  function into :   (important)

         
         potana function define karo :  function aapada mate kai pan work kari shke.

                               
                               def name_func(a,b) :         
                                  return a + b               

                              # use:

                              name_func(5,4)   output = nothing 
                              print(name_func(5,4))   output = 9
                                
                            
                               

55. return vs print

  def add_three(a,b,c):
       return a+b+c

    add_three (5,5,5)

    output = nothing 



   def add_three(a,b,c):
       print (a+b+c)

    add_three (5,5,5)

    output = 15
 

56. function practice :

      1. def karan(i) :
            return i[-1]


    
      2. def karan (i) : 
            if i%2 == 0 :
              return True
            else :
              return False

                    or 

      3. def karan (i) : 
          if i%2 == 0 :
            return True
          return False

                  or 

        def karan (i) : 
          eturn i%2 == 0 

                
        print(karan(9))


        ahi  i  = peramiter   and 9 = argument 


        4.   def karan():
                return "hiiii all"



60. print method :


for i in range (10) :
  print(i,end = " ")

output = 1 2 3 4 ... 10


  
#
    a = 0 
    b = 1
    print(a,b) 
    output = 0 1 
    
    

61. fibonacci series program :



def phibonaki (n):
    a = 0
    b = 1
    if n == 1 :
        print(a)
    elif n == 2:
        print(a,b)
    else :
       
        print(a,b , end = " ")
        for i in range (n-2) :
            c = a + b
            a = b 
            b = c 
            print(b , end  = " ")

n = int(input ("enter a number : "))
phibonaki(n)

62. default peramiter : 


  def user_info(first_name,last_name,age = 23) :
      print(f"your first name is {first_name}")
      print(f'your last name is {last_name}')
      print(f"your age is {age}")

    user_info('karan','patel')
         
  # jyar thi default aapo , tena pachi badha pera meter ne default aapavu pade

63. variable scope : 


  x = 5     
  def karan():
    global x 
    x = 7
    return x

  print(karan())
  print(x)

   output = 7
            7    kaaran k global variable ne badali didho che. 

    pan  jo print (x)
            print(karan())  hot to output = 5
                                            7  aavat karan k fuction ma x badalay te pela  print thai jay che. 

  #
  #  pan aa na karay karan aama global variable ne badalo to difficulte thai jay badhu so .



64. list 

  list = ordered collection of items 
  list ma int , float and string add kari shako


  numbers = [1,2,3,4]


  print(numbers[1])
  ot = 2


  words = ["word1",'word2','word3']


  print(words[:2])
  ot = ['word1','word2']


  mixed = [1,2,3,4,"five","six",2.3,None]       # python ma None means nothing   not zero and python ma int , float and string eki sathe ek j list ma add kari shakay che.
  print(mixed)


  print(mixed[-1])


  mixed[1] = 'two'
  print(mixed)
  ot = [1,'two',3,4,"five","six",2.3,None] 


  mixed[1:] = 'two'
  print(mixed)
  ot = [1,'t','w','o'] 


  mixed[1:] = ['three','four']
  print(mixed)
  ot = [1,'three','four'] 


  mixed[:0] = ['zero'] 
  print(mixed)
  ot = ['zero',1,'two',3,4,"five","six",2.3,None] 



  'add data in list' : 
   

  append('karan')
  insert(0,'karan')


  'combine 2 or more list'


  1. + vali     = aanathi 2 list  k vadhare joint thay 
  list1 = [1,2,3,4]
  list2 = [5,6,7,8]
  lists = list1 + list2
  print(lists)
  ot = [1,2,3,4,5,6,7,8]

  2. extend method = aanathi  2 list na aliment e 1 ma umeray  extend thay.
  list1 = [1,2,3,4]
  list2 = [5,6,7,8]
  list1.extend(list2)
  print(list1)
  ot = [1,2,3,4,5,6,7,8]


  list1 = [1,2,3,4]   = jo append vaparro to aliment na badale list extend thai jay.
  list2 = [5,6,7,8]
  list1.append(list2)
  print(list1)
  ot = [1, 2, 3, 4, [5, 6, 7, 8]]   

  'delete data from list' 
  1. pop
  2. del
  3. remove 


  ls.pop()  default : delete last aliment
  ls.pop(1) where 1 = position 
  # pop return deleted value
  list1 = [1,2,3,4]
  deleted = list1.pop()
  print(list1)
  print(deleted)
  ot = [1,2,3]
       4

  del ls[0]
  del ls[1:-2]

  remove('karan') # pass aliment value not position


  ls = [1,2,3]
  if 2 in ls:
    print('yes')
  else:
    print('no')

  for i in ls:
    print(i)



  some more list method :

  ls.count('karan')

  ls = [2,4,3,1]
  ls.sort()
  print(ls)

  ls.sorted() # sorted return kare che , you can store in different variable

  ls.clear()

  ls = [1,2,3]
  l2 = copy(ls)   #  ls == l2 and copy are different



  'compare list' :  (is vs =)

  1. is vs == 

    is check same memory
    == check same value



  'join method and split method'  : 

  1.split (string to list)
  names = '123,456,789,456,789,564,13,456,789,456'
  ls = names.split(',')
  print(ls)
  output = ['123','456',...]


  2. join method  (list into string)
  user_info = ['karan','17']
  print(','.join(user_info))
  karan,17                           


72. list vs string :

  string = immutable
  list = mutable 


74. list inside list

  matrix = [[1,2,3],[4,5,6],[7,8,9]]  # 2d list
  for i in matrix:
    print(i)
  ot = [1,2,3]
       [4,5,6]
       [7,8,9]

  for i in matrix :
    for j in i :
      print(j)
  ot = 1
       2
       3
       4
       5
       6
       7
       8
       9

  print(mtrix[1][1])
  ot = 5


  print(type(ls)) = list 



75. more about list :

  1.
  numbres = [1,2,3,4,5,6,7,8,9,10]
  numbers1 = list(range(1,11))    #same


  2. index method 
  numbres = [1,2,3,4,5,6,7,8,9,10,1]
  print(numbres.index(1))
  ot = 0

  numbres.index(su shodhavanu,kai podistion thi chalu karavanu,kya atakavanu)


  3. pass list to a function
  list1 = [1,2,3,4,5,1,6,9,8,1,2,5,6,9,4,1,5,6,9,1]
  def negative_list (i) :
    tv = []
    for i in list1 :
        tv.append(-i)
    return tv

  print(negative_list(list1))


81. min and max function :

  numbers = [10,50,30]
  print(min(numbers))
  ot = 10

  print(max(numbers))
  ot = 50


82. exercise 6 :

  def sub_list_check(i):
      total = 0
      for j in i :
          if type(j) == list :
              total += 1 
      return total
  ls = [1,2,3,[3.1,3.2,3.3,3.4],4,5,6,[6.1,6.2,7,8,9]]
  print(sub_list_check(ls))

  ot = 2


83. intro  to tuples

  tup = ('one','two',3,4,5)
  tuples  are faster than list

  (no append ,no insert , no pop , no remove)

  methods which we can use in tuples = count , index , len , slicing


  print(tup[2])



  1. lopping in tuples 
  ls = (1,2,3,4.0,'karan')
  for i in ls:
    print(ls)


  2. tuple with one element 
  ls = (1)   wrong (int)
  ls2 = (1,)  right (tuple)


  3. tuple without parenthesis
  names = 'karan','neel','nikhil'    = tuple


  4. tuple unpacking 
  names = 'karan','neel','nikhil','mit'
  name1,name2,name3,name4 = (names)
  print(name3)



  5. list inside tuples    =   tuple ni andar jo list hoy to data add and remove kari shakay.
  num = (1,2,3,[3.1,3.2,3.3])
  num[3].pop() right
  num.pop(3) wrong

  num[3].append(3.4)
  num[3].pop(0)


  6. min() , max , sum
  num = (1,2,3,[3.1,3.2,3.3])
  print(min(num))

  ot = error  to sub tuple k list na hovi joie

  num = (1,2,3,4,5)
  print(min(num),max(num),min(num)+max(num))

  ot = 1 5 6


85. function returning two values:

  def kar(i,j):
      s = i + j
      g = i * j
      return s,g

  ot = (30, 200)  when more than 1 value, tuple return kare.
  solution = saravalo , gunakar = kar(a,b)    aam tene variable ma add kari devay
  print(saravalo)
  print(gunakar)



86. tuple , list , string  more :

  num = tuple(range(1,11))

  nums = list((1,2,3,4,5,6,7,8,9,10))

  nums = str((1,2,3,4,5,6,7,8,9,10))
  print(nums)
  print(type(nums))

  ot = (1,2,3,4,5,6,7,8,9,10)
       string    because  in real '(1,2,3,4,5,6,7,8,9,10)'


87.  intro to dictionaries :


  how to create dectionaries:

  1.
  user = {'name' : 'karan' , 'age' : 17}
  print(user_info,type(user_info))

  ot = {'name': 'karan', 'age': 17} <class 'dict'>

  2. 
  user_info = {
              'name' : 'karan' , 
              'age' : 17
              }

  3.
  user_info1 = dict(
      name = 'karan' , 
      age = 17
      )


   
  how to access data from dictionaries  :

  1.

  print(user_info1[0])
  ot = error      because dictionaries unorder collection of data che. dictionaries has no index.


  print(user_info1['name'])
  print(user_info1['age'])



  which type of data can we store in dictionary ?
     numbers, string , list , dictionari , anything like list

  users = {
    'user1' : {

              }
          }   aam dictionary ni andar dictionary pan store kari shakie chi and complex data ne pan store kari shakie chie.

    

  how to add data to empty dictionary : 

  user_info2 = {}
  user_info2['name'] = 'karan'
  user_info2['age'] = 17

  {'name': 'karan' , 'age': 17}

  and if name was alredy there then it would update the value 



  looping and in keyword in dictionary : 


  if 'name' in dic:
      print('present')
  else :
      print('not present')



  if 17 in dic.values():
      print('present')
  else :
      print('not present')


  loops in dictionari :

  1. keys :

  for i in dic:
      print(i)

  2. values :

  for i in dic.values():
      pritn(i)
    

  3. values method :

  user = dic.values()
  print(user,type(user))

  ot = dict_values(['karan', 17]) <class 'dict_values'>

  print(user[0]) error!!
  ls = list(user)
  print(ls[0])


  4. keys method : 

  user = dic.keys()
  print(user,type(user))

  ot = dict_keys(['name', 'age']) <class 'dict_keys'>

  5. key looping

  for i in dic:
      print(i)

     values looping

  for i in dic:
      print(dic[i])
      or
  for i in dic.values():
      print(i)

  6. items method (most useful)

  for i in dic.items():
     print(i,type)

  ot = ('name', 'karan') <class 'tuple'>
       ('age', 17) <class 'tuple'>

  or 

  a = dic.items()
  print(a,type(a))

  ot = dict_items([('name', 'karan'), ('age', 17)]) <class 'dict_items'>


  7. use of items method

  for i , j in dic.items():
      print(f"{i} : {j}")
      print(type(i),type(j))

  ot = name : karan
      <class 'str'> <class 'str'>
      age : 17
      <class 'str'> <class 'int'>

  # tuple unpacking thai che.



  add and delete data from dictionari:

  user = dict(
        name = 'karan',
        age = 17,
        gender = 'male',
  )

  1. add data : 
  user['fav_song'] = song1

    
  2. pop method : 
  print(user.pop('fav_song'))  # retrun deleted value


  3. popitem method 
  print(user.popitem())   # return deted value and key
  aanathi last key and value delete kari de.



90. update method in dectionry:
  dic = dict(
      name = 'karan',
      )

  more_info = dict(
      address= 'c/9 vijay flats',
      pincode = 380004)

  dic.update(more_info)


  more_info = dict(name = 'neel')
  dic.update(more_info)   # if key are same than it will update the value of key



91. dictionary more methods:

  1.fromkeys
  d = dic(name = 'nuknown',age = 'unknown')  # default value 'unknown' 
          if different key --> same value then


  d = dict.fromkeys(['name','age','height'],'unknown')
          

  d = dict.fromkeys("abc",'unknown')
  ot = {'a': 'unknown', 'b': 'unknown', 'c': 'unknown'}


  d = dict.fromkeys(range(1,11),'unknown')

  d = dict.fromkeys(['name','age'], ['apple','pineapple'])
  ot = {'name': ['apple', 'pineapple'], 'age': ['apple', 'pineapple']}


  2. get method (useful)

  d = dict(name='karan',age=17)
  print(d['address'])  
  ot = error!

  print(d.get('address'))
  ot = None


  if d.get('address'):
      print('present')


  user = dict(name = 'karan',age = 17)
  print(uesr.get('address','not found !')) # retrun value


  3. clear

  d.clear()


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
       b  # because 'unordered collection of data'

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


94. if else with list comprehension

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
  # if 2 normal perameter --> at least 2 argument

  def total (*args,num): wrong (because jetala num pass karao badha args ma jase)



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


104. vertual envirment for project


python -m venv myenv   (make virtual envirment)
pip list   (install pip dependecies)
myenv/Scripts/activate.bat   (for activate envirment)  (for windows cmd)
source myenv/Scripts/activate   (for bash)
deactivate    (for deactivate envirment)
pip install --upgrade pip   (upgrade pip for install external ex. requirments.txt  file)
where python  (see which python is using this project # see top one)
pip fabric   (for pip freeze)
pip freeze   (print list for which pip this project has)
pip freeze -> requirments.txt    (make file output of pip freeze)
pip install -r requirments.txt   (install external file pip)


105. pickel (module)

""" it's like when you want to create file and save one thing for temperari and then retrive but pickel make it easy"""

# write pickle
with open("name.pkl","wb") as file_variable: #here .pkl not neccessery
  pickle.dump("value",file_variable) # here value can be any object

# read pickle
with open("name.pkl","rb") as file_variable:
  var = pickle.load(file_variable)

""" important Note: to delete pickle file after use can not be done in function/method"""
