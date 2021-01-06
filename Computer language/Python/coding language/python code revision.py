0. command line : 
 
   pwd = kaya folder ma cho e batave
   ls = list matalab aa folder ma su che eni list.
   clear 
   cd c:// = aanathi tame c drive ma move thai jao  short cut mate "tab" button dabavavu.
   mkdir "new folder" = aanathi navu new folder name nu folder bani jay. "" malakho jo space na chodavi hoy to nahi to emnam lakho.
   mkdir 1 2 3 4 = to 1 2 3 4 eva char folder bane .
   cd .. = back aava mate.
   touch "new file.txt" = file banavava mate.
   touch "new file.py" = python ni file banavava mate.
   touch "new file.java" = java ni file.
   touch new_file.py = "" vagar banavi hoy to.
   rm new_file.py = file delete karava mate.
   rm -rf new_folder = folder delete karava mate.
   code hello.py = coding karava mate.
   python hello.py = file run karava mate . windows user mate pan jo tame linux user hoy to tamare python3 lakhavu.
   mv old_file.py new_file.py = rename karava mate.
   mv file.py path ex.c/new_folder = move karava mate.
   cp copyfile.py path jyamove karavo che = copy and paste karava mate.
   ^ arrow e last code laci de.

6. print("hello world")
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

10. exercise

11. solution

12. raw string : 
    print("line a \\n line b") 
          or
    print(r"line a \n line b") pan pachi aama escape sequence na use kari shakay.

13. how to print emoji :
    1. wbsite = https://unicode.org/
    2. ema jya + hoy try 000 karava and aagal \ lagavavo ex.print("hi lol lol lol  \U0001F923")
    3. pan aagal and pachal space jove j ek emoji pachi.


