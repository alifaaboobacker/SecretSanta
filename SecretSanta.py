import csv
import random

from Validation import AssignmentValidator
from parser import Parser


class SecretSanta(Parser):
    """Handles Secret Santa assignment generation, inheriting from Parser."""

    def __init__(self, file_path, output_file_path, last_year_file):
        super().__init__(file_path)  # Inherit employee data loading from Parser
        self.output_file_path = output_file_path
        self.validator = AssignmentValidator(last_year_file)  # Validator for previous assignments

    def get_secret_santa_pair(self):
        """Generates Secret Santa pairs while ensuring no repeat assignments from last year."""
        givers = self.employees[:]
        receivers = self.employees[:]

        for _ in range(100):  # Max retries to prevent infinite loops
            random.shuffle(receivers)
            if all(giver[1] != receiver[1] and self.validator.is_valid_assignment(giver[1], receiver[1])
                   for giver, receiver in zip(givers, receivers)):
                return [(giver[0], giver[1], receiver[0], receiver[1]) for giver, receiver in zip(givers, receivers)]

        raise RuntimeError("Could not generate valid Secret Santa assignments. Try modifying input data.")

    def download_secret_santa_file(self):
        """Writes the Secret Santa assignments to a CSV file."""
        secret_santa_pairs = self.get_secret_santa_pair()
        with open(self.output_file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Giver Name", "Giver Email", "Receiver Name", "Receiver Email"])
            writer.writerows(secret_santa_pairs)
