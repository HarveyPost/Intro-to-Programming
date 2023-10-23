# Question 1
litres = int(input("Enter the capacity of the tank in litres: "))

kilometres = int(input("Enter the number of kilometres the car can travel per litre: "))

print("The distance the car can travel is ", kilometres * litres)


# Question 2
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

volume = 3.14159 * (radius ** 2) * height

print("The volume is ", volume)


# Question 3
fahrenheit = float(input("Enter the temp in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

print("The temp in Celsius is ", celsius)