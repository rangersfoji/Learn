from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
import requests
import time

class Onedrive:
	def __init__(self):
		self.bot = webdriver.Firefox()
		
		self.login('rangersfoji1')

	def login(self,username):
		bot = self.bot
		bot.get(f'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1580794159&rver=7.3.6962.0&wp=MBI_SSL_SHARED&wreply=https:%2F%2Fonedrive.live.com%3Fgologin%3D1%26mkt%3Den-US&lc=1033&id=250206&cbcxt=sky&mkt=en-US&lw=1&fl=easi2&username={username}%40gmail.com')
		time.sleep(1)

		#page opened
		email = bot.find_element_by_name('passwd')
		email.clear()
		email.send_keys('K98Op49p$')
		email.send_keys(Keys.RETURN)
		
		# time.sleep(3)
		# bot.find_element_by_class_name('_14ggU2yZvNol5U91gfmYQA').click()

		# time.sleep(1)
		# sign_out = bot.find_element_by_id('meControlSignoutLink').click()

		# this will work only for 'rangersfoji1@gmail.com' because link is its
		time.sleep(2)
		bot.get('https://onedrive.live.com/?id=44FF3EB4BA14D1A6%21104&cid=44FF3EB4BA14D1A6')
		
		source = requests.get('https://onedrive.live.com/?id=44FF3EB4BA14D1A6%21104&cid=44FF3EB4BA14D1A6').text

		soup = BeautifulSoup(source,'lxml')

		link = soup.find('img',class_='od-ImageTile-image')

		csv_file = open('test_html.txt','w') # worked (if you downloaded this file then create test_html.txt file where this file is exists )
		csv_file.write(soup.prettify())
		csv_file.close()


ed = Onedrive()



