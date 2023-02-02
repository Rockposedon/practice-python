class circle :

    def __init__(self):
        self.radius = int(input("enter radius :"))

    def area(self):
        return 3.14*self.radius*self.radius

    def circumference(self):
        return 2*3.14*self.radius
def dwrite(var1,var2,var3):
    file1 = open("detail.txt", "a")
    datarow = "{},{},{}\n".format(var1,var2,var3)
    file1.write(datarow)
    file1.close()
    print("write operation done successfully")

c1 = circle()
area1 = c1.area()
circumference1  = c1.circumference()
radius1 = c1.radius
var1 ="radius:{}cm".format(radius1)
var2 = "area:{}sq cm".format(area1)
var3 = "circumference:{}cm".format(circumference1)

dwrite(var1,var2,var3)
#
# print("radius:{}cm".format(radius1))
# print("area:{}sq cm".format(area1))
# print("circumference:{}cm".format(circumference1))