import csv


class Parser:
    """Base class to handle CSV file reading."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.employees = self._load_employees()

    def _load_employees(self):
        """Reads employee data from CSV."""
        try:
            with open(self.file_path, mode="r") as file:
                reader = csv.reader(file)
                next(reader)
                return [row for row in reader]
        except FileNotFoundError:
            raise Exception(f"File {self.file_path} not found.")