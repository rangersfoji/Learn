# ui
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QDialog,QMessageBox,QTreeWidgetItem,QPushButton
from PyQt5.QtCore import Qt ,QUrl
from PyQt5 import QtMultimedia
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import sys

from threading import Thread

from datetime import date
import datetime
import time
import os
 
# software
import mysql.connector
from datetime import date


'''
    HOW TO USE :
    - what if one day store closed or any hoiday after that , new day do countercash = 0
'''

'''
    WHAT NEED'S TO BE DONE :
    - set perfect budy (tab button to navigate second edit text)
    - check bug file
    - if scanned something and forget to submit and trying to close than show dialog
    - use background thread to do thing fast but join it before closing app
    - set data by changing date 

    --------------------------------
    - imporve performance
    - test in real store
    - buy fast server
    
'''
# database info 
A = "lotteryboydb.c65i8rqfjo7h.us-east-1.rds.amazonaws.com"
B = 3306
C = "lotteryboydb"
D = "K98Lp49p$K98Lp49p$"
E = "lotteryboydb"


COMMISSION = 5
CASHING_COMMISSION = 1
DATE = date.today()

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # change directory 
        path = None
        print('scanning for file...')
        for i , j , k in os.walk(os.getcwd()):
            if "lotteryboy_main.py" in k:
                path = i
                print('file found.')
                break
        print('scanning completed.')

        if path != None :
            os.chdir(path)

            # get databse info
            self.get_database_info()

            # initialize user interface

            self.ui = uic.loadUi('../ui/main.ui', self)
            self.show()

            # variables for display data
            self.no1 = 1
            self.no2 = 1

            # local databse
            self.active_db = []
            self.scan_db = []
            self.active_row_db = []
            self.scan_row_db = []

            # start software
            self.start_software()
        else : 
            print('file not found.')
            print('path :',path)


    def get_database_info(self):
        # conect to datebase
        self.db =  mysql.connector.connect(host=A,port=B,user=C,passwd=D,database=E)
        self.mycursor = self.db.cursor(buffered=True)

            
        # getting  'game number' from database and save in tuple 
        self.d_game_num = self.get_tuple_with_query("select game_number from lottery",1)
       
    def start_software(self):
        
        # add acitve book (scann)
        self.ui.active_scan.returnPressed.connect(self.add_scan)

        # add acitve book (manual)
        self.ui.active_bnum.returnPressed.connect(self.ui.active_addbtn.click)
        self.ui.active_addbtn.clicked.connect(self.add_manual)

        # add ticket (scan)
        self.ui.scan_scan.returnPressed.connect(self.add_scan_scan)

        # add ticket (manual)
        self.ui.scan_tnum.returnPressed.connect(self.ui.scan_addbtn.click)
        self.ui.scan_addbtn.clicked.connect(self.add_scan_manual)

        # add report 
        self.ui.report_351.returnPressed.connect(self.ui.report_subbtn.click)
        self.ui.report_subbtn.clicked.connect(self.send_report)


        # save active
        self.ui.active_subbtn.clicked.connect(self.active_save)

        # save scan
        self.ui.scan_subbtn.clicked.connect(self.scan_save)



    def add_scan(self):
    
        # set  obj , get text , clear input box
        text_obj = self.ui.active_scan
        text = text_obj.text()
        text_obj.clear()

        # check is inputs are int?
        approved = self.check_input(text)

        if approved:
            approved = False

            # check vaild scan
            try :
                l_game_num = int(text[-3] + text[2:4])
                l_book_num = int(text[4:10])
                approved = True
            except:
                approved = False
                self.error_dialog('Please Scan Again!!!')

           
            if approved:
    
                # check vaild game number
                if l_game_num in self.d_game_num:

                    ls = []

                    approved = True
                    try:
                        self.mycursor.execute(f'''select
                                        book_number
                                        from lottery as l 
                                        left join active_book as a
                                            using (game_id)
                                        where l.game_number = {l_game_num}''')
                        res = self.mycursor.fetchall()
                        for i in res:
                            ls.append(i[0])

                        if l_book_num in ls:
                            approved = False
                    except:
                        approved = None

                    if approved:

                        # check if already have?
                        approved = self.check_in_activedb(l_book_num)
                        
                        if approved:
                            # get name of game
                            l_game_name , l_game_id , l_game_tickets = self.get_tuple_with_query_fetchone(f'select name,game_id,total_ticket from lottery where game_number = {l_game_num}',3)  

                            # add into local database
                            self.active_db.append(tuple([l_game_id,l_game_num,l_book_num,l_game_name,l_game_tickets]))

                            # display active book info
                            self.display_active(l_game_num,l_book_num,l_game_name)
                        else:
                            # warning sound
                            self.play_sound('error.mp3')
                    elif approved == None:
                        self.error_dialog("Network Problem!!! Please Try Again.")
                        print('network problem')
                    else:
                        # error 
                        self.error_dialog('This Book Activated Before!!!')
                else :
                    if self.d_game_num == None:
                        print("none")
                    else:
                        print("Entered Game Number : ",l_game_num)
                        print("Game Numbers : ",self.d_game_num)
                    self.error_dialog('This Game Number Not Found!!! Scan Again.')

    def add_manual(self):
    
        # set  obj , get text , clear input box
        g_obj = self.ui.active_gnum
        b_obj = self.ui.active_bnum

        g_text = g_obj.text()
        b_text = b_obj.text()

        g_obj.clear()
        b_obj.clear()

        # check is inputs are int?
        approved = self.check_input(g_text,b_text)

        if approved:
            g_text = int(g_text)
            b_text = int(b_text)
            
            # check valid game number
            if g_text in self.d_game_num :

                # check if already have in database?
                ls = []

                approved = True
                try:
                    self.mycursor.execute(f'''select
                                    book_number
                                    from lottery as l 
                                    left join active_book as a
                                        using (game_id)
                                    where l.game_number = {g_text}''')
                    res = self.mycursor.fetchall()
                    for i in res:
                        ls.append(i[0])

                    if b_text in ls:
                        approved = False
                except:
                    approved = None

                if approved:

                    # check if already have?
                    approved = self.check_in_activedb(b_text)

                    if approved:
                        # sound
                        self.play_sound('add.mp3')

                        # get name of game 
                        n_text , g_id , g_tickets = self.get_tuple_with_query_fetchone(f'select name,game_id,total_ticket from lottery where game_number = {g_text}',3)

                        # add into local database
                        self.active_db.append(tuple([g_id,g_text,b_text,n_text,g_tickets]))

                        # display active books info
                        self.display_active(g_text,b_text,n_text)
                    else :
                        # warning sound
                        self.play_sound('error.mp3')
                elif approved == None:
                    self.error_dialog("Network Problem!!! Please Try Again.")
                    print('network problem')
                else:
                        # error 
                        self.error_dialog('This Book Activated Before!!!')
            else :
                if self.d_game_num == None:
                        print("none")
                else:
                        print("Entered Game Number : ",g_text)
                        print("Game Numbers : ",self.d_game_num)
                self.error_dialog('Invalid Game Number!!! Please Enter Again.')

    def add_scan_scan(self):
        
        # set  obj , get text , clear input box
        text_obj = self.ui.scan_scan
        text = text_obj.text()
        text_obj.clear()

        # check is inputs are int?
        approved = self.check_input(text)

        if approved:
            
            approved = False

            # check vaild scan
            try :
                game_num = int(text[:3])
                book_num = int(text[4:10])
                ticket_num = int(text[10:13])
                approved = True
            except:
                approved = False
                self.error_dialog('Please Scan Again!!!')

            if approved:

                # check book actived before?
                # approved = self.eliment_in_database('active_book','book_number',book_num)

                ls = []
                approved = False
                try:
                    self.mycursor.execute(f'''select
                                    book_number
                                    from lottery as l 
                                    left join active_book as a
                                        using (game_id)
                                    where l.game_number = {game_num}''')
                    res = self.mycursor.fetchall()
                    for i in res:
                        ls.append(i[0])

                    if book_num in ls:
                        approved = True
                except:
                    approved = None
               
                if approved:
    
                    # check if already have?
                    approved = self.check_in_scandb(book_num)

                    if approved:
                        approved = False
                        # get name of game
                        try:
                            
                            # find sold ticket
                            last_ticket = self.get_tuple_with_query_fetchone(f'select ticket_number from detail_report where book_number = {book_num}',1)[0]
                            sold_ticket = int(last_ticket) - ticket_num

                            # get game name
                            game_name = self.get_tuple_with_query_fetchone(f'select name from lottery where game_number = {game_num}',1)[0]
                                
                            approved = True
                        except:
                            approved = False
                            self.error_dialog('Something Is Wrong!! Please Scan Again!!')

                        if approved:
                            # add into local database
                            self.scan_db.append(tuple([ticket_num,book_num,sold_ticket]))

                            # display scaned ticket info
                            self.display_scan(game_num,ticket_num,game_name)
                    else:
                        # warning sound
                        self.play_sound('error.mp3')
                elif approved == None :
                    self.error_dialog("Network Problem!!! Please Try Again.")
                    print('network problem')
                else :
                    self.error_dialog('This Book Not Activated!!! Active First.')

    def add_scan_manual(self):
    
        # set  obj , get text , clear input box
        g_obj = self.ui.scan_gnum
        b_obj = self.ui.scan_bnum
        t_obj = self.ui.scan_tnum

        g_text = g_obj.text()
        b_text = b_obj.text()
        t_text = t_obj.text()

        g_obj.clear()
        b_obj.clear()
        t_obj.clear()

        # check is inputs are int?
        approved = self.check_input(g_text,b_text,t_text)

        if approved:
            g_text = int(g_text)
            b_text = int(b_text)
            t_text = int(t_text)


            # check valid game number
            if int(g_text) in self.d_game_num :

                # check book actived before?
                ls = []
                approved = False
                try:
                    self.mycursor.execute(f'''select
                                    book_number
                                    from lottery as l 
                                    left join active_book as a
                                        using (game_id)
                                    where l.game_number = {g_text}''')
                    res = self.mycursor.fetchall()
                    for i in res:
                        ls.append(i[0])

                    if b_text in ls:
                        approved = True
                except:
                    approved = None
                
                if approved:

                    # check if already have?
                    approved = self.check_in_scandb(b_text)

                    if approved:

                        # sound
                        self.play_sound('add.mp3')

                        # find sold ticket
                        last_ticket = self.get_tuple_with_query_fetchone(f'select ticket_number from detail_report where book_number = {b_text}',1)[0]
                        sold_ticket = int(last_ticket) - t_text     
                        
                        # get name of game 
                        n_text = self.get_tuple_with_query_fetchone(f'select name from lottery where game_number = {int(g_text)}',1)[0]

                        # add into local database
                        self.scan_db.append(tuple([t_text,b_text,sold_ticket]))
                        
                        # display active books info
                        self.display_scan(g_text,t_text,n_text)
                    else :
                        # warning sound
                        self.play_sound('error.mp3')
                elif approved == None:
                    self.error_dialog("Network Problem!!! Please Try Again.")
                    print('network problem')
                else:
                    self.error_dialog("This Book Is Not Activated Before!!! Please Acitvate First.")
            else :
                self.error_dialog('Invalid Game Number!!! Please Enter Again.')



    def active_save(self):
        if self.active_db != None:
            # get values
            values1 = []
            values2 = []
            for i in self.active_db:
                l1 = []
                l2 = []

                l1.append(i[0])
                l1.append(i[2])
                l1.append(DATE)

                l2.append(DATE.day)
                l2.append(i[2])
                l2.append(i[4]-1)
                l2.append(0)

                values1.append(tuple(l1))
                values2.append(tuple(l2))

            # active books method
            def active(values1,values2):

                try:
                    query = "insert into active_book(game_id,book_number,active_date,status) values(%s,%s,%s,'selling')"
                    self.mycursor.executemany(query,values1)
                except:
                    self.error_dialog('Network Problem!! Please Try Again.')

                
                query = 'insert into detail_report(day_no,book_number,ticket_number,sold_tickets) values(%s,%s,%s,%s)'
                self.mycursor.executemany(query,values2)
                self.db.commit()

            # book activated
            active(values1,values2)

            # dialog with sound
            self.submit_dialog('Books Are Activated.')

            # delete from local database 
            self.active_db.clear()

            # delete 'delete buttons'
            for i in self.active_row_db:
                try:
                    self.active_main.removeItemWidget(i,4)
                except:
                    print(i)
                
            # empty local database
            self.active_row_db.clear()
        else :
            self.warning_dialog("Please Enter New Data!!!")
                
    def scan_save(self):

        # set sold books
        self.sold_books()

        if self.scan_db != None:
            day = DATE.day
            month = DATE.month
            year = DATE.year

            instant_suppose_to_be = 0
            for i in self.scan_db:
                game_id = self.get_tuple_with_query_fetchone(f'Select game_id from active_book where book_number = "{i[1]}"',1)[0]
                amount = self.get_tuple_with_query_fetchone(f"select amount$ from lottery where game_id = '{game_id}' ",1)[0]
                instant_suppose_to_be += (amount * i[2])

                # detail report update
                self.insert_detail(day,i[1],i[0],i[2])


            # if try worked means this day's raw inserted
            try :
                before_draw_sale,before_lottery_sold,before_lottery_cashing,before_instant_sold,before_suppose,before_profit = self.get_tuple_with_query_fetchone(f'select draw_sale,lottery_sold,lottery_cashing,instant_sold,instant_suppose_to_be,profit from daily_detail_report where date = "{DATE}" ',6)
                
                # if report not saved yet
                if before_draw_sale == 0 and before_lottery_cashing == 0 and before_instant_sold == 0 :
                    draw_sale = before_draw_sale
                    lottery_cashing = before_lottery_cashing
                    instant_sold = before_instant_sold

                    new_instant_suppose = before_suppose + instant_suppose_to_be
                    lottery_sold = new_instant_suppose # because report haven't saved so 
                    difference = instant_sold - new_instant_suppose 
                    profit = (lottery_sold * COMMISSION)/100
                # else report is saved before
                else :
                    draw_sale = before_draw_sale
                    lottery_cashing = before_lottery_cashing
                    instant_sold = before_instant_sold

                    new_instant_suppose = before_suppose + instant_suppose_to_be
                    lottery_sold = before_lottery_sold + instant_suppose_to_be
                    difference = instant_sold - new_instant_suppose
                    profit = ( (lottery_sold * COMMISSION)/100 ) + ( (lottery_cashing * CASHING_COMMISSION)/100 )

            # except if row isn't inserted
            except :
                new_instant_suppose = instant_suppose_to_be
                draw_sale = 0
                lottery_cashing = 0
                instant_sold = 0
                lottery_sold = instant_suppose_to_be
                difference = instant_sold - instant_suppose_to_be
                profit = (instant_suppose_to_be * COMMISSION)/100
                



            # daily detail report add
            self.save_database(year,month,day,DATE,draw_sale,lottery_sold,lottery_cashing,COMMISSION,instant_sold,new_instant_suppose,difference,profit,"scan")
            
            # dialog with sound
            self.submit_dialog('Tickets have been saved.')

            # delete from local database 
            self.scan_db.clear()

            # delete 'delete buttons'
            for i in self.scan_row_db:
                try:
                    self.scan_main.removeItemWidget(i,4)
                except:
                    print(i)
                
            # empty local database
            self.scan_row_db.clear()
        else :
            self.warning_dialog("Please Enter New Data!!!")

    def send_report(self):
        
        # set  obj , get text , clear input box
        r_501_obj = self.ui.report_501
        r_502_obj = self.ui.report_502
        r_511_obj = self.ui.report_511
        r_512_obj = self.ui.report_512
        r_341_obj = self.ui.report_341
        r_351_obj = self.ui.report_351

        r_lottery_obj = self.ui.r_lottery_cash
        r_total_obj = self.ui.r_total_cash
        r_other_obj = self.ui.r_other_cash

        

        r_501_text = r_501_obj.text()
        r_502_text = r_502_obj.text()
        r_511_text = r_511_obj.text()
        r_512_text = r_512_obj.text()
        r_341_text = r_341_obj.text()
        r_351_text = r_351_obj.text()

        r_lottery_text = r_lottery_obj.text()
        r_total_text = r_total_obj.text()
        r_other_text = r_other_obj.text()
        
     

        # check is inputs are float?
        approved = self.check_input(r_501_text,r_502_text,r_511_text,r_512_text,r_341_text,r_351_text,r_lottery_text,r_total_text,r_other_text)


        if approved:
            r_501 = float(r_501_text)
            r_502 = float(r_502_text)
            
            r_511 = float(r_511_text)
            r_512 = float(r_512_text)
            r_341 = float(r_341_text)
            r_351 = float(r_351_text)
            r_counter_cash = None
            
            mode = None
            try :
                r_lottery = float(r_lottery_text)
                r_counter_cash = r_lottery
                mode = 1
            except:
                mode = 2
            try:
                r_total = float(r_total_text)
                r_other = float(r_other_text)
                r_counter_cash = r_total - r_other
                mode = 2
            except:
                mode = 1


            if mode == None:
                self.warning_dialog('You can use either separated cash mode or combined cash mode!!!')
            else:
                # not scan means sold
                # save info in databse
                dat = DATE
                
                year = dat.year
                month = dat.month
                day = dat.day  

                yesterday = dat - datetime.timedelta(days=1)
                if r_512 == 0 and r_351 == 0 and r_511 == 0 :
                    instant_sold = r_counter_cash - r_501 + r_502 + r_341
                else :
                    try :
                        db_totalcashing , db_drawsale = self.get_tuple_with_query(f"select lottery_cashing , draw_sale from daily_detail_report where date = '{yesterday}' ",2)
                    except : 
                        db_totalcashing = 0 
                        db_drawsale = 0
                    instant_sold = r_counter_cash - r_501 + r_502 + r_341 - (((r_512+r_351)-(db_totalcashing))-(r_511-db_drawsale))

                # if worked means row inserted
                try:
                    before_instant_suppose = self.get_tuple_with_query_fetchone(f'select instant_suppose_to_be from daily_detail_report where date = "{dat}" ',1)[0]
                    new_instant_suppose = before_instant_suppose
                    draw_sale = r_501
                    lottery_cashing = r_502 + r_341

                    if before_instant_suppose == 0 :
                        lottery_sold = draw_sale
                        difference = instant_sold
                        daily_profit = ( (lottery_sold * COMMISSION)/100 ) + ( (lottery_cashing * CASHING_COMMISSION)/100 )
                    else : 
                        lottery_sold = draw_sale + before_instant_suppose
                        difference = instant_sold - before_instant_suppose
                        daily_profit= ( (lottery_sold * COMMISSION)/100 ) + ( (lottery_cashing * CASHING_COMMISSION)/100 )
                # except if row isn't inseted
                except:   
                    lottery_cashing = r_502 + r_341
                    draw_sale = r_501
                    new_instant_suppose = 0 

                    lottery_sold = draw_sale - new_instant_suppose
                    difference = instant_sold
                    daily_profit = ( (lottery_sold * COMMISSION)/100 ) + ( (lottery_cashing * CASHING_COMMISSION)/100 )
                
                self.save_database(year,month,day,dat,draw_sale,lottery_sold,lottery_cashing,COMMISSION,instant_sold,new_instant_suppose,difference,daily_profit,"report")
               
                self.submit_dialog("Report Saved.")
                print('report saved')
                
    def sold_books(self):
        for i in self.scan_db:
                where_Sentence = "where book_number = " + str(i[1])
                if self.eliment_in_database("active_book","status","sold",where_Sentence):
                    self.mycursor.execute("UPDATE active_book SET status = 'selling' ")
                    self.db.commit()

        selling_books = list(self.get_tuple_with_query("select book_number from active_book where status = 'selling'",1))
        sold_books_book_number = selling_books.copy()

        for data in self.scan_db:
            # book_number = data[1]
            # ticket_Number = data[0]
            # sold_tickets = data[2]
            if data[1] in selling_books:
                    sold_books_book_number.remove(data[1])

        
        if not(sold_books_book_number == None):
            for i in sold_books_book_number:
                self.mycursor.execute(f'update active_book set status="sold" where book_number = {i}')
                self.db.commit()

                last_ticket = self.get_tuple_with_query_fetchone(f'select ticket_number from detail_report where book_number = {i}',1)[0]
                ticket_num = -1
                sold_ticket = last_ticket + 1
                book_number = i

                # add into local database
                self.scan_db.append(tuple([ticket_num,book_number,sold_ticket]))



    def error_dialog(self,sentence):
        # sound
        self.play_sound('error.mp3')


        mydg = QMessageBox()
        mydg.setWindowTitle('Error!!!')
        mydg.setWindowIcon(QIcon('../images/close.png'))
        mydg.setText(str(sentence))
        mydg.setIcon(QMessageBox.Critical)

        exitt = mydg.exec_()

    def warning_dialog(self,sentence):
        # sound
        self.play_sound('warning.mp3')


        mydg = QMessageBox()
        mydg.setWindowTitle('Warning!!!')
        mydg.setWindowIcon(QIcon('../images/warning_icon.png'))
        mydg.setText(str(sentence))
        mydg.setIcon(QMessageBox.Warning)

        exitt = mydg.exec_()

    def submit_dialog(self,sentence):
        # sound
        self.play_sound('submit.mp3')

        mydg = QMessageBox()
        mydg.setWindowTitle('Submited')
        mydg.setWindowIcon(QIcon('../images/submit.png'))
        mydg.setText(str(sentence))
        mydg.setIcon(QMessageBox.Information)

        exitt = mydg.exec_()

    def play_sound(self,sound_name):
        # sound
        self.music = QUrl.fromLocalFile(f'../sounds/{sound_name}')
        self.content = QtMultimedia.QMediaContent(self.music)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(self.content)
        # play sound
        self.player.play()



    def display_active(self,game_num,book_num,name):
        self.active_main = self.ui.active_dis
        row = QTreeWidgetItem(self.active_main)

        # add in local database
        self.active_row_db.append(row)

        # display 
        row.setText(0,str(self.no1))
        row.setText(1,str(game_num))
        row.setText(2,str(book_num))
        row.setText(3,str(name))

        btn = QPushButton('')
        btn.setIcon(QIcon('../images/delete.png'))
        self.active_main.setItemWidget(row,4,btn)

        # delete button clicked method
        def delete(clue):
            for i in self.active_db:
                if clue in i:
                    self.active_db.remove(i)
    

        def delete_local_info():
            # sound 
            self.play_sound('delete.mp3')


            # on display
            row.setText(1,'')
            row.setText(2,'')
            row.setText(3,'')
            self.active_main.removeItemWidget(row,4)

          
            # delte from local databse
            delete(book_num)
            
            

        btn.clicked.connect(delete_local_info)

        self.no1 += 1

    def display_scan(self,game_num,ticket_num,name):
        self.scan_main = self.ui.scan_dis
        row = QTreeWidgetItem(self.scan_main)

        # add in local database
        self.scan_row_db.append(row)

        # display  
        row.setText(0,str(self.no2))
        row.setText(1,str(game_num))
        row.setText(2,str(ticket_num))
        row.setText(3,str(name))

        btn = QPushButton('')
        btn.setIcon(QIcon('../images/delete.png'))
        self.scan_main.setItemWidget(row,4,btn)

        # delete button clicked method
        def delete(clue):
            for i in self.scan_db:
                if clue in i:
                    self.scan_db.remove(i)
    

        def delete_local_info():
            # sound 
            self.play_sound('delete.mp3')

            
            # on display
            row.setText(1,'')
            row.setText(2,'')
            row.setText(3,'')
            self.scan_main.removeItemWidget(row,4)

           
            # delte from local databse
            delete(ticket_num)
          
            

        btn.clicked.connect(delete_local_info)

        self.no2 += 1
    

    # get query and return tuple values function
    def get_tuple_with_query(self,query,number_of_getting_value):
        self.mycursor.execute(query)
        res = self.mycursor.fetchall()
        ls = []
        for i in res:
            for j in range(number_of_getting_value):
                ls.append(i[j])
        return tuple(ls)

    def get_tuple_with_query_fetchone(self,query,number_of_getting_value):
        self.mycursor.execute(query)
        res = self.mycursor.fetchall()
        ls = []
        for i in res:
            for j in range(number_of_getting_value):
                ls.append(i[j])
        return tuple(ls)



    def check_in_activedb(self,value):
        a = True
        for i in self.active_db:
            if value in i:
                a = False
                break
        return a   

    def check_in_scandb(self,value):
        a = True
        for i in self.scan_db:
            if value in i:
                a = False
                break
        return a

    def eliment_in_database(self,table_name,eliment_title,check_value,where_sentence = None):
        if where_sentence == None:
            self.mycursor.execute(f'select {eliment_title} from {table_name}')
            res = self.mycursor.fetchall()
            check = []
            for i in res:
                check.append(i[0])
        
            check = tuple(check)
            
            try :
                if (int(check_value) in check) :
                    return True
                else :
                    return False
            except :
                if (check_value in check):
                    return True
                else :
                    return False
        else :
            self.mycursor.execute(f'select {eliment_title} from {table_name} {where_sentence}')
            res = self.mycursor.fetchall()
            check = []
            for i in res:
                check.append(i[0])
        
            check = tuple(check)
            

            try :
                if (int(check_value) in check) :
                    return True
                else :
                    return False
            except :
                if (check_value in check):
                    return True
                else :
                    return False
    

    def check_input(self,text1 ,text2 = None,text3 = None,text4 = None ,text5 = None,text6 = None,text7 = None,text8 = None,text9 = None):
        # check is input String or show dialog

        if text2 == None  :
            try:
                int(text1)
                return True
            except:
                if text1:
                    self.warning_dialog('Only Numbers Are Accepted!!!')
                    return False
                else :
                    self.warning_dialog('you can\'t keep  empty box!!!')
                    return False

        elif text2 != None and text3 == None:
            try:
                int(text1)
                int(text2)
                return True
            except:
                if text1 and text2:
                    self.warning_dialog('Only Numbers Are Accepted!!!')
                    return False
                else :
                    self.warning_dialog('you can\'t keep  empty box!!!')
                    return False

        elif text3 != None and text4 == None:
            try:
                int(text1)
                int(text2)
                int(text3)
                return True
            except:
                if text1 and text2 and text3 :
                    self.warning_dialog('Only Numbers Are Accepted!!!')
                    return False
                else :
                    self.warning_dialog('you can\'t keep  empty box!!!')
                    return False

        elif text9 != None:
            try:
                float(text1)
                float(text2)
                float(text3)
                float(text4)
                float(text5)
                float(text6)
                float(text7)
                return True
            except:
                try:
                    float(text1)
                    float(text2)
                    float(text3)
                    float(text4)
                    float(text5)
                    float(text6)
                    float(text8)
                    float(text9)
                    return True
                except:
                    if (text1 and text2 and text3 and text4 and text5 and text6 and text7) or (text1 and text2 and text3 and text4 and text5 and text6 and text8 and text9) :
                        self.warning_dialog('Only Numbers Are Accepted!!!')
                        return False
                    else :
                        self.warning_dialog('you can\'t keep  empty box!!!')
                    return False



    # save database

    def save_database(self,year,month,day,date,draw_sale,lottery_sold,lottery_cashing,commision,instant_sold,instant_suppose_to_be_UPDATEONLY,difference_NotForUpdate,day_profit,mode):
            try :
                self.insert_year(self.mycursor,self.db,year,month,day,date,draw_sale,lottery_sold,lottery_cashing,commision,instant_sold,instant_suppose_to_be_UPDATEONLY,difference_NotForUpdate,day_profit,mode)
            except : 
                print('failed save_database')

    def insert_year(self,mycursor,mydb,year,month,day,dat,draw_sale,lottery_sold,lottery_cashing,commision,instant_sold,instant_suppose_to_be_UPDATEONLY,difference,day_profit,mode):
        year = int(year)
        profit = float(day_profit)
        if self.eliment_in_database("yearly_detail_report","year_no",year):
            # at last we will update year profit
            pass
        else : 
            self.mycursor.execute(f"INSERT INTO yearly_detail_report(year_no,profit) VALUES({year},{profit}) ")
            self.db.commit()
            print(f'{year} year inserted')
        
        self.insert_month(mycursor,mydb,month,year,day,dat,draw_sale,lottery_sold,lottery_cashing,commision,instant_sold,instant_suppose_to_be_UPDATEONLY,difference,day_profit,mode)

    def insert_month(self,mycursor,mydb,month,year,day,dat,draw_sale,lottery_sold,lottery_cashing,commision,instant_sold,instant_suppose_to_be,difference_NotForUpdate,day_profit,mode):
        month = int(month)
        profit = float(day_profit)
        where_sentence = "where year_no = " + str(year)
        if self.eliment_in_database("monthly_detail_report","month_no",month,where_sentence):
            # at last we will update month profit
            pass
        else : 
            mycursor.execute(f"INSERT INTO monthly_detail_report(month_no,year_no,profit) VALUES({month},{year},{profit})")
            mydb.commit()
            print(f'{month} is inseted in {year} ')

        self.insert_day(mycursor,mydb,day,month,year,dat,draw_sale,lottery_sold,lottery_cashing,commision,instant_sold,instant_suppose_to_be,difference_NotForUpdate,day_profit,mode)

    def insert_day(self,mycursor,mydb,day,month,year,dat,draw_sale,lottery_sold,lottery_cashing,commision,instant_sold,instant_suppose_to_be,difference,profit,mode):
            day = int(day)
            lottery_sold = float(lottery_sold)
            lottery_cashing = float(lottery_cashing)
            commision = float(commision)
            instant_sold = float(instant_sold)
            draw_sale = float(draw_sale)
            instant_suppose_to_be = float(instant_suppose_to_be)
            difference = float(difference)
            profit = float(profit)
            where_sentence = "where year_no = " + str(year) + " AND month_no = " + str(month)

            if self.eliment_in_database("daily_detail_report","day_no",day,where_sentence):
                mycursor.execute(f"UPDATE daily_detail_report SET draw_sale = {draw_sale},lottery_sold = {lottery_sold},lottery_cashing = {lottery_cashing},instant_sold = {instant_sold},instant_suppose_to_be = {instant_suppose_to_be},difference = {difference},profit={profit}")
                mydb.commit()
            else :
                mycursor.execute(f"""INSERT INTO daily_detail_report(day_no,
                                                                    month_no,
                                                                    year_no,
                                                                    date,
                                                                    draw_sale,
                                                                    lottery_sold,
                                                                    lottery_cashing,
                                                                    commission,
                                                                    instant_sold,
                                                                    instant_suppose_to_be,
                                                                    difference,
                                                                    profit) 
                                                                    VALUES({day},
                                                                            {month},
                                                                            {year},
                                                                            %s,
                                                                            {draw_sale},
                                                                            {lottery_sold},
                                                                            {lottery_cashing},
                                                                            {commision},
                                                                            {instant_sold},
                                                                            {instant_suppose_to_be},
                                                                            {difference},
                                                                            {profit})""",
                                                                            (dat,))
                mydb.commit()
                print(f'{day} is inseted in {month}/{year} ')

            # update month profit
            month_profit = sum(self.get_tuple_with_query_fetchone(f'select profit from daily_detail_report where month_no = {month} and year_no = {year}',1))
            self.mycursor.execute(f"UPDATE monthly_detail_report set profit = {month_profit}")
            self.db.commit()

            year_profit = sum(self.get_tuple_with_query_fetchone(f'select profit from monthly_detail_report where year_no = {year}',1))
            self.mycursor.execute(f"UPDATE yearly_detail_report set profit = {year_profit}")
            self.db.commit()

            # update year profit
       
        
    def insert_detail(self,day_no,book_number,ticket_number,sold_tickets):
        day_no = int(day_no)
        book_number = int(book_number)
        ticket_number = int(ticket_number)
        sold_tickets = int(sold_tickets)

        try:
            if self.eliment_in_database("detail_report","book_number",book_number):
                check_day , before_soldticket = self.get_tuple_with_query_fetchone(f'select day_no,sold_tickets from detail_report where book_number = {book_number}',2)
                if check_day == day_no:
                    new_soldticket = before_soldticket + sold_tickets
                    self.mycursor.execute(f"UPDATE detail_report SET ticket_number = {ticket_number} ,sold_tickets = {new_soldticket} WHERE book_number = {book_number}")
                    self.db.commit()
                else :
                    self.mycursor.execute(f"UPDATE detail_report SET ticket_number = {ticket_number} ,sold_tickets = {sold_tickets} WHERE book_number = {book_number}")
                    self.db.commit()
            else :
                self.mycursor.execute(f"INSERT INTO detail_report(day_no,book_number,ticket_number,sold_tickets) VALUES({day_no},{book_number},{ticket_number},{sold_tickets}")
                self.db.commit()
        except:
            print('Please check you network connection!!! ')


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())