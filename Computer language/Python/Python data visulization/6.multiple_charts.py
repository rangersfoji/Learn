from matplotlib import pyplot as pt 

# you can write any type of chart more than one

# you can do it with the help of 'subplot'
# see the below example

# subplot takes three arguments   
# 1.how many charts? 
# 2.horisontali how many?
# 3.what's the number of that chart

# in output you can adujest the spaces between them to see clear

pt.subplot(421)
pt.plot([5,12,23,50],[5,42,54,76])
pt.title("info 1")
pt.xlabel("x 1")
pt.ylabel("y 1")

pt.subplot(422)
pt.plot([3,1,5,4],[5,2,4,6])
pt.title("info 1")
pt.xlabel("x 1")
pt.ylabel("y 1")

pt.subplot(423)
pt.plot([5,2,12,25],[1,5,3,2])
pt.title("info 1")
pt.xlabel("x 1")
pt.ylabel("y 1")

pt.subplot(424)
pt.plot([3,1,5,4],[5,2,4,6])
pt.title("info 1")
pt.xlabel("x 1")
pt.ylabel("y 1")

pt.show()


