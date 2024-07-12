#Pseudocode for the program:


#Class Course:
#    Properties:
#        - Course code
#        - Name
#        - Teacher name
#        - Email
#        - Credits
#        - Lecture time and location
#        - Notes (optional)
#        - Assignments list
#        - Midterms list
#        - Finals list
#        - Deadlines schedule
#
#    Methods/Functions:
#        - add_assignment()
#        - add_midterm()
#        - add_final()
#        - add_deadline()
#        - modify_notes()
#        - show_course_info()
#        - show_upcoming_deadline()
#
#Main program:
#    Initialize an empty list to store Course objects
#    Create a menu-driven program to:
#        1. Add a new course
#        2. Add assignments, midterms, and finals to a course
#        3. Add notes to a course
#        4. Add deadlines to a course
#        5. Modify course information
#        6. Display course information
#        7. Show upcoming deadline
#        8. Save data to a file
#        9. Load data from a file
#        10. Exit the program



import pickle

class Course:
    def __init__(self, code, name, teacher, email, credits, schedule, notes=""):
        self.code = code
        self.name = name
        self.teacher = teacher
        self.email = email
        self.credits = credits
        self.schedule = schedule
        self.notes = notes
        self.assignments = []
        self.midterms = []
        self.finals = []
        self.deadlines = {}

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def add_midterm(self, midterm):
        self.midterms.append(midterm)

    def add_final(self, final):
        self.finals.append(final)

    def add_deadline(self, deadline, description):
        self.deadlines[deadline] = description

    def modify_notes(self, new_notes):
        self.notes = new_notes

    def show_course_info(self):
        print(f"Course: {self.name} ({self.code})")
        print(f"Teacher: {self.teacher} ({self.email})")
        print(f"Credits: {self.credits}")
        print(f"Lecture schedule: {self.schedule}")
        print(f"Notes: {self.notes}")

    def show_upcoming_deadline(self):
        if not self.deadlines:
            print("No upcoming deadlines for this course.")
        else:
            nearest_deadline = min(self.deadlines)
            print(f"Upcoming Deadline: {nearest_deadline} - {self.deadlines[nearest_deadline]}")

def main():
    courses = []

    while True:
        print("\nStudent Organizer Menu:")
        print("1. Add a new course")
        print("2. Add assignments, midterms, and finals to a course")
        print("3. Add notes to a course")
        print("4. Add deadlines to a course")
        print("5. Modify course information")
        print("6. Display course information")
        print("7. Show upcoming deadline")
        print("8. Save data to a file")
        print("9. Load data from a file")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            code = input("Enter course code: ")
            name = input("Enter course name: ")
            teacher = input("Enter teacher's name: ")
            email = input("Enter teacher's email: ")
            credits = input("Enter credits: ")
            schedule = input("Enter lecture schedule: ")
            notes = input("Enter any notes (optional): ")
            course = Course(code, name, teacher, email, credits, schedule, notes)
            courses.append(course)
            print("Course added successfully.")

        elif choice == "2":
            # Implement adding assignments, midterms, and finals to a course
            pass

        elif choice == "3":
            # Implement adding notes to a course
            pass

        elif choice == "4":
            # Implement adding deadlines to a course
            pass

        elif choice == "5":
            # Implement modifying course information
            pass

        elif choice == "6":
            course_code = input("Enter the course code to display information: ")
            for course in courses:
                if course.code == course_code:
                    course.show_course_info()
                    break
            else:
                print("Course not found.")

        elif choice == "7":
            course_code = input("Enter the course code to show upcoming deadline: ")
            for course in courses:
                if course.code == course_code:
                    course.show_upcoming_deadline()
                    break
            else:
                print("Course not found.")

        elif choice == "8":
            with open("courses_data.pkl", "wb") as file:
                pickle.dump(courses, file)
                print("Data saved to 'courses_data.pkl'.")

        elif choice == "9":
            try:
                with open("courses_data.pkl", "rb") as file:
                    courses = pickle.load(file)
                print("Data loaded from 'courses_data.pkl'.")
            except FileNotFoundError:
                print("No data found. Use option 1 to add courses.")

        elif choice == "10":
            print("Exiting the Student Organizer. Goodbye!")
            break

if __name__ == "__main__":
    main()
        