from matplotlib import pyplot as pt 
from matplotlib import style

# style.use("ggplot") # here this style dosen't suit

pt.bar([1,3,5,7,9],[5,2,7,8,2],label="example one")

pt.bar([2,4,6,8,10],[8,6,2,5,6],label="example two")

pt.title("info\n")
pt.xlabel("\nx title")
pt.ylabel("y title\n")

pt.legend()
pt.show()