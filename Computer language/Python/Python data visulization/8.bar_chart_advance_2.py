import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import style 


# style.use('ggplot')

items = ['candy','cold drinks','cegrettes','lottery']
revenue_2010 = [8000,31000,37000,1250]
revenue_2020 = [11000,33000,45000,1750]
profit_2010 = [800,3100,3700,12500]
profit_2020 = [1100,3300,4500,18400]

xpos = np.arange(len(items))


plt.xticks(xpos,items)
plt.bar(xpos-0.15,revenue_2010,label='2010(revenue)',width=0.1)
plt.bar(xpos-0.05,revenue_2020,label='2020(revenue)',width=0.1)
plt.bar(xpos+0.05,profit_2010,label='2010(profit)',width=0.1,color='#13640E')
plt.bar(xpos+0.15,profit_2020,label='2020(profit)',width=0.1,color='#29F00D')

plt.legend()
plt.title('Mobil Gas Station\'sell & profit in 2010 & 2020')
plt.ylabel('revenue')
plt.show()

# if you want this chart horizontaly  than
# use  plt.barh() insted of plt.bar()
# and change some value like : use yticks in sted of xticks .....


