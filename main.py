from classreport import ClassReport
from student import Student
from school_class import SchoolClass
from subject import Subject
from grade import Grade


def create_subject_liste(actual_report):
    actual_report.add_subject(Subject("Mathe"))
    actual_report.add_subject(Subject("Deutsch"))
    actual_report.add_subject(Subject("Turnen"))


def main():
    if __name__ == "__main__":
        # Am Anfang steht da eine Klasse
        the_class = SchoolClass("IM993a")
        #
        # Dann braucht es mal ein paar leere Zeugnisse und deren Fächer
        report_max = ClassReport()
        create_subject_liste(report_max)
        #
        report_pia = ClassReport()
        create_subject_liste(report_pia)
        #
        report_cem = ClassReport()
        create_subject_liste(report_cem)
        #
        # Und natürlich Lernende
        max = Student("Max", report_max)
        pia = Student("Pia", report_pia)
        cem = Student('Cem', report_cem)
        #
        # Nun immatrikulieren wir die Lernenden
        the_class.add_student(max)
        the_class.add_student(pia)
        the_class.add_student(cem)
        # Und dann erstellen wir mal die Klasseliste
        the_class.print_student_list()
        #
        # Jetzt braucht es noch Noten
        report_max.get_subject(0).add_grade(Grade(4.0, "1.1.11"))
        report_max.get_subject(0).add_grade(Grade(4.5, "2.2.22"))
        report_max.get_subject(1).add_grade(Grade(4.0, "3.3.33"))
        report_max.get_subject(1).add_grade(Grade(6.0, "4.4.44"))
        report_max.get_subject(1).add_grade(Grade(5.0, "5.5.55"))
        report_max.get_subject(2).add_grade(Grade(4.5, "6.6.66"))
        report_max.get_subject(2).add_grade(Grade(5.0, "7.7.77"))
        report_max.get_subject(2).add_grade(Grade(5.0, "8.8.88"))
        report_max.get_subject(2).add_grade(Grade(5.5, "9.9.99"))
        #
        report_pia.get_subject(0).add_grade(Grade(5.5, "1.1.11"))
        report_pia.get_subject(0).add_grade(Grade(5.5, "2.2.22"))
        report_pia.get_subject(1).add_grade(Grade(4.5, "3.3.33"))
        report_pia.get_subject(1).add_grade(Grade(6.0, "4.4.44"))
        report_pia.get_subject(1).add_grade(Grade(5.5, "5.5.55"))
        report_pia.get_subject(2).add_grade(Grade(4.0, "6.6.66"))
        report_pia.get_subject(2).add_grade(Grade(5.5, "7.7.77"))
        report_pia.get_subject(2).add_grade(Grade(6.0, "8.8.88"))
        report_pia.get_subject(2).add_grade(Grade(5.5, "9.9.99"))
        #
        report_cem.get_subject(0).add_grade(Grade(5.0, "1.1.11"))
        report_cem.get_subject(0).add_grade(Grade(3.5, "2.2.22"))
        report_cem.get_subject(1).add_grade(Grade(5.5, "3.3.33"))
        report_cem.get_subject(1).add_grade(Grade(6.0, "4.4.44"))
        report_cem.get_subject(1).add_grade(Grade(5.0, "5.5.55"))
        report_cem.get_subject(2).add_grade(Grade(4.5, "6.6.66"))
        report_cem.get_subject(2).add_grade(Grade(6.0, "7.7.77"))
        report_cem.get_subject(2).add_grade(Grade(6.0, "8.8.88"))
        report_cem.get_subject(2).add_grade(Grade(5.5, "9.9.99"))
        #
        the_class.print_student_report("Max")
        the_class.print_student_report("Pia")
        the_class.print_student_report("Cem")
        the_class.print_student_report("Theo")
        #
        report_cem.print_details()


if __name__ == '__main__':
    main()
