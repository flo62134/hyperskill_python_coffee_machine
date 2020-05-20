class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here

    def get_id(self):
        id = self.name[0]
        id += self.last_name
        return id + self.birth_year


student = Student(input(), input(), input())
print(student.get_id())
