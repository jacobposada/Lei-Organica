import matplotlib.pyplot as plt 

plantData = open("plants_1.csv", "r") 
print (plantData) 

fig, simple_chart = plt.subplots() 

simple_chart.plot(plantData) 

plt.show() 

for plant in plantData: 
    identifier = [int(entry[0]) for entry in plantData] 
    sepal_width = [float(entry[1]) for entry in plantData] 
    sepal_length = [float(entry[2]) for entry in plantData] 
    petal_width = [float(entry[3]) for entry in plantData] 
    petal_length = [float(entry[4]) for entry in plantData] 

print (sepal_length) 

