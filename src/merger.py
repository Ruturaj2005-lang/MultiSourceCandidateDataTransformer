import re
from normalizer import Normalizer


class Merger:

    def __init__(self, csv_data, pdf_text):
        self.csv_data = csv_data
        self.pdf_text = pdf_text

    # -----------------------------
    # Extract Name
    # -----------------------------
    def extract_name(self):
        lines = self.pdf_text.split("\n")

        for line in lines:
            line = line.strip()

            if len(line.split()) >= 2 and len(line) < 40:
                return line

        return self.csv_data.get("FullName")

    # -----------------------------
    # Extract Email
    # -----------------------------
    def extract_email(self):
        match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', self.pdf_text)

        if match:
            return match.group().strip()

        return None

    # -----------------------------
    # Extract Phone
    # -----------------------------
    def extract_phone(self):

        match = re.search(r'(\+91[\s-]?)?[6-9]\d{9}', self.pdf_text)

        if match:
            return Normalizer.normalize_phone(match.group())

        return None

    # -----------------------------
    # Extract Skills
    # -----------------------------
    def extract_skills(self):

        skill_list = [
            "Python",
            "Java",
            "JavaScript",
            "SQL",
            "Git",
            "React",
            "Node.js",
            "MongoDB",
            "PostgreSQL",
            "MySQL",
            "Spring Boot",
            "C#",
            "ASP.NET Core",
            "Power BI",
            "Pandas",
            "Machine Learning",
            "HTML",
            "CSS",
            "Bootstrap"
        ]

        found = []

        for skill in skill_list:

            if skill.lower() in self.pdf_text.lower():
                found.append(skill)

        csv_skills = Normalizer.normalize_skills(
            self.csv_data.get("Skills")
        )

        return list(set(found + csv_skills))

    # -----------------------------
    # Extract Education
    # -----------------------------
    def extract_education(self):

        education_keywords = [
            "B.Tech",
            "Bachelor",
            "M.Tech",
            "MCA",
            "BCA",
            "B.Sc",
            "MBA",
            "Computer Science",
            "Engineering"
        ]

        for line in self.pdf_text.split("\n"):

            for keyword in education_keywords:

                if keyword.lower() in line.lower():
                    return line.strip()

        return self.csv_data.get("Education")

    # -----------------------------
    # Extract Experience
    # -----------------------------
    def extract_experience(self):

        match = re.search(r'(\d+)\+?\s*(years|year)', self.pdf_text, re.IGNORECASE)

        if match:
            return match.group()

        return self.csv_data.get("ExperienceYears")

    # -----------------------------
    # Merge
    # -----------------------------
    def merge(self):

    # Extract data from PDF
        pdf_email = self.extract_email()
        pdf_phone = self.extract_phone()

        profile = {

            "candidate_id": self.csv_data.get("CandidateID"),

            "full_name": self.extract_name(),

            # Store extracted values (optional, useful for debugging)
            "pdf_email": pdf_email,

            "pdf_phone": pdf_phone,

            # Final merged values
            "emails": [
                pdf_email if pdf_email else self.csv_data.get("Email")
            ],

            "phones": [
                pdf_phone if pdf_phone else Normalizer.normalize_phone(
                    self.csv_data.get("Phone")
                )
            ],

            "skills": self.extract_skills(),

            "education": self.extract_education(),

            "experience": self.extract_experience(),

            # Recruiter Information (from CSV)
            "current_company": self.csv_data.get("Company"),

            "job_title": self.csv_data.get("JobTitle"),

            "location": Normalizer.normalize_location(
                self.csv_data.get("Location")
            ),

            "linkedin": self.csv_data.get("LinkedIn"),

            "github": self.csv_data.get("GitHub")
        }
        
        return profile
    


# ---------------------------------------
# Test
# ---------------------------------------

if __name__ == "__main__":

    sample_csv = {
        "CandidateID": "C001",
        "FullName": "John Doe",
        "Email": "john@gmail.com",
        "Phone": "9876543210",
        "Company": "TCS",
        "JobTitle": "Software Engineer",
        "Location": "Bangalore, India",
        "ExperienceYears": "3",
        "Skills": "Python;SQL",
        "Education": "B.Tech CSE",
        "LinkedIn": "https://linkedin.com/in/johndoe",
        "GitHub": "https://github.com/johndoe"
    }

    sample_pdf = """
    John Doe

    Email: john@gmail.com

    Phone: +91 9876543210

    B.Tech Computer Science

    Experience: 3 years

    Skills:
    Python
    Java
    SQL
    Git
    """

    merger = Merger(sample_csv, sample_pdf)

    result = merger.merge()

    from pprint import pprint
    pprint(result)