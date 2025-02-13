import csv
import os


class AssignmentValidator:
    """Validates Secret Santa assignments to avoid repetition from last year."""

    def __init__(self, last_year_file):
        self.last_year_assignments = self._load_last_year_assignments(last_year_file)

    def _load_last_year_assignments(self, file_path):
        """Reads last year's assignments from CSV."""
        if not os.path.exists(file_path):
            return {}

        assignments = {}
        with open(file_path, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                giver_email, receiver_email = row[1], row[3]
                assignments[giver_email] = receiver_email  # Store previous pairs
        return assignments

    def is_valid_assignment(self, giver_email, receiver_email):
        """Ensures that a giver is not assigned the same receiver as last year."""
        return self.last_year_assignments.get(giver_email) != receiver_email