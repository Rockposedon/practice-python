# Define a class named 'circle'
class Circle:
    # Constructor to initialize the radius by taking input from the user
    def __init__(self):
        self.radius = int(input("enter radius :"))
    
    # Method to calculate and return the area of the circle
    def area(self):
        return 3.14 * self.radius * self.radius
    
    # Method to calculate and return the circumference of the circle
    def circumference(self):
        return 2 * 3.14 * self.radius

# Function to write data to a file
def dwrite(var1, var2, var3):
    # Open the "detail.txt" file in append mode
    file1 = open("detail.txt", "a")
    datarow = "{},{},{}\n".format(var1, var2, var3)
    # Write the data to the file
    file1.write(datarow)
    # Close the file
    file1.close()
    print("write operation done successfully")

# Create an instance of the 'Circle' class
c1 = Circle()

# Calculate the area and circumference using the methods of the 'Circle' class
area1 = c1.area()
circumference1 = c1.circumference()
radius1 = c1.radius

# Prepare strings with formatted data for writing to the file
var1 = "radius:{}cm".format(radius1)
var2 = "area:{}sq cm".format(area1)
var3 = "circumference:{}cm".format(circumference1)

# Call the 'dwrite' function to write the data to the file
dwrite(var1, var2, var3)

The following lines are commented out, but they print the results to the console
print("radius:{}cm".format(radius1))
print("area:{}sq cm".format(area1))
print("circumference:{}cm".format(circumference1))
