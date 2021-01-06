from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time


def google_search(search):

        a = search
        a = a.replace('  ',' ')
        search = a.replace(' ','+')


        link = f'https://www.google.com/search?source=hp&ei=SIpHXp-SLIm1ggee0prICg&q={search}&oq={search}&gs_l=psy-ab.3..0l10.1782.4246..4694...0.0..0.184.809.10j1......0....1..gws-wiz.......0i131j0i10.bJ7KfMMOEgg&ved=0ahUKEwif1rDu8dLnAhWJmuAKHR6pBqkQ4dUDCAc&uact=5'
        bot = webdriver.Chrome()
        bot.get(link)
      
       




