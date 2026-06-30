import phonenumbers


class Normalizer:

    # -----------------------------
    # Name
    # -----------------------------
    @staticmethod
    def normalize_name(name):

        if not name:
            return None

        return " ".join(word.capitalize() for word in name.strip().split())

    # -----------------------------
    # Email
    # -----------------------------
    @staticmethod
    def normalize_email(email):

        if not email:
            return None

        return email.strip().lower()

    # -----------------------------
    # Phone
    # -----------------------------
    @staticmethod
    def normalize_phone(phone):

        if not phone:
            return None

        try:
            phone = str(phone).strip()

            parsed = phonenumbers.parse(phone, "IN")

            if phonenumbers.is_valid_number(parsed):
                return phonenumbers.format_number(
                    parsed,
                    phonenumbers.PhoneNumberFormat.E164
                )

        except Exception:
            pass

        return None

    # -----------------------------
    # Skills
    # -----------------------------
    @staticmethod
    def normalize_skills(skills):

        if not skills:
            return []

        skill_map = {

    # ---------------- Programming Languages ----------------
    "python": "Python",
    "py": "Python",

    "java": "Java",

    "c": "C",

    "c++": "C++",
    "cpp": "C++",

    "c#": "C#",

    "javascript": "JavaScript",
    "js": "JavaScript",

    "typescript": "TypeScript",
    "ts": "TypeScript",

    "go": "Go",
    "golang": "Go",

    "ruby": "Ruby",

    "php": "PHP",

    "kotlin": "Kotlin",

    "swift": "Swift",

    "r": "R",

    "scala": "Scala",

    "dart": "Dart",

    # ---------------- Web Technologies ----------------
    "html": "HTML",

    "html5": "HTML5",

    "css": "CSS",

    "css3": "CSS3",

    "bootstrap": "Bootstrap",

    "tailwind": "Tailwind CSS",
    "tailwind css": "Tailwind CSS",

    "sass": "SASS",

    "jquery": "jQuery",

    # ---------------- Frontend Frameworks ----------------
    "react": "React",

    "reactjs": "React",

    "react.js": "React",

    "angular": "Angular",

    "vue": "Vue.js",

    "vuejs": "Vue.js",

    "nextjs": "Next.js",

    "next.js": "Next.js",

    "nuxt": "Nuxt.js",

    # ---------------- Backend Frameworks ----------------
    "node": "Node.js",

    "nodejs": "Node.js",

    "node.js": "Node.js",

    "express": "Express.js",

    "expressjs": "Express.js",

    "django": "Django",

    "flask": "Flask",

    "fastapi": "FastAPI",

    "spring": "Spring Boot",

    "spring boot": "Spring Boot",

    "hibernate": "Hibernate",

    "asp.net": "ASP.NET Core",

    "asp.net core": "ASP.NET Core",

    "laravel": "Laravel",

    # ---------------- Databases ----------------
    "sql": "SQL",

    "mysql": "MySQL",

    "postgresql": "PostgreSQL",

    "postgres": "PostgreSQL",

    "sqlite": "SQLite",

    "mongodb": "MongoDB",

    "oracle": "Oracle",

    "oracle db": "Oracle",

    "redis": "Redis",

    "firebase": "Firebase",

    # ---------------- Cloud ----------------
    "aws": "AWS",

    "amazon web services": "AWS",

    "azure": "Microsoft Azure",

    "gcp": "Google Cloud",

    "google cloud": "Google Cloud",

    "docker": "Docker",

    "kubernetes": "Kubernetes",

    # ---------------- DevOps ----------------
    "git": "Git",

    "github": "GitHub",

    "gitlab": "GitLab",

    "jenkins": "Jenkins",

    "terraform": "Terraform",

    "ansible": "Ansible",

    "linux": "Linux",

    # ---------------- Data Science ----------------
    "numpy": "NumPy",

    "pandas": "Pandas",

    "matplotlib": "Matplotlib",

    "seaborn": "Seaborn",

    "scikit-learn": "Scikit-learn",

    "sklearn": "Scikit-learn",

    "tensorflow": "TensorFlow",

    "keras": "Keras",

    "pytorch": "PyTorch",

    "opencv": "OpenCV",

    "machine learning": "Machine Learning",

    "deep learning": "Deep Learning",

    "artificial intelligence": "Artificial Intelligence",

    "ai": "Artificial Intelligence",

    "nlp": "Natural Language Processing",

    "computer vision": "Computer Vision",

    # ---------------- BI ----------------
    "power bi": "Power BI",

    "tableau": "Tableau",

    "excel": "Microsoft Excel",

    # ---------------- Mobile ----------------
    "android": "Android",

    "android studio": "Android Studio",

    "flutter": "Flutter",

    "react native": "React Native",

    # ---------------- Testing ----------------
    "selenium": "Selenium",

    "junit": "JUnit",

    "pytest": "PyTest",

    "postman": "Postman",

    # ---------------- Others ----------------
    "rest": "REST API",

    "rest api": "REST API",

    "graphql": "GraphQL",

    "microservices": "Microservices",

    "oauth": "OAuth",

    "jwt": "JWT",

    "agile": "Agile",

    "scrum": "Scrum",

    "jira": "Jira",

    "figma": "Figma",

    "canva": "Canva",

    "adobe xd": "Adobe XD",

    "ui/ux": "UI/UX",

    "ui ux": "UI/UX",

    "blockchain": "Blockchain",

    "solidity": "Solidity",

    "ethereum": "Ethereum",

    "web3": "Web3"
}

        normalized = []

        if isinstance(skills, str):
            skills = skills.replace(",", ";").split(";")

        for skill in skills:

            skill = skill.strip()

            if not skill:
                continue

            canonical = skill_map.get(skill.lower(), skill.title())

            if canonical not in normalized:
                normalized.append(canonical)

        return normalized

    # -----------------------------
    # Location
    # -----------------------------
    @staticmethod
    def normalize_location(location):

        if not location:
            return None

        return location.strip().title()

    # -----------------------------
    # Experience
    # -----------------------------
    @staticmethod
    def normalize_experience(exp):

        if not exp:
            return None

        exp = str(exp).strip().lower()

        exp = exp.replace("years", "Year")
        exp = exp.replace("year", "Year")
        exp = exp.replace("yrs", "Year")
        exp = exp.replace("yr", "Year")

        return exp

    # -----------------------------
    # Education
    # -----------------------------
    @staticmethod
    def normalize_education(education):

        if not education:
            return None

        return education.strip()


# ------------------------------------
# Test
# ------------------------------------
if __name__ == "__main__":

    print("Name:")
    print(Normalizer.normalize_name("ruturaj   padhy"))

    print("\nEmail:")
    print(Normalizer.normalize_email("Ruturaj@Gmail.COM"))

    print("\nPhone:")
    print(Normalizer.normalize_phone("9876543210"))

    print("\nSkills:")
    print(Normalizer.normalize_skills("python, js, sql, react, python"))

    print("\nLocation:")
    print(Normalizer.normalize_location("bangalore, india"))

    print("\nExperience:")
    print(Normalizer.normalize_experience("3 years"))

    print("\nEducation:")
    print(Normalizer.normalize_education(" B.Tech Computer Science "))