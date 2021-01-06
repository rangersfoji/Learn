from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
import requests
import time
import csv
import keyboard
import os

class Onedrive:
    def __init__(self):
        self.bot = webdriver.Firefox()
		
        self.login('karandpatel321')

    def login(self,username):
        bot = self.bot
        bot.get(f'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1580794159&rver=7.3.6962.0&wp=MBI_SSL_SHARED&wreply=https:%2F%2Fonedrive.live.com%3Fgologin%3D1%26mkt%3Den-US&lc=1033&id=250206&cbcxt=sky&mkt=en-US&lw=1&fl=easi2&username={username}%40gmail.com')
        time.sleep(1)

        #page opened
        # for login
        email = bot.find_element_by_name('passwd')
        email.clear()
        email.send_keys('K98Op49p$')
        email.send_keys(Keys.RETURN)
        
        time.sleep(4)
        # content = bot.page_source  
     
        # soup = BeautifulSoup(content,'lxml')
        # for i in soup.findAll('span',class_ = 'ms-Tile-name name_6ecfd39b'):
        #     print(i['id'])
        #     print(i.span.span.text)
        #     print()
        #     print()


        # enter into folder which you want to downlaod
        bot.get('https://onedrive.live.com/?id=FAFC1D647E52CCAD%21207&cid=FAFC1D647E52CCAD')
        time.sleep(3)
        bot.find_element_by_name('Download').click()
        time.sleep(3.5)
        keyboard.press('down')
        keyboard.release('down')
        time.sleep(0.5)
        keyboard.press('enter')
        keyboard.release('enter')
       


        # after download logout

        time.sleep(20)
        bot.find_element_by_class_name('_14ggU2yZvNol5U91gfmYQA').click()

        time.sleep(1)
        sign_out = bot.find_element_by_id('meControlSignoutLink').click()
        time.sleep(2)
        keyboard.press('alt + F4')
        keyboard.release('alt + F4')



        # move downloaded file into desktop
        before = os.getcwdb().decode('utf-8')
        os.startfile(r'C:\Users\Karan\Downloads')
        time.sleep(1)
        keyboard.press('down')
        keyboard.release('down')
        keyboard.press('up')
        keyboard.release('up')


        keyboard.press('ctrl + x')
        keyboard.release('ctrl + x')

        time.sleep(0.2)
        keyboard.press('alt + F4')
        keyboard.release('alt + F4')
        os.startfile(r'C:\Users\Karan\Desktop')
        time.sleep(0.2)
        keyboard.press('ctrl + v')
        keyboard.release('ctrl + v')
        time.sleep(0.3)
        keyboard.press('alt + F4')
        keyboard.release('alt + F4')

        os.chdir(before)

        # close program
        exit()

   

		

ed = Onedrive()







