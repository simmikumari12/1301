class EmptyRosterError(Exception):
    def __init__(self):
        super().__init__('Error: Course Roster is Empty!')


class StudentNotFoundError(Exception):
    def __init__(self, student_id):
        super().__init__(f'Error: Student ({student_id}) not found.')


class GradeItemNotFoundError(Exception):
    def __init__(self, grade_item_name):
        super().__init__(f'Error: Grade Item ({grade_item_name}) not found.')


class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def get_student_id(self):
        return self.student_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name


class GradeItem:
    def __init__(self, name, total_points):
        self.name = name
        self.total_points = total_points
        self.grades = {}

    def add_student_grade(self, student_id, grade):
        self.grades[student_id] = grade

    def get_name(self):
        return self.name

    def get_total_points(self):
        return self.total_points

    def get_student_grade(self, student_id):
        return self.grades.get(student_id, None)


class Course:
    def __init__(self):
        self.roster = []
        self.grade_items = []

    def add_student(self, student):
        self.roster.append(student)

    def add_grade_item(self, grade_item):
        self.grade_items.append(grade_item)

    def add_student_grade(self, grade_item_name, student_id, grade):
        student = next((s for s in self.roster if s.get_student_id() == student_id), None)
        if not student:
            raise StudentNotFoundError(student_id)

        grade_item = next((g for g in self.grade_items if g.get_name() == grade_item_name), None)
        if not grade_item:
            raise GradeItemNotFoundError(grade_item_name)

        grade_item.add_student_grade(student_id, grade)

    def print_student_grades(self, student_id):
        if not self.roster:
            raise EmptyRosterError()

        student = next((s for s in self.roster if s.get_student_id() == student_id), None)
        if not student:
            raise StudentNotFoundError(student_id)

        print(f"\n{student.get_last_name()}, {student.get_first_name()} ({student_id}):")
        for grade_item in self.grade_items:
            grade = grade_item.get_student_grade(student_id)
            print(f"  {grade_item.get_name()}: {grade if grade is not None else 'N/A'} ({grade_item.get_total_points()})")

    def print_roster(self):
        if not self.roster:
            raise EmptyRosterError()

        print("\nCourse Roster:")
        for student in self.roster:
            print(f"  {student.get_last_name()}, {student.get_first_name()} ({student.get_student_id()})")

    def print_class_grades(self):
        if not self.roster:
            raise EmptyRosterError()

        print("\nClass Grades:")
        for student in self.roster:
            print(f"{student.get_last_name()}, {student.get_first_name()} ({student.get_student_id()}):")
            for grade_item in self.grade_items:
                grade = grade_item.get_student_grade(student.get_student_id())
                print(f"  {grade_item.get_name()}: {grade if grade is not None else 'N/A'} ({grade_item.get_total_points()})")


def main():
    print("\nWelcome to CSC/DSCI 1301: Principles in CS/DS 1")
    course = Course()
    print("Please choose one of the following options (Enter 'quit' or 'q' to exit):")
    print("1) Add a Student.")
    print("2) Add a Grade Item.")
    print("3) Add a Student's Grade.")
    print("4) Print a Student's Grades.")
    print("5) Print Course Roster.")
    print("6) Print Class Grades.\n")
    while True:
        choice = input(":> ").lower()

        try:
            if choice in {'1', 'add student'}:
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                try:
                    student_id = int(input("Enter Student ID: "))
                    course.add_student(Student(first_name, last_name, student_id))
                except ValueError:
                    print("Error: Enter an Integer Student ID.")

            elif choice in {'2', 'add grade item'}:
                name = input("Enter grade item: ")
                try:
                    total_points = int(input("Enter the total points for the grade item: "))
                    course.add_grade_item(GradeItem(name, total_points))
                except ValueError:
                    print("Error: Enter an Integer for total points.")

            elif choice in {'3', "add student's grade"}:
                grade_item_name = input("Enter grade item name: ")
                try:
                    student_id = int(input("Enter Student ID: "))
                    grade = float(input("Enter Student Grade: "))
                    course.add_student_grade(grade_item_name, student_id, grade)
                except ValueError:
                    print("Error: Enter numeric values for Student ID and Grade.")
                except (StudentNotFoundError, GradeItemNotFoundError) as e:
                    print(e)

            elif choice in {'4', "print a student's grades"}:
                try:
                    student_id = int(input("Enter Student ID: "))
                    course.print_student_grades(student_id)
                except ValueError:
                    print("Error: Enter an Integer Student ID.")
                except (StudentNotFoundError, EmptyRosterError) as e:
                    print(e)

            elif choice in {'5', 'print course roster'}:
                try:
                    course.print_roster()
                except EmptyRosterError as e:
                    print(e)

            elif choice in {'6', 'print class grades'}:
                try:
                    course.print_class_grades()
                except EmptyRosterError as e:
                    print(e)

            elif choice in {'quit', 'q'}:
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()