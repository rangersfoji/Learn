from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard

bot = webdriver.Chrome()
bot.get('https://www.instagram.com/accounts/login/')

time.sleep(2)
a = bot.find_element_by_name('username')
a.send_keys('username')
time.sleep(1)
# shift + f10  works like (right click)
a.send_keys(Keys.SHIFT , Keys.F10)



