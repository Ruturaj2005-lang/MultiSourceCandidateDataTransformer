class Confidence:

    @staticmethod
    def calculate(profile, csv_data):

        score = 0

        # -------------------
        # Email Match
        # -------------------
        if profile.get("email"):
            if profile["email"].lower() == csv_data.get("Email", "").lower():
                score += 30

        # -------------------
        # Phone Match
        # -------------------
        if profile.get("phone"):
            if profile["phone"] == csv_data.get("Phone"):
                score += 25

        # -------------------
        # Name Match
        # -------------------
        if profile.get("full_name"):
            if profile["full_name"].lower() == csv_data.get("FullName", "").lower():
                score += 20

        # -------------------
        # Skills
        # -------------------
        if profile.get("skills"):
            score += 15

        # -------------------
        # Education
        # -------------------
        if profile.get("education"):
            score += 5

        # -------------------
        # Experience
        # -------------------
        if profile.get("experience"):
            score += 5

        return {
            "overall_confidence": round(score / 100, 2)
        }

if __name__ == "__main__":

    merged_profile = {
        "email": "john@gmail.com",
        "phone": "+919876543210",
        "full_name": "John Doe",
        "skills": ["Python", "Java", "SQL", "Git"],
        "experience": "3 years",
        "education": "B.Tech"
    }

    csv_data = {
        "Email": "john@gmail.com",
        "Phone": "9876543210",
        "FullName": "John Doe"
    }

    result = Confidence.calculate(merged_profile, csv_data)

    print(result)