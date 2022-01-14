# import libraries
import matplotlib.pyplot as plt
# All the posible inputs must be integer values
x = input("Enter value: ")
# Cast input to integer
x = int(x)
# initialize values
counter = 1
xAxis = []
yAxis = []
# append the input and counter (for the x-axis)
yAxis.append(x)
xAxis.append(counter)
# Start of Algorithm 
# for odd numbers n = n * 3 + 1
# for even numbers n = n / 2
# threshold number is 1 : and will repeat 4,2,1 infinetely
while x != 1:
    if x % 2 != 0:
        x = x * 3 + 1
        yAxis.append(x)
        counter += 1
        xAxis.append(counter)
    else:
        x /= 2
        yAxis.append(x)
        counter += 1
        xAxis.append(counter)
print(yAxis)
print("end of the hailstorm")
print("start of infinite loop of 4,2,1")
print("length of the numbers ", len(yAxis))

 
# plotting the points
plt.plot(xAxis, yAxis)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('Collatz Conjecture')
 
# function to show the plot
plt.show()