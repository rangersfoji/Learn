from bs4 import BeautifulSoup
import requests

source = requests.get('https://techcrunch.com/tag/blogs/').text

soup = BeautifulSoup(source,'lxml')


j = 1
ls = set()
for i in soup.findAll('div'):

    # title
    try:
        title = i.find('a',class_='post-block__title__link').text.strip()
    except:
        title = 'Title Not Found !!!'
    
    # content
    try :
        content = i.find('div',class_='post-block__content').text.strip()
    except :
        content = 'Content Not Found !!!'

    # img 
    try :
        img = i.find('a',class_='post-block__title__link')['href']
    except:
        img = 'Image Link Not Found !!!'

    if ((title == 'Title Not Found !!!') and (content == 'Content Not Found !!!')) and (img == 'Image Link Not Found !!!'):
        continue

    ls.add(tuple([title,content,img]))

    j += 1


ls = list(ls)
ls.sort()
j = 1
for i in ls:
    print(f'{j}.')
    print('\tTitle :',i[0])
    print('\tContent :',i[1])
    print('\tLink :',i[2])
    j += 1


   

    
        

    



