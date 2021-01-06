from matplotlib import pyplot as pt 
from matplotlib import style

style.use("ggplot") # back ground type & only for this we imported style

x = [5,8,10]    
y = [12,16,6]

x2 = [5,8,10]
y2 = [10,14,8]

pt.plot(x,y,'r',label='our\'s',linewidth=2)  # draw first red line with label , but label dosen't show 
pt.plot(x2,y2,'g',label='rival\'s',linewidth=2) # draw line two


pt.xlabel("\nx title") 
pt.ylabel("y title\n")
pt.title("info\n")

pt.legend()  # first , and second line's label show with this method

pt.grid(True,color="b")  # ubhi and aadi checks 

pt.show()  # show the graph
