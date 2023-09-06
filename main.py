from class_report import ClassReport
from student import Student
from school_class import SchoolClass

if __name__ == '__main__':
    r = ClassReport()
    rr = ClassReport()
    s = Student('Kevin', r)
    ss = Student('Rene', rr)
    c = SchoolClass('IM20ab')
    s.school_class = c
    ss.school_class = c
    c.add_student(s)
    c.add_student(ss)

    c.print_student_list()
    print(s.school_class)