14. python as a calculator :
    print(2+3)
    print(2+3*4)
    
    1. +  addition(saravalo)
    2. -  subtration (badabaki)
    3. *  multiplication (gunakar)
    4. /  float devision (bhagakar)    - aama point pachini kimmata batave and na hoy to zero pan batave ex. 2.5 and 2.0
    5. // integer devision (bhagakar)  - aama point pachini kimmata batave nahi ex. 2 and 3 pan jo 0.2 aave to e 0 batave.
    6. %  modulo (shesh)
    7. ** exponent (gat)  ex. 2 ni 3 gat to print(2**3)
                          ex. 2 nu vargmul to print(2**0.5)
    8. round  = moti kimmat  0.64646849849564 ne round karava mate vaparay.
                ex. print(round (2**0.5,4) ) to aama , pachi 4 lakho to point pachi 4 kimmat j batave.
                notes : 1. jo point pachi 2 kimmat round karavani hoy and point pachi 1 j kimmat hoy to em na em j rahe che. ex. 1.225 nu 1.23    pan    1.2 nu 1.2 j.
                        2. input ma tame string lo pan point ni kimmat levi hoy to   int ma nahi feravavano pan  float ma feravavavo. karan int ma point ni kimmat na aave.
    
    9. precedence rule and associativity rule  : 
         jyare moti ganatari hoy like print(2*32**5-5//5) to e kai rite thay pela su thay e mate na aa rule che. gujarati ma  bhagusaba.

         precedence rule :  1. ()
                            2. **   (gat)
                            3. *,/,//,%
                            4. +,-

        associativity rule : 1. ()  ma highest   ex. be () ma je moto te pela
                             2. **  ma right to left  ex. print(2**2**3)  = 256 
                             3. *,/,//,%  ma left to right.
                             4. +,-  ma left to right

15. variables,rules, conventions :
  
 
 ''' number1 = 2  
     print (number1)  
     output = 2  
      
     number1 = 2 
     print (number1) 
     number1 = 4 
     print (number1) 
     output = 2 
              4 
      ''' 
 # variable ma su lai shakay [sting, int , float , koi pan number] 
 ''' name = "karan" 
     print = (name) 
     output = karan 
      
      name = "karan" [string ne "" ma j lakhay] 
     print = (name) 
     output = karan 
     name = 123 
     print = name 
     output = karan 
              123 ''' 
 
 # variable na niyamo 
 # 1. variable number thi chaluna rakhay ex. 1num = 2 na chale 
 # 2. variable e letter and _ thi chalu kari shakay ex. _name = "karan" 
 # 3. variable ma spacial symbol na vapri shakay e pan pahel pan nahi and pachee pan nahi ex . $,@,! vagere 
 # 4. variable ma number vachhe chale ex. num1= 2 
 
 # variable na convanion 
 # username = "karan " [ahi variable ma vadhare letter hoy to tene chuta padava mate space na chale enamate vacche (_) vapri shakay.] 
 # ex. user_one_name  [aa writing ne = snake case writing] 
 # ex. userOneName  [aa writing ne = camel case writing kahe] 
 # aanathi koi farak na pade pan vanchvama saru re 

16.  (string concatention) 
 '''  first_name = "karan " 
      last_name = "patel" 
       
      full_name = first_name + " "+ last_name  
      print (full_name)  
      output = karan patel''' 
 # tame string sathe number na + kari shake ex. print(frist_name + 3) output = error!! [karan k tame string sathe number na + kari shako to solution print (first_name + "3" or str(3) ) output = karan3 ] 
 # pan aam kari shko [ print ( first_name * 3 ) out put = karankarankaran] 
 # pan aam kari shako [ print ( (first_name + "\n" ) * 3 ) ] out put = karan
                                                                  #    karan 
                                                                  #    karan

                                                                
17.  user input 
 # name = input ("please enter your name ") 
 # print (name ) 
 # output = je nam lakho te 
 '''  
   name = input("please enter your name : ") 
   print ( "hello " + name )         # input function hamesha input string ma j lese  
 ''' 
 # ex  age = input ("type you age.") 
 #     print ("your age is " + age)         
 #     output = your age is 17  [ tethi aa input string che  "17" karan jo na hot  to error aapt karan sting + int na thay  tethi aa input hamesha string ma le. ]                                                                                                                
     
18. int () function
  '''  
   number_1 = input ("enter number1.") 
   number_2 = input ("enter number2") 
   total = number_1 + number_2 
   print ("your total is " + total ) 
    
   jo hi pela 10 
         pachi 20 
         to out put = 1020 aave [karan input string ma leche tethi "10" + "20" = 1020 
          
    to solutuion :  
    number_1 = int(input ("enter number1.")) 
   number_2 =  int( input ("enter number2")) 
   total = number_1 + number_2 
   print ("your total is " + total ) 
             
            pan aama haji problem karan gave total int ma che and chelle string + int na thay to  
 
            solutution : 
                 number_1 = int(input ("enter number1.")) 
                 number_2 =  int( input ("enter number2")) 
                 total = number_1 + number_2 
                 print ("your total is " + str(total) ) 
             or 
     
    number_1 = input ("enter number1.") 
   number_2 = input ("enter number2") 
   total = int(number_1) + int(number_2) 
   print ("your total is " + total ) 
    
             pan aama haji problem karan gave total int ma che and chelle string + int na thay to  
 
             solutution : 
                 number_1 = int(input ("enter number1.")) 
                 number_2 =  int( input ("enter number2")) 
                 total = number_1 + number_2 
                 print ("your total is " + str(total) )''' 
   
  # str 4--> "4" 
  # int "4" --> 4  
  # float "4" --> 4.0  
 
  #  number1 = str(4) 
  #  number2 = float("4") 
  #  number3 = int("33") 
  #  print(number2 + number3) 
  #  output = 77.0 [ matalb int + float thay pan final output float ma aave ] 
 
19. more about variable
  
  # name, age = "karan ", 24 
  # print ("hello"+ name + "your age is "+ str(age)) 
 
  # x=y=z=1 
  # print(x+y+z) 
  # output = 3 
 
20. more than one input in one line
 
 # name = input ("enter your name : ") 
 # age = input ("enter your age : ") 
  
 # [ aana badle ek j line ma] 
 # name,age = input ("enter your name and age").split()   
 # print (name) 
 # print (age) 
 # out put = enter your name and age karan 24 [ ahi vache space karvu pade karan space 24. pan space na badle , vaparvu hoy to .split(",") karavu pade] 
 
21. string formmating 
 #   name = "karan" 
    #  age = 17 
    #  print("hello " + name + "your age is " + str(age) )  [bau lambu sentence] 
 
    #  [python 3 (gani badhi language ma ) ni rit] 
       #print ("hello {} your age is {} " .format(name, age))  [ahi age int ma che k string ma teni koi chinta karava ni  jarur nathi.] 
       # [ahi thodi calculation pan kari shakay che ex. print ("hello {} your age is {} " .format(name, age + 2 ))] 
    #  [ python 3.6 (aa python 3.6 ma , pan gani var jyare online python progrram run karavo pade to python 3.6 vali aarit nathi chalti to tena mate python 3 ni rit vaprvi pade.)] 
       # print(f"hello {name} your age is {age}")  [f""  string ni agal f lagavanu na bhulta] 
       # [ahi thodi calculation pan kari shakay che ex. print (f"hello {name} your age is {age + 2 }")] 
 
22. string indexing 
    # language = "python" 
    # [ahi position = index number (position ne indexing number pan kahevay.) ] 
    # [position hamesha 0 thi chalu thay che.] 
    # [ ahi language ma p=0 , y=1 , t=2 , h=3 , o=4 , n=5 position ma che.] 
    # [ ex. ahi jo t print karavo hoy to [ print(launguage[2])  ]] 
    # [ ex. ahi jo o print karavo hoy to [ print(launguage[4])  ]] 
    # [ ex. ahi jo [ print(launguage[6])  ] karishu to error aavse karan k jetla charecter hoy tenathi vadhare number hoy to error aave.] 
    # [ ex. ahi jo n print karavo hoy to [ print(launguage[-1])  ] jo tamne nathi khabar k string ma ketla cheracter che to tamare jo chello akshar print karavo hoy to [-1] lakhavu and tevi rite pachadthi print karava hoy to (-) thi chalu karavu pan ahi 1 thi chalu karavu.] 
 
23. string slicing
 # lang = "python" 
 # [jo ahi python ma aapde matra p or t or h or y or o ...  jeve akshar print karavava matte print(lang[1]) em karata pan ek karata vadhare akhar print karava hoy ex. py or pyt or hon em to ena mate aa vapray ] 
 # [ kai rite lakhay [ start argument : stop argument -1 (ahi -1 no matlab am che k jo hu 2 lakhu to ahi -1 thaine 1 aavse and jo hu -1 lakhu to -1 thaine -2 aavse)]  ] 
 # [ex. print(lang[0:2]) output = py  ] 
 # [ex. jo mare tho print karvu che to [ print(lang[2:5])  output = tho ]] 
 # [ pan jo lang = "python " hoy and jo mare pytho print karavu che to [ print ( lang[0:-1] )  ]   ave pan ahi output = python aayu karan ahi "python " che tehi ahi last space ni space pan count thay che tethi.] 
 # [ have print(lang[:] )  jo ahi start and stop banne argument na lakho to output = python aave, etle k aakhi string print thai ne aave.] 
 # [ have print(lang[1:]) to output = ython aave , etle k jo stop argument na lako to and sudhi print thai jay.] 
 # [ heve print(lang[:3]) to output = pyt aave , etle k jo start argument na lako to 0 thi start thay and ahi stop argument ma 3 etle 3-1=2 etle t sudhi print thayu .] 
 # [ ahi jaruru nehi k variable ma j thay  ex. ptint("karan" [2:5])  output = ran ] 
 
24. step argument 
 # [ print("karanpatel"[0:5:1]) output = karan ] 
 # [ print("karanpatel"[0:5:2]) output = krn  karan ahi [0:5:2] ma [0:5] no output karan aave pan trijo (:2) e step no che matalab ahi k pachi a nahi and r pachi a nahi and n ] 
 # [ print("karanpatel"[0::2]) output = krnae  karan ahi [0::2] ma [0:] no output karanpatel aave pan trijo (:2) e step no che matalab ahi k pachi a nahi and r pachi a nahi and n .... ] 
 # [ print("karanpatel"[0::3]) output = kaal  karan ahi [0::3] ma [0:] no output karanpatel aave pan trijo (:3) e step no che matalab ahi k pachi a nahi and r pachi a nahi and n .... ] 
 # [ ahi step vala etle ke trija : ma 1 etle normal , 2 etle 1 chodi 1 , 3 etle 2 chodi ek ... ] 
 # [ print("karanpatel"[::-1]) output = letapnarak karan k ahi (::) no output = karanpatel and step no (:-1) matalab normal pan revers ma tethi undho print thay che  ] 
 # [ print ("karanpatel" [4::-1]) output = narak karan k ahi (4::-1) ma chalu 4 etle k (n) thi end( :) etle and sudhi pan jo start and stop be j hoy to npatel thy pan ahi step (:-1) che etle revers ma chelle sudhi matalb k (k) sudhi ] 
 # [ uper na ex. ma [4::-1] ma jo start su dhi javu hoy to [4::-1] aam j lakhay pan jo [4:0:-1] lakho to nara aave karan  [4:0:-1] jeva tran start , stop and step em 3 aave tyare 1.ni position 0 thi chalu thay and pachi bijo 1 ... , 2. ma posion ahi 3 box matej ( :) thi chalu thay and bija ni (0) 3. to step no che em position na hoy .] 
 # [ print("karanpatel"[-1::-1]) output = letapnarak ] 
 # [ print("karanpatel"[::-1]) output = letapnarak ] 
 
25. string methods part 1
 # [aa tutorial ma 5 function sikhvana.] 
 # [1. len() = function  ] 
 # [2. lower() = method ] 
 # [3. upper() = method ] 
 # [4. title() = method ] 
 # [5. count() = method ] 
 
 # [ 1. len()  [len function aapdi string ma ketla akshar che tane janava mate]] 
 # [ print(len("karan")) output = 5  ahi len func. karan na akshar gane che and print tene print kare che] 
 # [ print(len(input("enter word k jena akhar tame ganva mangta hoy : ")))] 
 # [ ahi space pan ganavama aave ] 
 
 # [ 2. lower() = method  [string ma badha akshar ne small letter ma karava]  ] 
 # [ a = "KaRAnPateL"] 
 # [ variable or sting.lower()] 
 # [ a.lower() or "KaRAnPateL".lower() aa badhane karanpatel ma ferave and print karavava  [ print(a.lower())  output = karanpatel ] or [ print("KaRAnPateL".lower()) output = karanpatel ]  ] 
 
 # [ 3. upper() = method   [ string ma badha akshar ne capital lette ma karava vapray.]] 
 #  [ a = "KaRAnPateL"] 
 # [ variable or sting.upper()] 
 # [ a.upper() or "KaRAnPateL".upper() aa badhane KARANPATEL ma ferave and print karavava  [ print(a.upper())  output = KARANPATEL ] or [ print("KaRAnPateL".upper()) output = KARANPATEL ]  ] 
 
 # [ 4. title() = method [string ma pela akshar ne cepital letter ma bija badhane small ma karava pan space pachi no word lo pelo akshar cepital and bija small tatha (.) (,) act... jeva koi pan sybol and number pachi tarat lakhelo sting pelo akshr cepital ma aave che]  ] 
 # [ a = "KaRAn PateL"] 
 # [ variable or sting.title()] 
 # [ a.title() or "KaRAn PateL".title() aa badhane Karan Patel ma ferave and print karavava  [ print(a.title())  output = Karan Patel ] or [ print("KaRAn PateL".title()) output = Karan Patel ]  ] 
 
 #  [ 5. count() = method [string ma koi akshar or letter ne count  karava]  ] 
 # [ a = "KaRAnPateL"] 
 # [ variable or sting.count("h")  ahi ("")ma je word k akshar count karavoy te lakhavo.] 
 # [ a.count("a") or "KaRAnPateL".count("a") to print("KaRAnPateL".count("a")) output = 1  karn ahi a 1 var che bujo A cepital che tethi te na ganay. ] 
 # [ ahi cepital H ne count("H") ma lakhyo hoy and tame h lakho to te count thato nathi] 
 
 # print(f"   hello i am {} "  ma {} ma "" fari na aavi sake etle {} ma input na levay and count method na levay pan len , lower , upper , title method levay    pan .format vali rit ma input levay. )  
 
26. strip method and solve precious problem of spaces  
 # name = "   karan    "   [ len() func ma space pan ganati ti e problem ne solve karava mate strip method vaparay.] 
 # dots = ".........."     [ strip space ne remove kare che.] 
 # [left space ne remove karava mete [   lstrip() method ]] 
  # ex. print (name + dots)  output =    karan   ..........  
  # ex. print (name.lstrip() + dots)  output = karan    .......... 
 # [right space ne remove karava mete [   rstrip() method ]]  
  # ex. print (name + dots)  output =    karan   ..........  
  # ex. print (name.rstrip() + dots)  output =    karan.......... 
 # [left and right space ne remove karava mete [   strip() method ]]  
  # ex. print (name + dots)  output =    karan   ..........  
  # ex. print (name.strip() + dots)  output = karan.......... 
 # [ pan jo tamara string ma vachhe space hoy to strip method ene remove nathi karati ex. print("   kar   an   ".strip.() )  to output = kar   an] 
 # [ jo variable k string ma jetla pan space che badha remove karava hoy to tamare [  replace method vaparvi pade.]  ] 
  # ex.  name.replace(" ","") output = karan  [ ahi  name.replace(" ","") ma replace method ma ( " ","") no matalab pela jene remove karavu che te string ma and bija ma jenathi replace karavu che te string ma lakhavu ahi aapde " " space ne "" etle kai nahi thi replace karayu etle jya jya pan space hase tya tya "" etle non space aavi jase. ] 
  # ex. print(name.replace(" ","") + dots)  output = karan.......... 
 
27. replace and find method 
 # string = "she is beautiful and she is good dancer." 
 
 # replace method :- 
 # print(string.replace(" ","_"))  output =   she_is_beautiful_and_she_is_good_dancer. 
 # print(string.replace("is","was"))  output = she was beautiful and she was good dancer.  [ badha is was ma replace thai gaya.] 
 # [jo 1 is ne was sathe replace karavu hoy and bija is ne is j reva devu hoy to ]   print(string.replace("is","was",1))  output = she was beautiful and she is good dancer.  [ 1 is was ma replace thai gayo. jo , 2 lakhyu hot to 2 is was ma replace thay pan , 3 lakhayu hot to pan kai fer na padat karan ahi 2 j is che etle banne is was ma replace thai jay.] 
  
 # find method :- 
 # [ find method thi aapdi string ma koi word ni position khabar pade and character ni position pan find karai shakie aapdi sting ma .] 
 # ex.  print(string.find("is"))   output = 4   [ ahi is ni position 4 che ene 1 is ni kahi and 1 is jyathi chalu thay che te position kahi didhi.] 
 # [jo mare bija is ne find karavo hoy to print(string.find("is",5))  output = 25   ahi ("is",5)   ma (,5) no matalab have te 5 position thi find karavanu chalu karase] 
 # [ahi find method ma is aam hoy k iskara hoy pan position banne ma position batavej che] 
 # [ pan jo aapan ne 1 is ni position khaba na hoy and aapde 2 is ni position janavi hoy to] 
 # [ be rit] 
   # 1. a = find("is") + 1 
      #   print(find("is", a)) 
      #   output = 26 
 
   # 2. print(string.find("is", string.find(is) + 1)  ) 
     #  output = 26 
 
28. center method with programm
 # [center method] 
 ''' name = "karan" 
      print(name.center(7,"*"))    output = *karan*    [ahi name.center() karan k method che pachi name.ceter(7,"*") ma (7,"*") no matalab ahi tamara name ni lenth 5 che and tame 7 lakhyu etle 2 vadhare and (,"*") ma * no matalab tamare name ni aajubaju su lagavu che to to output = *karan*] 
                    [ jo tame (6, "*")  lakyu hot to   output = *karan   or karan* rendom li aave ,  ahi (6," ")  " "  ma tamare aju baju je lagavu che te string ma lakhvu] 
                  [ jo tame print (name.center(4, "*"))      lakho to output  =  karan aave    
                  [jo 2 star ad karavahoy to print(name.center(9,"*")) ] 
                  ''' 
                     
29. string are immutable
 # string = "karan" 
 # print(string[1]) 
 # output = a 
 
 # string = "karan"  [ have mare aa variable ma karan ma (a) ne (A) ma bladalvo hoy to hu na badlli shaku karan string immutable che. tame ek var string banai to tame badli na shako] 
  
 # string = "karan" 
 # print(string.replace("a","A")) 
 # output = kArAn 
 
 # string = "karan" 
 # print(string.replace("a","A")) 
 # print(string) 
 # output = kArAn 
 #          karan   [ eno matalb k replace method thi string change thati nathi aam string immutable che . replace method e string ne change nathi karti te navi string creat kare che. pachi te navi string ne tame variable ma store karavi sako cho.] 
             
30. more assignment operator       
 
  # name = "karan"  [ pan mare patel umervu che yad rakho string badalase nahi pan variable badli shakay . ] 
  # name = "karan" + "patel" 
  # or name += " patel" 
  # print(name)  
  # output = karan patel  
 
  # age = 17 
  # age = age + 1 
  # or age += 1 
  # print (age) 
  # output = 18 
 
  # [ tevi rite *,/,-,+ badha mate *= , /= , -= , +=  vapri shakay.] 
  # ex . num = 10 
         # num *= 3 
         # print(num) 
         # output = 30 
 
31. if statement
  #  [if condition che ] 
 
  # age = input("enter your age : ") 
  # age = int (age) 
  # if age >= 14 : 
  #    print("your are above 14.") 
  # [ jo tame  13 enter karo to output kai na male pan 14 karo to output = you are above 14. ] 
  # [ ahi dhyan rakhvu jo tame >=10 or <= 10 aapo condition aa rite thay (10 and 10 thi vadhare ) and (10 and 10 karata ochi .)] 
  # [ jo mare 12 karata ochi jovti hoy to <=11 lakhvu pade] 
 
32. pass statement
 
 # x = 18 
 # if x > 18 : 
 # output = error!! 
 
 # [ ahi jo kai na lakhvu hoy if statement ma to pass lakay.] 
 # x = 18 
 # if x > 18: 
   #  pass 
 # output = kai na aave 
 
33. else statement
 # [ else statement if pachi lakhay] 
 # age = input("enter your age : ") 
 # if age >= 14 : 
 #       print("you are above 14 .") 
 # else :  
 #       print("you ain't above 14 . ")  [ jaru ri nathi if hoy to else hoy pan else ekli na hoy , and else hamesha if pachi aave .] 
  
34. gussing game exsercise
  # name = input("enter your name : ") 
  # age = input("enter your age : ") 
 
  # input("This is number guessing game , in this game you have to choose one number between 1 to 50 , if you choose correct number you will win the game or you loss game. press enter to start game .") 
 
  # winning_num = 27 
  # guessing_num = int(input("guess one number between 0 to 50 : ")) 
 
  # if winning_num == guessing_num : 
  #     print("congratulation you win the game!!!!") 
  # else: 
  #     if 0 <= guessing_num <= winning_num: 
  #         print("your number is too low.") 
  #     elif 50 >= guessing_num >= winning_num: 
  #         print("your number is too high.") 
  #     else :  
  #         print("you enter invalid number.") 
 
 
  # [ and ahi apde (<= ne badele < vapri shako pan pachi -1< gussing_num aave )  (tevi j rite > pan vapri shakay pan 51> gussing_num aave.)] 
  # [pan aama winnig_num e 27 fix che pan aapde redom number mate  
  #     import rendom 
  #     winning_num =  random.randint(1,50)     [ ahi (1,50) no matalab 1 and 50 and temni vacheeno thay ema 1 and 50 pan aave] ]    
 
35. tutorial and , or operator
   # [ 2 comdition eki sathe check karava mate vapray] 
 
   # and operator  
   # name = "karan" 
   # age = 17 
   # if name == "karan" and age == 17 :  
   #    print("condition true.") 
   # else :  
   #    print("condition false.") 
   # output = jo karan and 17 aapyu to condition true nahitar condition false. 
   # [ ahi and operator ma jo banne condition sachi hoy to j condition true nahitar be manthi koi pan ek khoti hoy to condition false aave.] 
 
   # or operator  
   # name = "karan" 
   # age = 17 
   # if name == "karan" or age == 17 :  
   #    print("condition true.") 
   # else :  
   #    print("condition false.") 
   # output = jo karan and 17 mathi koi pan ek condition sachi to condition true jo banne sachi to pan condition true pan jo banne condition khoti hoy to condition false. 
   # [ ahi or operator ma jo banne mathi koi ek pan  condition sachi hoy to  condition true and banne schi hoy to condition true batave nahitar bnne  khoti hoy to condition false aave.] 
 
36. exercise 
 # name = input("enter your name : ") 
 # age = int(input ("enter your age : ")) 
 
 # if 0 >= age : 
 #     print("you enter invalid age.") 
 # elif name.upper()[0] == "A" and age >= 10 : 
 #     print("you can watch coco movie.") 
 # else : 
 #     print("sorry , you cannot watch coco movie.") 
 
 #  [or] 
 
 # name = input("enter your name : ") 
 # age = int(input ("enter your age : ")) 
 
 # if 0 >= age : 
 #     print("you enter invalid age.") 
 # elif (name[0] == "A" or name[0] == "a") and age >= 10 : 
 #     print("you can watch coco movie.") 
 # else : 
 #     print("sorry , you cannot watch coco movie.") 
 
37. if...elif...else statement
 # age = int(input("enetr your age : ")) 
    
 # if 0<age<= 3 : 
 #       print("ticket prince : free.") 
 # elif 3<age<=10: 
 #       print("ticket price : 150") 
 # elif 10<age<=60: 
 #       print("ticket price : 250") 
 # elif 0==age or 0>age: 
 #     print("you enter invalid value.") 
 # else: 
 #       print("ticket price : 200") 
 
38. in keyword
  # name = "karan" 
  # if "a" in name :    or if "a" in "karan" :  
  #     print("a is present in name.") 
  # else: 
  #       print("not present.") 
  # output = present 
 
39. check empty or not (important)
  # name = "abc" 
  # if name :         [ ahi if name : no matalb aa statement e check kare che k name empty che k nahi jo name empty hoy to hello print nahi thay nahitar jo kai pan hase to print hello thai jase.] 
      # print("hello") 
 
   # name = input("enter your name : ") 
   # if name: 
   #      print(f"hello {name}") 
   # else : 
   #      print("plz enter name , you can\'t enter nothing.") [ maro programm ho name ma kai input kare to else statement print thase nahitar if statement print thase.] 
    
40. tutorial (while loop)  
   # print("hello karan.")  [ jo mare 10 var print karavu hoy to while loop or for loop vapray.] 
   #                        [ while loop thi j kam kari shakay te kam for loop thi pan kari shakay pan khali banne na sintex alag che pan banne shikhava jaruri che.] 
   #  i = 1  
   #  while i<= 10: 
   #      print("hello world.") 
   #      i = i + 1 
   #  output = hello world. 
   #           hello world. 
   #           hello world. 
   #           hello world. 
   #           hello world. 
   #           hello world. 
   #           hello world. 
   #           hello world. 
   #           hello world. 
   #           hello world. 
 
   #  i = 1  
   #  while i<= 10: 
   #      print(f"{i} hello world.") 
   #      i = i + 1 
   #  output = 1 hello world. 
   #           2 hello world. 
   #           3 hello world. 
   #           4 hello world. 
   #           5 hello world. 
   #           6 hello world. 
   #           7 hello world. 
   #           8 hello world. 
   #           9 hello world. 
   #           10 hello world.   [ jo i = 0 thi start karyu hot to 11 var print that.] 
 
41. sum of numbers program using while loop 
   # total = 0 
   # i = 1 
 
   # while i<= 10: 
   #   total += i 
   #   i += 1  
     
   # print(total) 
 
42. exercise 
     
    # i = 1
    # j = int(input("enter your number : "))
    # total = 0
    # while i <= j :
    #     total += i
    #     i += 1
    # print(total)

43. exercise 

    # name = input("enter your name : ")
    # i = 0
    # tv = ""

    # while i <= len(name) :
    #     if name[i] not in tv :
    #         tv += name[i]
    #         print(f" {name[i]} : {name.count(name[i])} ")
    #     i += 1

44. infinite loop : 
    # reson : 1. mistakely
    #         2. aapani maraji thi 
    # stop karava mate :  ctr + c

   
    #  1. mistakely
    # i = 0
    # while i <= 10 
    #   print("hello world")

    #  2. aapani maraji thi  (important)
      
      # while true : 
      #    print('hello world')
    
    '''  python ma  be bulian 
         1. true
         2. false    '''

45. for loop : 
 
  #  for i in range(10):     (ahi range (10)  no matalab  0 thi 9 pan jo 1 thi 10 karavu hoy to range(1,11) karavu. )
  #    print('hello world')

46. for loop example 1 :
  #  1 thi 10 no sum

  # total = 0
  # for i in range (1,11) : 
  #   total += i
47. for loop example 2 : 

# num = input("enter number : ").strip()
# total = 0
# for i in range(0,len(num)):
#   total += int(num[i])

48. for loop example 3 : 

# name = input("enter your name : ")
# tv = ""
# for i in range (0,len(name)) : 
#   if name[i] not in tv : 
#     print(f" {name[i]} : {name.count(name[i])}")


49. break and continue :

# break keyword ne loop ne break karava mate vaparay

for i in range(1,11) : 
  print(i)

# pan mare 5 value aave tarat j loop break karavi hoy to 

# for i in range(1,11) : 
#   if i == 5 : 
#     break
#   print(i)

# ahi  aave etle loop break thai jay.
 


#  continue :

# print 1 thi 10 pan 5 print nahi karava na 

# for i in range (1,11) :
#    if i == 5 :
#      continue
#   print(i)

# ahi continue aave to loop skip thi jay 
# ex. i ni value 5 thay etle continue na lidhe te for par jump mare etle 5 print na thay .
# pan jo print(i) e  if  statement ni pela hot  to 5 print thia jay karan k continue ni niche nu skip thay pan pela nu nahi.

50. exercise : 
      
      sikhava jevu : game_over = False
                     while not  game_over : 
                        if winning_number == user_number : 
                            print(f"winner winner !!!  , you guessed the number in {i} times.")
                            game_over = True 

51. dry principle of coding :
       # means : don't repeat yourself 
      # aagal number gauessing game ne modify karati vakhate aapade  user_number = int(input("guess again !  : "))     varam varar lakhyu eni vadale aapade simple bar lakhi didhu hot to e badha mate work karat to elte aane dry principle kahevay.
                                                                   # i += 1

      # have number geussing game na diffierent solutions : 
        '''     1. game_over na badale     while True kari infinite loop chalavi       winning if ma break kari devay.
                2. guess again ne kadhi     first vakhatano input   e  while loop ma lavi ne     continue statement vapari shakay. 
                3. aama bhale dry principle vaparavano kidho che pan aapada code pramane aapade na vapari shakie kaaran else statement juo.   '''


52. step argument in range function : 

  '''  for i in range (1,11,2):
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
                  -10        '''


53. for loop and string :

'''    old (badhi laguage ma work kare):  
                 name = "karan"
                 for i in range (len(name)):
                     print(name[i])
                
                 output : k
                          a
                          r
                          a
                          n

        new (only for python laguage) : 
                   name = "karan"
                   for i in name: 
                     print(i)


                output : k
                          a
                          r
                          a
                          n




                          
                          name = input("enter a number : ").strip()
                          total = 0
                          for i in name :
                              total += int(i) 
                          print(total)

                          output = saravalo  '''


54.  function into :   (important)
   '''   name  = "karan"
         print(len(name))  
         
         aama len  e function che j python developer e pelethi aapyu chu .
         function no use e varam var code nalakhavo pade e mate thay che .
         ahi koi pan string ni lenth janava mate aapade len function no use karie chie.  
         
         
         
         potana function define karo :  function aapada mate kai pan work kari shke.

                               #  evu function j 2 number no saravalo kare.

                               def name_func(a,b) :          # def function define karava mate , name_func e fuction nu name che te tame kai pan rakhi shako ex, karan()       ,   name_func ( a, b ) : a and b e be peramiter che etle be input lese je 2 kimmat le int k string . 
                                  return a + b                # return ma function a and b ni saravalo mokalase  pan tame print karo to print Pan thay pan  mote bhage tamare funcion ma return j aapavu   jo tamare print karavavu j na hoy pan kimmat levi hoy to return levu pade.

                              # use:

                              name_func(5,4)   output = nothing 
                              print(name_func(5,4))   output = 9
                              total = name_func(5,4)
                              print(total)     
                              
                              
                              # 
                                 num1 = int(input("enter first number : ))
                                 num2 = int(input("enter second number  : ))
                                 total = name_func (num1,num2)      
                                 
                                 
                              #   
                              # num1 = input("enter first number : )
                                 num2 = input("enter second number  : )
                                 total = name_func (num1,num2) 
                                 
                                 to aama string joint thay . 
                                 matalab peramiter ma   argument kai pan pass karay like floting number , string , intiger number ...

                                 
                               ''' 

55. return vs print

''' def add_three(a,b,c):
       return a+b+c

    add_three (5,5,5)

    output = nothing 



   # def add_three(a,b,c):
       print (a+b+c)

    add_three (5,5,5)

    output = 15
 
    pan return function mate vadhre saru che. aagal programming ma khabar padase. '''

56. function practice :

  '''       1. def karan(i) :
                  return i[-1]

                print(karan("karan"))  output = n
                print(karan(5))   out put = error!!

            2. def karan(i) : 
                  if i%2 == 0 :
                    return "even"
                  else : 
                    return "odd"

                    or

                def karan(i) : 
                  if i%2 == 0 :
                    return "even"
                  return "odd"

            3.  def karan (i) : 
                  if i%2 == 0 :
                    return True
                  else :
                    return False

                    or 

                def karan (i) : 
                  if i%2 == 0 :
                    return True
                  return False

                  or 

                def karan (i) : 
                  return i%2 == 0 

                
                print(karan(9))


                ahi  i  = peramiter   and 9 = argument 


            4.   def karan():
                   return "hiiii all"


                   aa evu function je koi input leto nathi.
                   jo return na badale print karo programm chalu karata j print thai jay.  '''


57. exercise

 '''  def grater(x,y) :
         if x > y :
           return x
         else :
           return y

      a = int(input("enter first number : "))
      b = int (input ("enter second number : "))
      print(greater(a,b))

              or

      def grater(x,y) :
         if x > y :
           return f"{x} is greater than {y}."
         else :
           return f"{y} is greater than {x}."

      a = int(input("enter first number : "))
      b = int (input ("enter second number : "))
      print(greater(a,b))   '''

58.  define greatest :
       
  '''  def greatest (a,b,c) :
          if a>b and a>c :
            return a
          elif b>a and b>c :
            return b
          else:
            return c 

       print(greatest(10,20,30))


              or 

    note : function ni andar function vapari shakay ex. 
        
        def greater (a,b):
          if a>b :
            return a
          return b
      
        def greatest (a,b,c) :
          bigger = greater(a,b)
          return greater(bigger,c)

               
                or


        def greatest (a,b,c) :
          return greater(greater(a,b),c)

       print(greatest(10,20,30))    '''

59. exercise :


'''  def is_pelindrome(z) :
         return z == z[::-1]

      name = input("enter your name : ").strip()
      print(is_pelindrome(name))
              
       
                 or 

    def is_pelindrome(z) :
          if name == name[::-1] :
             return True
          return False   ''' 

60. print method :

'''for i in range (10) :
  print(i)

output = 1
         2
         3...
         10

for i in range (10) :
  print(i,end = " ")

output = 1 2 3 4 ... 10

ahi " " ma je lakhavu hoy te lakhay . by default \n hoy che
  
  
#
    a = 0 
    b = 1
    print(a,b) 
    output = 0 1 
    
    '''

61. fibonacci series program :



# def phibonaki (n):
#     a = 0
#     b = 1
#     if n == 1 :
#         print(a)
#     elif n == 2:
#         print(a,b)
#     else :
       
#         print(a,b , end = " ")
#         for i in range (n-2) :
#             c = a + b
#             a = b 
#             b = c 
#             print(b , end  = " ")

# n = int(input ("enter a number : "))
# phibonaki(n)

62. default peramiter : 

# def user_info(first_name,last_name,age) :
#    print(f"your first name is {first_name}")
#    print(f'your last name is {last_name}')
#    print(f"your age is {age}")

# user_info('karan','patel',18)

# pan  1. age pass na karu to   error !!
#              def user_info(first_name,last_name,age = 23) :
#                   print(f"your first name is {first_name}")
#                   print(f'your last name is {last_name}')
#                   print(f"your age is {age}")

#                 user_info('karan','patel')
              
#         to have jo hu age pass na karu to by default age 23 aavase. and jo age 18 pass kare to 18 print thay.
#         pan jo None lakho to None print thay pan python ma none no means nothing thay zero nahi.

#     2. have jo last_name pan by default "unknown" thay to unknown print thay and age by default 23 print thay . 
#     3. pan jo only last_name j default hoy and age default na hoy to error aave . kaaran tame evu na kari shako k tame ek ne default banavo and bija badha ne  na banavo . tame jene default banavo teni pachi badhane default banavavva j pade . and ha only jo tame last valane by default banavo to chale.
#     4. and jo function ma verable like karan(a,b,c) karaine use karie to default print nathi thata enu solution shodhavanu che. 


63. variable scope : 

# def karan():
#   x = 7
#   return x

# def func():
#   print(x)

# func() 

# output: error kaaran k funcion no veriable function ma j kam kare and function purato j hoy.


# 2.

# def karan():
#   x = 7
#   return x

# print(x)

# output = error ,  aava functioin na variable ne local veriables kahevay. 



#3.
# x = 5     
# def karan():
#   x = 7
#   return x

# print(x)
# print(karan())

# output = 5
#          7   kaaran 5 valo x e global variable che.



#4.

# x = 5     
# def karan():
#   global x 
#   x = 7
#   return x

# print(karan())
# print(x)

#  output = 7
          # 7    kaaran k global variable ne badali didho che. 

#   pan  jo print (x)
#           print(karan())  hot to output = 5
#                                           7  aavat karan k fuction ma x badalay te pela  print thai jay che. 
#
#
#  pan aa na karay karan aama global variable ne badalo to difficulte thai jay badhu so .


64. intro to list 

''' list = ordered collection of items 
list ma int , float and string add kari shako


1.
numbers = [1,2,3,4]
print(numbers)

print(numbers[1])
ot = 2


2. 
words = ["word1",'word2','word3']
print(words)

print(words[:2])
ot = ['word1','word2']

3. 
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


4.
ls = [1,2,3,4,5,6,7,8,'nine']
print(ls)
ls[8:] = [9,10]
print(ls)

ot = [1, 2, 3, 4, 5, 6, 7, 8, 'nine']
     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] '''


65. add data in list :
'''  

1. append method =  1 j value ne add kari shake and chelle j add kare.
list1 = [1,2,3,4]
list1.append(5)
print(list1)
ot = [1,2,3,4,5]

2. insert method = 1 j value ne add kari shake and jya add karavi hoy tya kari sake.
list1 = [1,2,3,4]
list1.insert(1,'1.5')
print(list1)
ot = [1,1.5,2,3,4]

3. + vali     = aanathi 2 list  k vadhare joint thay 
list1 = [1,2,3,4]
list2 = [5,6,7,8]
lists = list1 + list2
print(lists)
ot = [1,2,3,4,5,6,7,8]

4. extend method = aanathi  2 list na aliment e 1 ma umeray  extend thay.
list1 = [1,2,3,4]
list2 = [5,6,7,8]
list1.extend(list2)
print(list1)
ot = [1,2,3,4,5,6,7,8]

list1 = [1,2,3,4]   = jo append vaparro to aliment na badale list extend thai jay.
list2 = [5,6,7,8]
list1.append(list2)
print(list1)
ot = [1, 2, 3, 4, [5, 6, 7, 8]]   '''

66. delete data from list :

''' 
1. pop method   = by default tane joi value pass na karao to last delete thai jay.
list1 = [1,2,3,4]
list1.pop()
print(list1)
ot = [1, 2, 3]

list1 = [1,2,3,4]
list1.pop(1)
print(list1)
ot = [1, 3, 4]

pan aa pop method e aliment ne delete kare ene store pan kare che.

list1 = [1,2,3,4]
deleted = list1.pop()
print(list1)
print(deleted)
ot = [1,2,3]
     4

2. delete operator  =  aa e kthi vadhare ne delete kare and position ssathe . slicing thi.
list1 = [1,2,3,4]
del list1[1]
print(list1)
ot = [1,3,4]

list1 = [1,2,3,4,5,6,7,8,9]
del list1[4:]
print(list1)
ot = [1, 2, 3, 4]

list1 = [1,2,3,4,5,6,7,8,9]
del list1[4:7]
print(list1)
ot = [1, 2, 3, 4, 8, 9]

3. remove method = tamane nahi khabar k elimtent kyache and pan delete karavo che. aama j lakho e delete thai jay.
list1 = [1,2,3,4]
list1.remove(1)
print(list1)
ot = [2,3,4]

list1 = [1,2,3,4,1]
list1.remove(1)
print(list1)
ot = [2,3,4,1] '''

67. in keyword with list :

'''
list1 = [1,2,3,4]
if 2 in fruits :
  print('present')
else :
  pritn('not present')

ot = present  '''

68. some more list method :
'''
1.  count method = aliment count karava mate 
list1 = [1,2,3,4,1,2]
ptint(list1.count(2))
ot = 2 

2. sort method  =  alimet ne alphabeticaly sort karava mate and integer ne numerical sort karava mate. 
                   pan jo badha sting or badha number hoy to j thay.

list2 = [5,4,2,3,1]
list2.sort()
print(list2)
ot = [1,2,3,4,5]

3. sorted function = aanathi list sort nathi karato pan sorted print kare che.
la = ['karan','neel','dhaval']
print(sorted(la))
print(la)
ot = ['dhaval', 'karan', 'neel']
     ['karan', 'neel', 'dhaval']

4. clear method = list ne empty kari de delete na kare delete kare to list pan delete thay empty kare.
names = ['dhaval', 'karan', 'neel']
names.clear()
print(names)
ot = []

5. copy method = list ni copy kare 
names = ['dhaval', 'karan', 'neel']
vijay_na_balako = names.copy()
print(vijay_na_balako)
ot = ['dhaval', 'karan', 'neel']  '''

69. compare list :  (is vs =)
'''
1. is vs == 

lis1 = [1,2,3,4]
lis2 = [1,2,3,4]
lis3 = [1,3,4]

print(lis1 == lis3)

print(lis1 is  lis3)

print(lis1 == lis2)

print(lis1 is lis2)

ot = False
     False
     True
     False    kaaran is e memory ma compare kare  jo memory ma be ni position same hoy to j true kare. '''

70 . join method and split method  : 
'''
1. split method 
user_info = 'karan 17'.split()
print(user_info)
ot = ['karan','17']

jo , thi todavo hoy to .split(',')

2. join method 
user_info = ['karan','17']
print(','.join(user_info))
karan,17                             joint kari ne list ne string ma convert kare.  '''

71. list vs array :

'''  
array = order collection of items
list = order collection of items (python)

c, c++ , java array =   ma ek j value store kari shkay either int or string
python list =  store any data (flexible)

python array module = fix data type  (but performance high)
python numpy arrays = binding c (flexibility python but performance c (high) )

javascipt array = python list (flexible) '''

72. list vs string :

'''
s = "string"
l = [1,2,3,4]

string are immutable  (badali na shako)
list are mutable  (badali shako)

'''

73. lopping in list : 

''' 
lis = [1,2,3,4]

# for loop
for i in lis :
  print(i) 

# while
lis = [1,2,3,4,5]
i = 0
while i < len(lis):
    print(lis[i])
    i += 1

'''

74. list inside list
'''
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

print(mtrix[1[1]])
ot = 5


2. type function

s = "karan"
print(type(s))
ot = string 

'''

75. more about list :
'''

1. generate lists with range functions

numbres = [1,2,3,4,5,6,7,8,9,10]
numbers1 = list(range(1,11))    #same

2. index method 
numbres = [1,2,3,4,5,6,7,8,9,10,1]
print(numbres.index(1))
ot = 0

numbres.index(su shodhavanu,kai podistion thi chalu karavanu,kya atakavanu)

# my function 

list1 = [1,2,3,4,5,1,6,9,8,1,2,5,6,9,4,1,5,6,9,1]
def count(i,j):
    l = 0
    for k in i :
            if k == j : 
               a =  i.index(j,l,len(i))
               print(a)
               l = a + 1
            
count(list1,1)
                
ot = 0
     5
     9
     15
     19


3. pass list to a function
list1 = [1,2,3,4,5,1,6,9,8,1,2,5,6,9,4,1,5,6,9,1]
def negative_list (i) :
  tv = []
  for i in list1 :
      tv.append(-i)
  return tv

print(negative_list(list1))

'''

76. exerecise 1 
''' 
def list_square (i):
    tv = []
    for j in i :
       tv.append(j**2)
    return tv

ls = [1,2,3,4,5,6,7,8,9]   or    ls = list(range(1,10))
print(list_square(ls))

ot = [1, 4, 9, 16, 25, 36, 49, 64, 81]

'''

77. exercise 2 
'''
ls = list(range(1,11))

def reversek (i):
    return i[::-1]
print(reversek(ls))

 
      or 



def reversek (i):
     i.reverse()
     return i`
print(reversek(ls))

 
         or 


def reversek (i):
    tv = []
    for j in range(len(i)) :
          
          tv.append(i.pop())
    return tv
print(reversek(ls))



ot = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
'''

78. exercise 3 
'''
def reverse_list_aliment (i):
     tv = []
     for j in i :
         tv.append(j[::-1])
     return tv

ls = ['karan','dhaval','neel','nikhil','anita','dinesh']
print(reverse_list_aliment(ls))

'''
79. exercise 4 
'''
def odd_even(i):
    odd = []
    even = []
    total = []
    for j in i :
        if j%2 == 0:
            even.append(j)
        else :
            odd.append(j)
    total.append(odd)
    total.append(even)
    return total
  

        or 

    total = [odd,even]
    return total
           
ls = list(range(1,25))
print(odd_even(ls))

''' 

80. exercise 5 
'''
def same(i,j):
    tv = []
    for k in i :
        if k in j:
            tv.append(k)
    return tv

ls = [1,2,3,4,5]
ls2 = [3,4,5,6,7,8,9]
print(same(ls,ls2))

ot = [3,4,5]
'''
81. min and max function :
'''
numbers = [10,50,30]
print(min(numbers))
ot = 10

print(max(numbers))
ot = 50

def greatest_difference(i):
    return max(i) - min (i)

ls = [10,5,6,7,8,9]
print(greatest_difference(ls))
ot = 5
'''

82. exercise 6 :
'''
def sub_list_check(i):
    total = 0
    for j in i :
        if type(j) == list :
            total += 1 
    return total
ls = [1,2,3,[3.1,3.2,3.3,3.4],4,5,6,[6.1,6.2,7,8,9]]
print(sub_list_check(ls))

ot = 2
'''


83. intro  to tuples
'''
tuple data structure     tup = ('one','two',3,4,5)
tuple pan list ni flexiable data store kari shake.
tuples are immutable,can't update   (no append ,no insert , no pop , no remove)
use = when we know that our data will not be change   ex.  week_days = ('monday','tuesday')
tuples  are faster than list
methods which we can use in tuples = count , index , len , slicing

tup = ('one','two',3,4,5)
print(tup[2])
ot = 3
'''

84. more about tuples:
'''
1. lopping in tuples 
ls = (1,2,3,4.0,'karan')
for i in ls:
  print(ls)

2. tuple with one element 
ls = (1)   wrong
ls2 = (1,)  right
print(ls)
print(ls2)

ot = int
     tuple

3. tuple without parenthesis
names = 'karan','neel','nikhil'    = tuple


4. tuple unpacking 
names = 'karan','neel','nikhil','mit'
name1,name2,name3,name4 = (names)
print(name3)

ot = nikhil

5. list inside tuples    =   tuple ni andar jo list hoy to data add and remove kari shakay.
num = (1,2,3,[3.1,3.2,3.3])
num[3].pop()
print(num)

ot = (1, 2, 3, [3.1, 3.2])

num[3].append(3.4)
print(num)

ot = (1, 2, 3, [3.1, 3.2, 3.4])

num[3].pop(0)
print(num)

ot = (1, 2, 3, [3.2, 3.4])

6. min() , max , sum
num = (1,2,3,[3.1,3.2,3.3])
print(min(num))

ot = error  to sub tuple k list na hovi joie

num = (1,2,3,4,5)
print(min(num),max(num),min(num)+max(num))

ot = 1 5 6

'''
85. function returning two values:
'''
def kar(i,j):
    s = i + j
    g = i * j
    return s,g

a = int(input("enter first number : "))
b = int(input('enter second number : '))
print(kar(a,b))

# ot = (30, 200)  jyare function eki sathe be value return karo to funciton tuple return kare.
solution = saravalo , gunakar = kar(a,b)    aam tene variable ma add kari devay
print(saravalo)
print(gunakar)

'''

86. tuple , list , string  more :
'''

num = tuple(range(1,11))
print(num)

ot = (1,2,3,4,5,6,7,8,9,10)


nums = list((1,2,3,4,5,6,7,8,9,10))
print(nums)

ot = [1,2,3,4,5,6,7,8,9,10]

nums = str((1,2,3,4,5,6,7,8,9,10))
print(nums)
print(type(nums))

ot = (1,2,3,4,5,6,7,8,9,10)
     string    because  in real '(1,2,3,4,5,6,7,8,9,10)'




#
my experiment :
name = input("enter your name : ")
age = int(input("enter your age : "))
user_info = (name,age)
print(user_info,type(user_info))

print(user_info)
change_name = input("if you want to change your name press y else press n : ")
if change_name == "y": 
    new_name = input("enter your name : ")
    user_info = list(user_info)
    user_info.remove(name)
    user_info.insert(0,new_name)
    user_info = tuple(user_info)
print(user_info,type(user_info))

ot = 
enter your name : karan
enter your age : 17
('karan', 17) <class 'tuple'>
if you want to change your name press y else press n : y
enter your name : neel
('neel', 17) <class 'tuple'>
#
'''

87.  intro to dictionaries :
''' 
 why we use dictionaries ? = because of limitation of lists , lists are not enough to present real data.
ex.
user = ['karan',17,[vijay flats,c/9]]
 
 this list contains user name , age and address
 you can do this but this is not a good way to do this.
 
 what are dictionaries = unordered collections of data in key : value pair.


 how to create dectionaries
1.
user = {'name' : 'karan' , 'age' : 17}
print(user_info,type(user_info))

ot = {'name': 'karan', 'age': 17} <class 'dict'>

2. 
user_info = {
    
             'name' : 'karan' , 
             'age' : 17
             
             }
print(user_info,type(user_info))

user_info1 = dict(
    name = 'karan' , 
    age = 17
    
    )
print(user_info1,type(user_info1))

ot = {'name': 'karan', 'age': 17} <class 'dict'>
     {'name': 'karan', 'age': 17} <class 'dict'>

 
 how to access data from dictionaries  

1.
user_info1 = dict(
    name = 'karan' , 
    age = 17
    
    )

print(user_info1[0])
ot = error      because dictionaries unorder collection of data che. dictionaries has no index.

so we take help of key.  ex. key = name ,age

print(user_info1['name'])
print(user_info1['age'])
ot = 'karan'
      17


 which type of data can we store in dictionary ?
  numbers, string , list , dictionari , anything like list

user_info = {
     
     'name' : 'karan',
     'age' : 17
     'fav_mocies' : ['force','pink'],
     'fav_tunes' : ['fairy tale'],


}
print(user_info)
print(user_info['name'])
print(user_info['fav_mocies'])
print(user_info['fav_tunes'])
print(user_info['age'])

ot = {'name': 'karan', 'age': 17, 'fav_mocies': ['force', 'pink'], 'fav_tunes': ['fairy tale']}
      karan
      ['force', 'pink']
      ['fairy tale']
      17


users = {
  'user1' : {


  
  }



}   aam dictionary ni andar dictionary pan store kari shakie chi and complex data ne pan store kari shakie chie.

  
  how to add data to empty dictionary

user_info2 = {}
user_info2['name'] = 'karan'
print(user_info2)
user_info2['age'] = 17
print(user_info2)

ot = {'name': 'karan'}
     {'name': 'karan' , 'age': 17}

'''

88. looping and in keyword in dictionary : 
'''
# if you want to check keys:


dic = dict(
    name = 'karan',
    age = 17
)

if 'name' in dic:
    print('present')
else :
    print('not present')

ot = present


# if you want to check values : 

dic = dict(
    name = 'karan',
    age = 17
)
# print(dic,type(dic))
if 17 in dic.values():
    print('present')
else :
    print('not present')

ot = present
jo if '17' in dic.values():  hoy to error


# loops in dictionari

1. keys print thay
dic = dict(
    name = 'karan',
    age = 17
)

for i in dic:
    print(i)

ot = name
     age

2. values print thay
for i in dic.values():
    pritn(i)
  
ot = karan
     17 


3. values method
dic = dict(
    name = 'karan',
    age = 17
)
user = dic.values()
print(user,type(user))

ot = dict_values(['karan', 17]) <class 'dict_values'>

4. keys method
dic = dict(
    name = 'karan',
    age = 17
)
user = dic.keys()
print(user,type(user))

ot = dict_keys(['name', 'age']) <class 'dict_keys'>

5. 

for i in dic:
    print(dic[i])

ot = karan
     17

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
''' 

89. add and delete data from dictionari:
'''
user = dict(

      name = 'karan',
      age = 17,
      gender = 'male',

)

1. add data : 
user['fav_song'] = song1
print(user)
  
ot = {'name': 'karan', 'age': 17, 'gender': 'male', 'fav_song': 'song1'}  

2. pop method : 
print(user.pop('fav_song'))
print(user)

ot = song1
     {'name': 'karan', 'age': 17, 'gender': 'male'}

aama pop method ma argument pass karavavi j pade list ni jem nachale.


3. popitem method 
print(user.popitem())
print(user)

ot = ('gender', 'male')
     {'name': 'karan', 'age': 17}

aanathi last key and value delete kari de.

'''


90. make virtual envirment for project


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


91. pickel (module)

""" it's like when you want to create file and save one thing for temperari and then retrive but pickel make it easy"""

# write pickle
with open("name.pkl","wb") as file_variable: #here .pkl not neccessery
  pickle.dump("value",file_variable) # here value can be any object

# read pickle
with open("name.pkl","rb") as file_variable:
  var = pickle.load(file_variable)

""" important Note: to delete pickle file after use can not be done in function/method"""


 