import json


class Projector:

    def __init__(self, config_path):
        self.config_path = config_path

    def load_config(self):
        with open(self.config_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def split_location(self, location):

        city = None
        region = None
        country = None

        if location:

            parts = [x.strip() for x in location.split(",")]

            if len(parts) > 0:
                city = parts[0]

            if len(parts) > 1:
                region = parts[1]

            if len(parts) > 2:
                country = parts[2]

        return {
            "city": city,
            "region": region,
            "country": country
        }

    def project(self, merged_profile, confidence):

        config = self.load_config()

        missing = config.get("on_missing", "null")

        result = {}

        # ---------------------------------
        # Candidate ID
        # ---------------------------------

        result["candidate_id"] = merged_profile.get("candidate_id")

        # ---------------------------------
        # Name
        # ---------------------------------

        result["full_name"] = merged_profile.get("full_name")

        # ---------------------------------
        # Emails
        # ---------------------------------

        emails = merged_profile.get("emails")

        if emails is None:
            emails = []

        result["emails"] = emails

        # ---------------------------------
        # Phones
        # ---------------------------------

        phones = merged_profile.get("phones")

        if phones is None:
            phones = []

        result["phones"] = phones

        # ---------------------------------
        # Location
        # ---------------------------------

        result["location"] = self.split_location(
            merged_profile.get("location")
        )

        # ---------------------------------
        # Links
        # ---------------------------------

        result["links"] = {

            "linkedin": merged_profile.get("linkedin"),

            "github": merged_profile.get("github"),

            "portfolio": None,

            "other": []

        }

        # ---------------------------------
        # Headline
        # ---------------------------------

        result["headline"] = merged_profile.get("job_title")

        # ---------------------------------
        # Years Experience
        # ---------------------------------

        exp = merged_profile.get("experience")

        try:
            years = int(str(exp).split()[0])
        except:
            years = None

        result["years_experience"] = years

        # ---------------------------------
        # Skills
        # ---------------------------------

        result["skills"] = []

        for skill in merged_profile.get("skills", []):

            result["skills"].append({

                "name": skill,

                "confidence": 1.0,

                "sources": [
                    "resume.pdf",
                    "recruiter.csv"
                ]

            })

        # ---------------------------------
        # Experience
        # ---------------------------------

        result["experience"] = [

            {

                "company": merged_profile.get("current_company"),

                "title": merged_profile.get("job_title"),

                "start": None,

                "end": None,

                "summary": None

            }

        ]

        # ---------------------------------
        # Education
        # ---------------------------------

        result["education"] = [

            {

                "institution": None,

                "degree": merged_profile.get("education"),

                "field": None,

                "end_year": None

            }

        ]

        # ---------------------------------
        # Provenance
        # ---------------------------------

        if config.get("include_provenance", False):

            provenance = []

            for field, info in merged_profile.get("provenance", {}).items():

                provenance.append({

                    "field": field,

                    "source": info.get("source"),

                    "method": info.get("method")

                })

            result["provenance"] = provenance

        # ---------------------------------
        # Overall Confidence
        # ---------------------------------

        if config.get("include_confidence", False):

            result["overall_confidence"] = confidence.get(
                "overall_confidence",
                0
            )

        # ---------------------------------
        # Handle Missing Values
        # ---------------------------------

        if missing == "omit":

            result = {

                k: v for k, v in result.items()

                if v is not None and v != []

            }

        elif missing == "error":

            for key, value in result.items():

                if value is None:

                    raise ValueError(f"{key} is missing")



        if config.get("include_confidence", False):
            result["confidence"] = confidence

        if config.get("include_provenance", False):
            result["provenance"] = merged_profile.get("provenance")

        return result