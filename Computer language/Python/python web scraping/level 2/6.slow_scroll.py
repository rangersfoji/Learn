from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from threading import Thread
from multiprocessing import Process



def search_query(bot,search):
        

        bot.get('https://www.google.com/')
        time.sleep(0.5)
        input_box = bot.find_element_by_name('q')
        input_box.clear()
        input_box.send_keys(search)
        input_box.send_keys(Keys.RETURN)

def scroll(bot):

        speed = 4
        j = 0
        k = speed
        for i in range(1000):
            bot.execute_script(f'window.scrollTo({j},{k})')
            j = k
            k += speed

def main(search):
    bot = webdriver.Chrome()
    time.sleep(3)
    t = Thread(target=search_query,args=[bot,search])
    t.start()
    time.sleep(0.5)
    t = Thread(target=scroll,args=[bot])
    t.start()
    
      
if __name__ == '__main__':
    
    search = 'python'
    main(search)

    while True:
        pass
    
    
        

