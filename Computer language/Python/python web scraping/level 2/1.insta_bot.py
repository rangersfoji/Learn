# pip install selenium
# install firefox webdriver and move it in python folder(main)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time

class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
        self.driver = webdriver.Firefox()  
        self.login()

    def login(self):
        bot = self.driver

        bot.get('https://twitter.com/login')
        time.sleep(1)
        email = bot.find_element_by_name("session[username_or_email]")
        email.clear()
        email.send_keys(self.username)

    
        password = bot.find_element_by_name('session[password]')
        password.clear()
 
        password.send_keys(self.password)
        time.sleep(0.5)
        password.send_keys(Keys.RETURN)

    def search(self,search_string):
        time.sleep(0.5)
        bot = self.driver

        bot.get('https://twitter.com/search?q=' + search_string + '&src=typed_query')
        time.sleep(2)

    def like_tweets(self):
        bot = self.driver

        # bot.execute_script('window.scrollTo(0,document.body.scrollHeight)') this is java script and this do scroll down one time

        # but we want more time so ,loop

        for i in range(1):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(4)

        # now here we will find all of tweets, it's use ful like in onedrive document
        # (important)
       
        # to find all of that  here we use find 'elements' insted of element
        # it returns list

        # here find with tag name(here anker tag : 'a')
        tweets = bot.find_elements_by_tag_name('a')
        
        # here not anker tag's text but from it's attribute data 
        links = [i.get_attribute('href') for i in tweets]

        # every link has 'a' tag but out tweet has 'status' word in link , so filter it
        links = [i for i  in links if 'status' in i]

        # remove duplicate links (check out the method)
        links = self.remove_dupplicate_link(links)

        # now start open and like every single tweet
        bot.get(links[0])
        for i in links:
            bot.get(i)
            
            # like is not working because of element not found (fix that)
            try:
                time.sleep(2)
                like = bot.find_element_by_xpath("//path[contains(@d,'M12 21.638h-.014C9.403 21.59 1.95 14.856 1.95 8.478c0-3.064 2.525-5.754 5.403-5.754 2.29 0 3.83 1.58 4.646 2.73.814-1.148 2.354-2.73 4.645-2.73 2.88 0 5.404 2.69 5.404 5.755 0 6.376-7.454 13.11-10.037 13.157H12zM7.354 4.225c-2.08 0-3.903 1.988-3.903 4.255 0 5.74 7.034 11.596 8.55 11.658 1.518-.062 8.55-5.917 8.55-11.658 0-2.267-1.823-4.255-3.903-4.255-2.528 0-3.94 2.936-3.952 2.965-.23.562-1.156.562-1.387 0-.014-.03-1.425-2.965-3.954-2.965z')]").click()
            except:
                print('like did not work')
            time.sleep(3)

        bot.close()

    def remove_dupplicate_link(self,lis):
        ls = lis

        # get '/' all positions
        ck = []
        for i in ls:
            tem = []
            a = 0
            for j in range(1,7):
                b= i.find('/',a)
                tem.append(b)
                a = b + 1
            ck.append(tem)

        # check after status and number does it have '/'
        check = []
        for i in ck :
            if i[5] != -1:
                check.append(i[5])
            else:
                check.append(-1)

        # remove dupplicate values(links)
        newls = []
        j = 0
        for i in check:
            if i == -1:
                newls.append(ls[j])
            else :
                newls.append(ls[j][:i])
            j += 1
        newls = list(set(newls))
        newls.sort()

        return newls


if __name__ == '__main__':
    insta = InstaBot('7813506346','K98Tp49p$')
    insta.search('python programming')
    insta.like_tweets()


