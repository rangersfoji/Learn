import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import style 


style.use('ggplot')

items = ['candy','cold drinks','cegrettes','lottery']
revenue_2010 = [8000,31000,37000,125000]
revenue_2020 = [11000,33000,45000,184000]

xpos = np.arange(len(items))  # you will understand this after learing numpy


plt.xticks(xpos,items)
plt.bar(xpos-0.2,revenue_2010,label='2010',width=0.4)

plt.bar(xpos+0.2,revenue_2020,label='2020',width=0.4)

plt.legend()
plt.title('Mobil Gas Station\'sell & profit in 2010 & 2020')
plt.ylabel('revenue')
plt.show()

# if you want this chart horizontaly  than
# use  plt.barh() insted of plt.bar()
# and change some value like : use yticks in sted of xticks .....


