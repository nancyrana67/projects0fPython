print(" Welcome to Student Data Organizer ")


print("\nThis program helps you:")
print("- Add student records")
print("- Display all students")
print("- Update student information")
print("- Delete student records")
print("- Display unique subjects\n")

students = []
all_subjects = set()


def add_student():

    print("\n--- Add Student ---")
    name = input("Enter student name: ")

    
    age = int(input("Enter age: "))
    grade = input("Enter grade: ")

    subjects_input = input("Enter subjects (comma-separated): ")
    subjects = [sub.strip() for sub in subjects_input.split(",")]
    
    student_id = input("Enter student ID: ")
    dob = input("Enter date of birth: ")

    #tuple
    student_tuple = (student_id, dob)

    # Dictionary
    student = {
        "id": student_tuple[0],
        "dob": student_tuple[1],
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects
    }

    
    students.append(student)
    all_subjects.update(subjects)
    print("\nStudent added successfully!\n")


# Function 
def display_students():

    print("\n--- All Students ---")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
       
        print(f"""
Student ID : {student['id']}
Name       : {student['name']}
Age        : {student['age']}
Grade      : {student['grade']}
DOB        : {student['dob']}
Subjects   : {", ".join(student['subjects'])}
""")

        print("Student {} is in grade {}.".format(
            student['name'],
            student['grade']
        ))

        print("Age of %s is %d years." %
              (student['name'], student['age']))

        print("-" * 40)


# Function to update student
def update_student():

    print("\n--- Update Student ---")

    sid = input("Enter student ID to update: ")

    found = False

    for student in students:
        if student["id"] == sid:
            found = True

            print("\nWhat do you want to update?")
            print("1. Age")
            print("2. Subjects")

            choice = input("Enter choice: ")

            if choice == "1":

                new_age = int(input("Enter new age: "))
                student["age"] = new_age
                print("Age updated successfully!")

            elif choice == "2":

                new_subjects = input(
                    "Enter new subjects (comma-separated): "
                )

                subject_list = [
                    sub.strip()
                    for sub in new_subjects.split(",")
                ]

                student["subjects"] = subject_list

                # Update set
                all_subjects.update(subject_list)

                print("Subjects updated successfully!")

            else:
                print("Invalid choice!")

    if not found:
        print("Student ID not found!")


# Function to delete student
def delete_student():

    print("\n--- Delete Student ---")

    sid = input("Enter student ID to delete: ")

    found = False

    for i in range(len(students)):

        if students[i]["id"] == sid:

            found = True

            # del keyword
            del students[i]

            print("Student record deleted successfully!")
            break

    if not found:
        print("Student ID not found!")


# Function to display unique subjects
def display_subjects():

    print("\n--- Unique Subjects Offered ---")

    if len(all_subjects) == 0:
        print("No subjects available.")
    else:
        for subject in all_subjects:
            print(subject)


# Main Menu
while True:

    print("\n-------- MENU--------")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        display_subjects()

    elif choice == "6":

        print("\nThank you for using Student Data Organizer!")
        break

    else:
        print("Invalid choice! Please try again.")
