class circle:
    def __init__(self, radius):
        self.radius = radius
        # for radius in range (1,101):
    def area(self):
        return 3.14*self.radius*self.radius
    def circumference(self):
        return 2*3.14*self.radius

def dwrite(x):
    file1 = open("detail10.txt", "a")
    file1.write(x)
    file1.close()
    print("write operation done successfully")

def dread():
    pass

for i in range(0,101):
    var1 = circle(i)
    var2 = var1.area()
    var3 = var1.circumference()
    var4 = "{},{},{}\n".format(var1.radius,var2,var3)
    dwrite(var4)
    print("radius of circle = {} cm".format(var1.radius))
    print("area of circle = {} cm".format(var2))
    print("circumference of circle = {} cm".format(var3))
    print("-----------------------------------------------")

