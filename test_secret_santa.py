import unittest
import csv
import os
from SecretSanta import SecretSanta
from parser import Parser
from Validation import AssignmentValidator

class TestSecretSanta(unittest.TestCase):

    def setUp(self):
        """Setup test data"""
        self.test_employees_file = "test_employees.csv"
        self.test_output_file = "test_secret_santa.csv"
        self.test_last_year_file = "test_last_year.csv"

        # Create test employee data
        with open(self.test_employees_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Employee Name", "Email ID"])
            writer.writerows([
                ["Alice Johnson", "alice.johnson@example.com"],
                ["Bob Smith", "bob.smith@example.com"],
                ["Charlie Brown", "charlie.brown@example.com"]
            ])

        # Create test last year data
        with open(self.test_last_year_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Giver Name", "Giver Email", "Receiver Name", "Receiver Email"])
            writer.writerows([
                ["Alice Johnson", "alice.johnson@example.com", "Bob Smith", "bob.smith@example.com"],
                ["Bob Smith", "bob.smith@example.com", "Charlie Brown", "charlie.brown@example.com"],
                ["Charlie Brown", "charlie.brown@example.com", "Alice Johnson", "alice.johnson@example.com"]
            ])

    def test_csv_parsing(self):
        """Test if employee data is correctly read"""
        parser = Parser(self.test_employees_file)
        self.assertEqual(len(parser.employees), 3)
        self.assertEqual(parser.employees[0][0], "Alice Johnson")

    def test_secret_santa_pairs(self):
        """Test that no one is assigned to themselves"""
        santa = SecretSanta(self.test_employees_file, self.test_output_file, self.test_last_year_file)
        pairs = santa.get_secret_santa_pair()
        for giver, giver_email, receiver, receiver_email in pairs:
            self.assertNotEqual(giver_email, receiver_email)

    def test_no_repeat_from_last_year(self):
        """Test that the validator prevents repeat assignments"""
        validator = AssignmentValidator(self.test_last_year_file)
        self.assertFalse(validator.is_valid_assignment("alice.johnson@example.com", "bob.smith@example.com"))  # Repeated
        self.assertTrue(validator.is_valid_assignment("alice.johnson@example.com", "charlie.brown@example.com"))  # New

    def test_file_creation(self):
        """Test that the Secret Santa file is correctly written"""
        santa = SecretSanta(self.test_employees_file, self.test_output_file, self.test_last_year_file)
        santa.download_secret_santa_file()
        self.assertTrue(os.path.exists(self.test_output_file))

    def tearDown(self):
        """Cleanup test files"""
        for file in [self.test_employees_file, self.test_output_file, self.test_last_year_file]:
            if os.path.exists(file):
                os.remove(file)

if __name__ == "__main__":
    unittest.main()
