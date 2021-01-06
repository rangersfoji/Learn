from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time


def google_search(search):

        a = search
        a = a.replace('  ',' ')
        search = a.replace(' ','+')


        link = f'https://www.google.com/search?source=hp&ei=SIpHXp-SLIm1ggee0prICg&q={search}&oq={search}&gs_l=psy-ab.3..0l10.1782.4246..4694...0.0..0.184.809.10j1......0....1..gws-wiz.......0i131j0i10.bJ7KfMMOEgg&ved=0ahUKEwif1rDu8dLnAhWJmuAKHR6pBqkQ4dUDCAc&uact=5'
        bot = webdriver.Edge()
        bot.get(link)
      
        source = requests.get(link).text

        soup = BeautifulSoup(source,'lxml')

        links = []

        link = soup.find('a')
        for i in soup.findAll('a'):
            if 'http' in i['href'] and '/url?q=' in i['href']:
                a = i['href']
                ls = a.split('?q=')
                a = ls[1]
                ls = a.split('&sa=')
                link = ls[0]
                if 'www.youtube.com' in link:
                    link = link.replace('%3D','=')
                    link = link.replace('%3F','?')
                    if link in links:
                        pass
                    else :
                        links.append(link)
                elif 'https://accounts.google.com/ServiceLogin%3Fcontinue=https://www.google.com/search%3Fsource' in link:
                    pass
                else:
                    if link in links:
                        pass
                    else:
                        links.append(link)


        for i in links:
            try:
                bot.get(i)
            
                time.sleep(1)
            except:
                time.sleep(1)

        bot.close()




