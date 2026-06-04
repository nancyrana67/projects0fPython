class Employee:
    # Fixed: Changed _init_ to __init__
    def __init__(self, employee_id="", name="", age=0, salary=0):
        self.__employee_id = employee_id
        self.name = name
        self.age = age
        self.__salary = salary

    # Getter methods
    def get_employee_id(self):
        return self.__employee_id

    def get_salary(self):
        return self.__salary

    # Setter methods
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        print("\nEmployee Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)

    # Fixed: Changed _del_ to __del__
    def __del__(self):
        print("Employee object deleted.")


class Manager(Employee):
    # Fixed: Changed _init_ to __init__
    def __init__(self, employee_id, name, age, salary, department):
        super().__init__(employee_id, name, age, salary)
        self.department = department

    def display(self):
        print("\nManager Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary:", self.get_salary())
        print("Department:", self.department)


class Developer(Employee):
    # Fixed: Changed _init_ to __init__
    def __init__(self, employee_id, name, age, salary, programming_language):
        super().__init__(employee_id, name, age, salary)
        self.programming_language = programming_language

    def display(self):
        print("\nDeveloper Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary:", self.get_salary())
        print("Programming Language:", self.programming_language)


employee = None
manager = None
developer = None

while True:
    print("\n===== Employee Management System =====")
    print("1. Create Employee")
    print("2. Create Manager")
    print("3. Create Developer")
    print("4. Show Details")
    print("5. Check Subclass")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))

        employee = Employee(emp_id, name, age, salary)
        print("Employee created successfully!")

    elif choice == "2":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        manager = Manager(emp_id, name, age, salary, department)
        print("Manager created successfully!")

    elif choice == "3":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        language = input("Enter Programming Language: ")

        developer = Developer(emp_id, name, age, salary, language)
        print("Developer created successfully!")

    elif choice == "4":
        print("\n1. Employee")
        print("2. Manager")
        print("3. Developer")

        option = input("Enter choice: ")

        if option == "1":
            if employee:
                employee.display()
            else:
                print("No Employee Record Found.")

        elif option == "2":
            if manager:
                manager.display()
            else:
                print("No Manager Record Found.")

        elif option == "3":
            if developer:
                developer.display()
            else:
                print("No Developer Record Found.")

        else:
            print("Invalid Choice!")

    elif choice == "5":
        print("\nSubclass Checking")
        print("Manager is subclass of Employee:",
              issubclass(Manager, Employee))
        print("Developer is subclass of Employee:",
              issubclass(Developer, Employee))

    elif choice == "6":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice. Try Again!")

print("Thank You!")
