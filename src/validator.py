import re

class Validator:

    @staticmethod
    def validate(profile):

        errors = []

        if not profile.get("full_name"):
            errors.append("Full Name Missing")

        emails = profile.get("emails", [])

        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        for email in emails:
            if not re.match(email_pattern, email):
                errors.append("Invalid Email")

        phones = profile.get("phones", [])

        for phone in phones:

            if phone is None:
                errors.append("Invalid Phone")

        if errors:
            return False, errors

        return True, []


if __name__ == "__main__":

    sample = {

        "full_name": "John Doe",

        "emails": ["john@gmail.com"],

        "phones": ["+919876543210"]

    }

    print(Validator.validate(sample))