class Student:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.section = None

    def get_first_name(self):
        return self.firstName

    def get_last_name(self):
        return self.lastName

    def get_full_name(self):
        return self.get_first_name() + " " + self.get_last_name()

    def set_first_name(self, firstName):
        self.firstName = firstName

    def set_last_name(self, lastName):
        self.lastName = lastName

    def get_section(self):
        return self.section
    
    def assign_section(self, section):
        self.section = section
    
class Section:
    def __init__(self, sectionName):
        self.sectionName = sectionName
        self.subject = None
        self.students = []

    def get_section_name(self):
        return self.sectionName

    def set_section_name(self, sectionName):
        self.sectionName = sectionName

    def get_subject(self):
        return self.subject

    def assign_to_subject(self, subject):
        self.subject = subject

    def add_student(self, student):
        if self.get_subject() == None:
            print("Student: " + student.get_full_name() + " cannot be added to section " + self.get_section_name() + " since this section has no assigned subject yet!")
        elif student.get_section() == None:
            self.students.append(student)
            student.assign_section(self)
            print("Student: " + student.get_full_name() + " added to section " + self.get_section_name())
            print("Student: " + student.get_full_name() + " added to section " + self.get_section_name())
        else:
            print("Student: " + student.get_full_name() + " is already assigned to a section!")

    def remove_student(self, student):
        if student.get_section() == None:
            print("Cannot remove student with no assigned section.")
        elif student.get_section().get_section_name() != self.get_section_name():
            print("Cannot remove student not assigned to this section.")
        else:
            self.students.remove(student)
            student.assign_section(None)
            print("Student: " + student.get_full_name() + " has been removed from this section.")


    def list_students(self):
        print("\nStudents under section " + self.get_section_name() + ":")
        for i in range(len(self.students)):
            print(str(i+1) + ". " + self.students[i].get_full_name())
        print("")
        

class Subject:
    def __init__(self, code):
        self.code = code
        self.sections = []

    def get_code(self):
        return self.code
    
    def set_code(self, code):
        self.code = code

    def add_section(self, section):
        if section.get_subject() == None:
            self.sections.append(section)
            section.assign_to_subject(self)
            print("Section " + section.get_section_name() + " added to subject " + self.get_code())
        else:
            print("Section " + section.get_section_name() + " is already assigned to a subject!")

    def remove_section(self, section):
        if section.get_subject() == None:
            print("Cannot remove section with no assigned subject.")
        elif section.get_subject().get_code() != self.get_code():
            print("Cannot remove section not assigned to this subject.")
        else:
            self.sections.remove(section)
            section.assign_to_subject(None)
            print("Section " + section.get_section_name() + " has been removed from subject " + self.get_code())


    def list_sections(self):
        print("\nSections under " + self.get_code() + ":")
        for i in range(len(self.sections)):
            print(str(i+1) + ". " + self.sections[i].get_section_name())
        print("")

student1 = Student("Marc", "Saulo")
student2 = Student("Tony", "Stark")
student3 = Student("Thor", "Odinson")
student4 = Student("Steve", "Rogers")
student5 = Student("Natasha", "Romanoff")

subject1 = Subject("CMSC 123")
subject2 = Subject("CMSC 100")

section1 = Section("D")
section2 = Section("E")
section3 = Section("F")

subject1.add_section(section1) #add D to CMSC 123
subject1.add_section(section2) #add E to CMSC 123
subject1.list_sections() #list down the sections under CMSC 123

subject1.remove_section(section3) #remove F from CMSC 123
subject1.remove_section(section2) #remove E from CMSC 123
subject2.remove_section(section1) #remove D from CMSC 100
subject1.list_sections() #list down the sections under CMSC 123

section3.add_student(student1) #add Marc Saulo to section F
section1.add_student(student2) #add Tony Stark to section D
section1.add_student(student3) #add Thor Odinson to section D
section1.list_students() #list down the students under section D

student3.set_first_name("Loki") #change name of Thor to Loki
section1.remove_student(student1) #remove Marc Saulo from section D
section1.remove_student(student2) #remove Tony Stark from section D
section1.list_students() #list down the students under section D

