import os
import json

from csv_reader import CSVReader
from pdf_reader import PDFReader
from merger import Merger
from confidence import Confidence
from projector import Projector
from validator import Validator


def main():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    csv_path = os.path.join(BASE_DIR, "input", "recruiter.csv")
    pdf_path = os.path.join(BASE_DIR, "input", "resume.pdf")
    config_path = os.path.join(BASE_DIR, "config", "default.json")
    output_path = os.path.join(BASE_DIR, "output", "result.json")

    # --------------------
    # Read Resume
    # --------------------

    pdf_reader = PDFReader(pdf_path)
    pdf_text = pdf_reader.read_pdf()

    temp_merger = Merger({}, pdf_text)

    pdf_email = temp_merger.extract_email()
    pdf_phone = temp_merger.extract_phone()

    print("Resume Email :", pdf_email)
    print("Resume Phone :", pdf_phone)

    # --------------------
    # Read CSV
    # --------------------

    csv_reader = CSVReader(csv_path)
    candidates = csv_reader.read_csv()

    matched_candidate = None

    for candidate in candidates:

        csv_email = candidate.get("Email", "").strip().lower()

        csv_phone = candidate.get("Phone", "")

        if pdf_email and csv_email == pdf_email.lower():
            matched_candidate = candidate
            break

        if pdf_phone and csv_phone:
            if pdf_phone.endswith(csv_phone[-10:]):
                matched_candidate = candidate
                break

    if matched_candidate is None:
        print("No matching candidate found in CSV.")
        return

    print("Matched Candidate :", matched_candidate["FullName"])

    # --------------------
    # Merge
    # --------------------

    merger = Merger(matched_candidate, pdf_text)

    merged_profile = merger.merge()

    confidence = Confidence.calculate(merged_profile,matched_candidate)

    projector = Projector(config_path)

    final_output = projector.project(
        merged_profile,
        confidence
    )

    valid, errors = Validator.validate(final_output)

    if not valid:
        print(errors)
        return

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(final_output, file, indent=4)

    print("\nTransformation Successful\n")

    print(json.dumps(final_output, indent=4))


if __name__ == "__main__":
    main()