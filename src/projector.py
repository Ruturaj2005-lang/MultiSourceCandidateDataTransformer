import json


class Projector:

    def __init__(self, config_path):
        self.config_path = config_path

    def load_config(self):
        with open(self.config_path, "r") as file:
            return json.load(file)

    def project(self, merged_profile, confidence):

        config = self.load_config()

        result = {}

        fields = config.get("fields", [])

        rename = config.get("rename", {})

        missing = config.get("on_missing", "null")

        for field in fields:

            value = merged_profile.get(field)

            if value is None:

                if missing == "omit":
                    continue

                if missing == "error":
                    raise ValueError(f"{field} is missing")

            output_name = rename.get(field, field)

            result[output_name] = value

        

        if config.get("include_confidence"):

            result["confidence"] = confidence

        return result