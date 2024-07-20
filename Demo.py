class Student(object):
    count = 0
    school = "ABC School"

    def __init__(self, firstName, lastName, number, count=0):
        self.firstName = firstName
        self.lastName = lastName
        self.number = number
        Student.count += 1
        self.count = count

    def getFullName(self):
        return f"{self.firstName} with the last name as {self.lastName}"

    @classmethod
    def changeSchoolName(cls, newName):
        Student.school = newName

    @staticmethod
    def greetings():
        print("Hello World")

    def __str__(self):
        return f"Student({self.firstName}, {self.lastName}, {self.number})"


class Programmer(Student):
    def __init__(self, firstName, lastName, number, language):
        super().__init__(firstName, lastName, number)
        self.language = language

    def __str__(self):
        return f"Programmer({self.firstName}, {self.lastName}, {self.number}, {self.language})"


## Programmer object
p1 = Programmer("John", "Doe", 1234, "Python")
print(p1)
print(p1.getFullName())
p1.greetings()
