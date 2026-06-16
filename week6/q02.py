class Student:
    def __init__(self, name, age, gpa, major):
        self.name = name
        self.age = age
        self.gpa = gpa
        self.major = major

no_of_students = int(input("Enter number of students: "))
students = []
for i in range(no_of_students):
    print("Student " + str(i+1))
    student_list = [input("Name: "), input("Age: "), input("GPA: "), input("Major: ")]
    students.append(Student(student_list[0], student_list[1], student_list[2], student_list[3]))

print("Name                 Age   GPA     Major")
for student in students:
    print(f"{student.name:20} {student.age:5} {student.gpa:7} {student.major}")
