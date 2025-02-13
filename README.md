Project Structure
The project is organized into different modules, each handling a specific part of the Secret Santa assignment process.
SecretSanta/
│── assets/                        # CSV files for input/output
│   ├── employees.csv              # Employee data (Name, Email)
│   ├── lastyear.csv               # Last year’s assignments
│   ├── secretsantas.csv           # Output: Secret Santa pairings
│── parser.py                      # Parses employee CSV
│── validator.py                   # Validates assignments against last year
│── secret_santa.py                # Generates Secret Santa pairs
│── main.py                        # Runs the Secret Santa script
│── test_secret_santa.py           # Unit tests for validation and assignment
│── README.md                      # Documentation and setup instructions
1️⃣ Overview
This project automates the Secret Santa assignment process while ensuring that no one is assigned to themselves or their last year's recipient. The assignments are written to a CSV file for easy distribution.

2️⃣ Modules Description
📌 parser.py (Data Parsing)
Reads the employees.csv file.
Extracts employee names and email addresses.
Stores them in a list for further processing.
📌 validator.py (Assignment Validation)
Reads the lastyear.csv file.
Stores last year’s assignments to ensure no repeat pairings.
Provides a method is_valid_assignment(giver_email, receiver_email) to check whether an assignment is valid.
📌 secret_santa.py (Pair Generator)
Inherits from Parser to get employee data.
Uses random shuffling to generate Secret Santa pairs.
Ensures no employee is assigned to themselves.
Ensures that no employee gets the same recipient as last year.
Writes the final Secret Santa assignments to secretsantas.csv.
📌 main.py (Program Execution)
Reads employee data.
Calls the SecretSanta class to generate assignments.
Handles errors and prints success/failure messages.

3️⃣ How to Run the Project
🔹 Step 1: Install Dependencies
Make sure you have Python 3 installed. If you’re using a virtual environment, activate it.
pip install -r requirements.txt
🔹 Step 2: Prepare Input Files
Place your employees.csv file in the assets/ directory.
If available, place the lastyear.csv file for validation.
🔹 Step 3: Run the Main Script
Execute the script using:
python main.py
This will generate a new secretsantas.csv file inside the assets/ folder.

4️⃣ Testing the Code
To run the unit tests and ensure everything is working correctly:

python -m unittest test_secret_santa.py
5️⃣ Error Handling
If a valid assignment cannot be generated (due to constraints), an exception is raised.
If the lastyear.csv file is missing, the validator skips checking old assignments.

This document should serve as a quick reference for understanding and using the Secret Santa project.
