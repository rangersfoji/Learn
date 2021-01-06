from matplotlib import pyplot as plt 

# this is histogram 
# difference between historgram and bar chart

'''
In histogram - contatative variables
In bar - catagorical variables

like here bins are 0,10,20  means 10 difference 
means 1-10 values shows in one barline
here in histogram you can show approxy ages like you can say 
between 20-30 age group there is 70 % population.

however in barchart you have fix value like  google company has this profit and that revenue
'''

populatoin_ages = [22,55,62,45,21,22,64,34,42,42,4,99,102,110,120,111,122,130,111,115,112,80,75,65,54,44,43,42,48]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(populatoin_ages,bins,histtype='bar',rwidth=0.8,label='ages')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Histogram')
plt.legend()
plt.show()
