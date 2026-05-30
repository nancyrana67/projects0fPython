# ==============================
# DATA ANALYZER AND TRANSFORMER
# ==============================

data = []
dataset_summary = {}

# Input Data
def input_data():
    """Input data into a 1D list."""
    global data

    data = list(map(int, input(
        "Enter data for a 1D array (separated by spaces): "
    ).split()))

    print("Data has been stored successfully!")


# Built-in Functions
def display_summary():
    """Display summary using built-in functions."""
    global dataset_summary

    if not data:
        print("No data available!")
        return

    dataset_summary = {
        "Total Elements": len(data),
        "Minimum Value": min(data),
        "Maximum Value": max(data),
        "Sum": sum(data),
        "Average": round(sum(data) / len(data), 2)
    }

    print("\nData Summary:")
    for key, value in dataset_summary.items():
        print(f"- {key}: {value}")


# User Defined Function
def calculate_average():
    """Calculate average of dataset."""
    return sum(data) / len(data)


# *args Function
def show_values(*args):
    """Display multiple values using *args."""
    print("\nValues in Dataset:")
    for value in args:
        print(value, end=" ")
    print()


# **kwargs Function
def dataset_info(**kwargs):
    """Display dataset information using **kwargs."""
    print("\nDataset Information:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Recursion
def factorial(n):
    """Calculate factorial recursively."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Lambda Function
def filter_data():
    """Filter data using lambda function."""
    threshold = int(input(
        "Enter a threshold value to filter out data above this value: "
    ))

    filtered = list(filter(lambda x: x >= threshold, data))

    print(f"\nFiltered Data (values >= {threshold}):")
    print(*filtered, sep=", ")


# Sorting
def sort_data():
    """Sort dataset."""
    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    choice = input("Enter your choice: ")

    if choice == "1":
        sorted_data = sorted(data)
        print("\nSorted Data in Ascending Order:")
    else:
        sorted_data = sorted(data, reverse=True)
        print("\nSorted Data in Descending Order:")

    print(*sorted_data, sep=", ")


# Return Multiple Values
def statistics():
    """Return multiple statistics."""
    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = total / len(data)

    return minimum, maximum, total, average


# Display Documentation
def show_docs():
    """Display all function documentation."""
    print("\nFunction Documentation:")
    print(input_data.__doc__)
    print(display_summary.__doc__)
    print(calculate_average.__doc__)
    print(show_values.__doc__)
    print(dataset_info.__doc__)
    print(factorial.__doc__)
    print(filter_data.__doc__)
    print(sort_data.__doc__)
    print(statistics.__doc__)


# ==========================
# MAIN PROGRAM
# ==========================

print("Welcome to the Data Analyzer and Transformer Program")

while True:

    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Show *args and **kwargs")
    print("8. Show Function Documentation")
    print("9. Exit Program")

    choice = input("Please enter your choice: ")

    if choice == "1":
        input_data()

    elif choice == "2":
        display_summary()

    elif choice == "3":
        num = int(input("Enter a number to calculate its factorial: "))
        print(f"\nFactorial of {num} is: {factorial(num)}")

    elif choice == "4":
        if data:
            filter_data()
        else:
            print("Please input data first.")

    elif choice == "5":
        if data:
            sort_data()
        else:
            print("Please input data first.")

    elif choice == "6":
        if data:
            minimum, maximum, total, average = statistics()

            print("\nDataset Statistics:")
            print("- Minimum value:", minimum)
            print("- Maximum value:", maximum)
            print("- Sum of all values:", total)
            print("- Average value:", round(average, 2))
        else:
            print("Please input data first.")

    elif choice == "7":
        if data:
            show_values(*data)

            dataset_info(
                Total_Elements=len(data),
                Minimum=min(data),
                Maximum=max(data),
                Average=round(calculate_average(), 2)
            )
        else:
            print("Please input data first.")

    elif choice == "8":
        show_docs()

    elif choice == "9":
        print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")