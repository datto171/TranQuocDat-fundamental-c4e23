from matplotlib import pyplot

#1 prepare data 
machine_count = [18, 4, 2]

#2 prepare label 
machine_type = ['pc', 'mac', 'linux']


#3 draw pie
pyplot.pie(machine_count, labels=machine_type, autopct="%.1f%%", shadow=True, explode=[0, 0.1, 0])
pyplot.title("Pc vs Mac vs Linux usage")
pyplot.axis('equal')
#4 show
pyplot.show()