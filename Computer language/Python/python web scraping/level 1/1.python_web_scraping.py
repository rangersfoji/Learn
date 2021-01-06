# pip install requests
# pip install beautifulsoup4
# pip install lxml  (here we use this parser)
# pip install html5lib (this is second parser , we won't use here)

'''

from bs4 import BeautifulSoup
import requests



# 1. for local file in your desktop
with open('index.html') as html_file:
	soup = BeautifulSoup(html_file,'lxml')

print(soup) 
ot = whole html code

print(soup.prettify())
ot = whole html code (but in nice format)

# parse data
match = soup.title
print(match)
ot = print first title tag
		ex . <title>this is my first website</title>

match = soup.title.text
print(match) 
ot = this is my first website


# but this gives us only first tag , 
# what if we want specific tag
# use find method

match = soup.find('div',class_='footer')  # class_ because python has class atribute
print(match)
ot = <div class = 'footer'>
		<p> Footer information</p>
	 </div>


# in browser to find exectly what you want
# right click, inspect element

article = soup.find('div',class_='article')
print(article)
ot = first that class's element'

	example:
		<div class="article">
		<h2><a href="article_1.html">Aricle 1 Headline</a></h2>
		<p>This is a summary of article 1</p>
		</div>

    # if you want only h2 tag's a tag's text
    Headline = article.h2.a.text
    print(Headline)
    ot = Aricle 1 Headline

    summary = article.p.text
    print(summary)
    ot = This is a summary of article 1

# that was only that class's first element
# we want all element
# we can use find_all but that return list so put in for loop

for article in soup.find_all('div',class_='article')
	Headline = article.h2.a.text
    print(Headline)

    summary = article.p.text
    print(summary)

    print()

ot = Aricle 1 Headline
	 This is a summary of article 1
	 
	 Aricle 2 Headline
	 This is a summary of article 2

'''
'''
# now start with online websites

from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source,'lxml')

print(soup.prettify())

ot = whole html code 


# now we want title,summary ,video link (all)from websites
# choose class that has all the information you want

# here article tag

article = soup.find('article')
print(article.prettify())
ot = first article tag's info '

headline = article.h2.a.text
print(headline)
ot = Python Tutorial: Zip Files – Creating and Extracting Zip Archives
here this headline is first link so we can use 'article.a.text' but sometiems it convenient 
however don't use every single tag to specify or it will gonna be so long line 

summary = article.find('div',class_='entry-content').p.text
print(summary)
ot = summary of the article


# in video it's different
# in youtube video there is not direncet link you have to create it
# in youtube every video has their own 'id'

video_src = article.find('iframe',class_='youtube-player')
print(video_src)
ot = 
<iframe allowfullscreen="true" class="youtube-player" height="360" 
src="https://www.youtube.com/embed/z0gguhEmWiY?version=3&amp;rel=1&amp;fs=
&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;
wmode=transparent" style="border:0;" type="text/html" width="640"></iframe>

# here we don't want to get text between tag 
# but we want text of tags (src text # link)
# you can do this:
video_src = article.find('iframe',class_='youtube-player')['src']
print(video_src)
ot = 
https://www.youtube.com/embed/z0gguhEmWiY?version=3&rel=1&fs=1&autohide=
2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent

# here video id = z0gguhEmWiY (after last '/' and before '?')
vid_id = video_src.split('/')
print(vid_id)
ot = 
['https:', '', 'www.youtube.com', 'embed', 
'z0gguhEmWiY?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_
load_policy=1&wmode=transparent']

# here it gives list
# so now use 
vid_id = video_src.split('/')[4]
print(vid_id)
ot = 
'z0gguhEmWiY?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_
load_policy=1&wmode=transparent'

vid_id = vid_id.split('?')[0]
print(vid_id)
ot = z0gguhEmWiY

# now create youtube link
yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)
ot = https://youtube.com/watch?v=z0gguhEmWiY
'''

'''
# now we got all info from article 1 , now we want it from all article
# use for loop :
# whole code :


from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source,'lxml')

for article in soup.find_all('article'):
	headline = article.h2.a.text
	print(headline)

	summary = article.find('div',class_='entry-content').p.text
	print(summary)

	vid_src = article.find('iframe',class_='youtube-player')['src']


	vid_id = vid_src.split('/')[4]
	vid_id = vid_id.split('?')[0]

	yt_link = f'https://youtube.com/watch?v={vid_id}'
	print(yt_link)

	print()

ot = error!!
#because it can be possible that so article don't have link 
# or don't have specific info that you try to gain
# if it can give you an error!!
# solution use try except 
'''

'''
from bs4 import BeautifulSoup
import requests

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source,'lxml')

for article in soup.find_all('article'):
	headline = article.h2.a.text
	print(headline)

	summary = article.find('div',class_='entry-content').p.text
	print(summary)


	

	try:
		vid_src = article.find('iframe',class_='youtube-player')['src']


		vid_id = vid_src.split('/')[4]
		vid_id = vid_id.split('?')[0]

		yt_link = f'https://youtube.com/watch?v={vid_id}'
	except Exception as e:
		yt_link = "Link not found!!"

	print(yt_link)

	print()
'''

# now you are just printing but you can save this in file
# cvs file 
# see example below

# import csv (top)


from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source,'lxml')

csv_file = open('cms_scrape.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])


for article in soup.find_all('article'):
	headline = article.h2.a.text
	print(headline)

	summary = article.find('div',class_='entry-content').p.text
	print(summary)


	

	try:
		vid_src = article.find('iframe',class_='youtube-player')['src']


		vid_id = vid_src.split('/')[4]
		vid_id = vid_id.split('?')[0]

		yt_link = f'https://youtube.com/watch?v={vid_id}'
	except Exception as e:
		yt_link = "Link not found!!"

	print(yt_link)

	print()

	csv_writer.writerow([headline,summary,yt_link])

csv_file.close()
