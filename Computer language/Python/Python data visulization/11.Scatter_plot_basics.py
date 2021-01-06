import matplotlib.pyplot as plt 
from matplotlib import style

style.use('ggplot')


x = [1,5,2,6,9,8,7,5,4,3]
y = [5,7,9,6,4,2,3,7,5,9]

plt.scatter(x,y,label="skitscat",color='r',s=25)

plt.title('Scatter plot')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()