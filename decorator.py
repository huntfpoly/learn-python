class Student:
    def __init__(self, name):
        self.name = name

    # @property
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self, value):
    #     self._name = value

student = Student('Hieu')
print(student.name)
student.name = 'Hieu pv'
print(student.name)