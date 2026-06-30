import csv
import os
class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        candidates = []
        # Check if file exists
        if not os.path.exists(self.file_path):
            print(f"Error: File not found -> {self.file_path}")
            return candidates
        try:
            with open(self.file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    candidates.append(dict(row))
        except Exception as e:
            print("Error while reading CSV:", e)
        return candidates
# Test the file independently
if __name__ == "__main__":
    # Get project root directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Build the correct path
    csv_path = os.path.join(BASE_DIR, "input", "recruiter.csv")

    reader = CSVReader(csv_path)
    candidates = reader.read_csv()
    print("Total Candidates:", len(candidates))
    for candidate in candidates:
        print(candidate)