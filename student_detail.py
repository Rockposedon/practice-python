class student_detail:
    def __init__(self):
        self.name = input("enter student name :")
        self.fathername = input("enter father name : ")
        self.age = input("enter age : ")
        self.year = input("enter year :  ")
        self.course = input("enter course name  : ")
        self.contact = input("enter contact :")
    def show_detail(self):
        print("name : ", self.name)
        print(" father name : ", self.fathername)
        print("age : ", self.age)
        print(" joining year : ", self.year)
        print("course : ", self.course)
        print("contact details :", self.contact)

