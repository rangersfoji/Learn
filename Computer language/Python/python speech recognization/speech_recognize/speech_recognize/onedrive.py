from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time


def main(tim):
		bot = webdriver.Edge()
		login(bot,'karandpatel321',tim)
		bot.close()
		exit()

def login(bot,username,tim): 
		bot.get(f'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1580794159&rver=7.3.6962.0&wp=MBI_SSL_SHARED&wreply=https:%2F%2Fonedrive.live.com%3Fgologin%3D1%26mkt%3Den-US&lc=1033&id=250206&cbcxt=sky&mkt=en-US&lw=1&fl=easi2&username={username}%40gmail.com')
		time.sleep(1)

		#page opened
		email = bot.find_element_by_name('passwd')
		email.clear()
		email.send_keys('K98Op49p$')
		email.send_keys(Keys.RETURN)
		
		j = tim
		for i in range(tim):
			print(j)
			time.sleep(1)
			j -= 1
    			
		bot.find_element_by_class_name('_14ggU2yZvNol5U91gfmYQA').click()

		time.sleep(2.5)
		bot.find_element_by_id('meControlSignoutLink').click()
		time.sleep(4)
		




    


