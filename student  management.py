class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("\nName:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)


students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        marks = input("Enter marks: ")

        student = Student(name, roll_no, marks)
        students.append(student)

        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            for student in students:
                student.display()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
