import pdfplumber
import os

class PDFReader:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_pdf(self):

        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"PDF file not found: {self.file_path}")

        extracted_text = []

        try:
            with pdfplumber.open(self.file_path) as pdf:


                for page_number, page in enumerate(pdf.pages, start=1):

                    text = page.extract_text()

                    if text:
                        # Remove unnecessary spaces and blank lines
                        cleaned_text = "\n".join(
                            line.strip()
                            for line in text.splitlines()
                            if line.strip()
                        )

                        extracted_text.append(cleaned_text)

        except Exception as e:
            print("Error while reading PDF:", e)
            return ""

        return "\n".join(extracted_text)

    def get_text(self):
        return self.read_pdf()


# -----------------------------------
# Test
# -----------------------------------
if __name__ == "__main__":

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    pdf_path = os.path.join(BASE_DIR, "input", "resume.pdf")

    reader = PDFReader(pdf_path)

    text = reader.get_text()

    print("========== Resume Text ==========\n")
    print(text)