class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        # self.msg = self.name + " got grade " + self.grade # instead of this we will make a seperate method for this

    def msg(self):
        return self.name + " got grade " + self.grade 



stud1 = Student('AbdulRafay','B')
print(stud1.name)
stud1.grade = 'A'
print(stud1.grade) # Here the grade is changed to A
print(stud1.msg()) # By changing the grade, we still got B in the message property.... but after we made a seperate method for msg we got the correct output which is grade A
# abhi to ye sirf aik jahah tha is wajah se ham ne easily change kar lia.... pehle msg sirf aik attribute tha aur stud1.msg se chal raha tha lekin jab use method banaya to stud1.msg()--> parenthesis add karne pare call karne k liye....ab agr code bara hota aur ye msg hamne baar baar use kia hota to ye har jagah change karna parna tha.
# so we will use property decorator which will allow us to change class without effecting the client code


print('-------------------------------------------------------------')

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        
    @property
    def msg(self):
        return self.name + " got grade " + self.grade 

    @msg.setter
    def msg(self,msg):
        sent = msg.split(" ")
        print(sent)
        self.name = sent[0]
        self.grade = sent[-1]
    


stud1 = Student('AbdulRafay','B')
print(stud1.name)
stud1.grade = 'A'
print(stud1.grade)



stud1.msg = 'Abdul got grade C' 

print(stud1.msg) #--> property decorator use karne se ham use attribute ki tarah access kar rahe hain!!




print('-------------------------------------------------------')

class Student:
    def __init__(self,marks):
        self.__marks = marks

    def per(self):
        return (self.__marks/600)*100
    @property
    def marks(self):
        return self.__marks

    
    @marks.setter
    def marks(self,value):
        if value < 0 or value > 600:
            print("can't set value stick to previous value!!!")
        else:
            self.__marks = value


s = Student(400)

s.marks = 590
print(s.marks)
print(s.per())



# s.setter(500)
# print(s.getter())
# print(s.per())