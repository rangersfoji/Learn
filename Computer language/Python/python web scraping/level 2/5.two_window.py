from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import system
import time

def login(bot):
    a , b  = system.getinfo()
    time.sleep(3)

    bot.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/div[2]/button').click()

    time.sleep(0.5)

    # here second window opens so below won't work :
    # aa = bot.find_element_by_xpath('//*[@id="email"]')
    # aa.clear()
    # aa.send_keys(a)


    # so you have to switch window
    # print(bot.window_handles) # shows howmany window are there

    main_window = bot.window_handles[0]
    pop_up_window = bot.window_handles[1]

    bot.switch_to_window(pop_up_window)

    time.sleep(0.2)
    aa = bot.find_element_by_xpath('//*[@id="email"]')
    aa.clear()
    aa.send_keys(a)
   

    bb = bot.find_element_by_xpath('//*[@id="pass"]')
    bb.clear()
    bb.send_keys(b)

    time.sleep(0.2)
    bb.send_keys(Keys.RETURN)
    time.sleep(1)

    bot.switch_to_window(main_window)

    time.sleep(3)
    # if email info come (enter)
    try:
        email = bot.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/form/div[3]/div[1]/div/div/input')
        email.send_keys('himynameiskaran@gamil.com')
        email.send_keys(Keys.ENTER)
    except:
        print('email info not worked')
    
    




def main():

    bot = webdriver.Firefox()


    bot.get('https://tinder.com/')
    
    login(bot)

main()
