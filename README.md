
Logic Box 🧠
📌 Overview

Logic Box is a simple interactive Python console application that allows users to:

Generate star patterns
Analyze a range of numbers (odd/even check + sum calculation)
Exit the program

It runs in a loop until the user chooses to exit.

⚙️ Features
1. Pattern Generator
Generates a right-angled triangle pattern using *
User defines number of rows
Validates input (must be > 0)
2. Number Range Analyzer
Takes a start and end range
Checks each number as odd or even
Calculates total sum of the range
Validates range (end must be ≥ start)
3. Exit Option
Safely exits the program

▶️ How to Run

Make sure you have Python installed (Python 3+ recommended).

Run the script using:

python your_file_name.py


🧾 Menu Example
...welcome to logic box...

select an option:
1. generate a pattern.
2. analyze a range of number.
3. exit

enter your choice:

🔢 Example Outputs
Pattern Generator

Input: 5

*
**
***
****
*****
Range Analysis

Input: start = 1, end = 5

number 1 is odd.
number 2 is even.
number 3 is odd.
number 4 is even.
number 5 is odd.

sum of all numbers from 1 to 5 is: 15
🚫 Input Rules
Pattern rows must be greater than 0
Range end must be greater than or equal to start
Invalid inputs will show error messages
📌 Notes
Program runs continuously until option 3 is selected
Uses basic Python loops, conditionals, and input handling
👨‍💻 Author

Created as a beginner Python logic practice project.
