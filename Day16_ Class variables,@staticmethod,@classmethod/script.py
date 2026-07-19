# class Methods

    # class methods dont need (self) as an argument...rather we pass (cls) as first argument... that is nothing but class itself
    # we use class method decorator before creating this class method

# this is a class... Now we will modify it. We will calculate how many objects have been created from this class....
'''
class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def msg(self):
        print(f'{self.name} got {self.marks}%')


S1 = Student('Manahil',90)
S2 = Student('Rafay',95)

'''

class Student:

    counter = 0

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        Student.counter = Student.counter+1
        # when the object will be created, this initialization method will run and this class variale will increment to +1 each time.

    def msg(self):
        print(f'{self.name} got {self.marks}%')

    @classmethod
    def object_count(cls):
        return cls.counter

    @staticmethod
    def get_age(age):
        if age<18:
            print('You belong to school!')
        else:
            print('you doesnot belong to school!')


S1 = Student('Manahil',90)
S2 = Student('Rafay',95)

print(Student.object_count())
Student.get_age(34)