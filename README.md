# 📄 Multi-Source Candidate Data Transformer

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![JSON](https://img.shields.io/badge/Output-JSON-green)
![CSV](https://img.shields.io/badge/Input-CSV-orange)
![PDF](https://img.shields.io/badge/Input-PDF-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Overview

The **Multi-Source Candidate Data Transformer** is a Python-based application that consolidates candidate information from **Recruiter CSV files** and **Resume PDF documents** into a standardized **Canonical JSON Profile**.

The system extracts information from resumes, matches the correct recruiter record, normalizes data, merges information, calculates a confidence score, tracks provenance, validates the final output, and generates configurable JSON based on runtime configuration.

---

## ✨ Features

- 📂 Read recruiter information from CSV
- 📄 Extract candidate details from PDF resumes
- 🔍 Candidate matching using:
  - Email
  - Phone Number
  - Full Name
- 🔄 Merge recruiter and resume information
- 📱 Normalize phone numbers (E.164)
- 📧 Normalize emails
- 🛠 Normalize skills and locations
- ✅ Validate mandatory fields
- 📊 Dynamic confidence score calculation
- 📜 Provenance tracking
- ⚙ Configurable JSON output
- 🧩 Modular architecture

---

## 📁 Project Structure

```text
MultiSourceCandidateDataTransformer/
│
├── config/
│   ├── default.json
│   └── custom.json
│
├── input/
│   ├── recruiter.csv
│   └── resume.pdf
│
├── output/
│   └── result.json
│
├── src/
│   ├── csv_reader.py
│   ├── pdf_reader.py
│   ├── normalizer.py
│   ├── merger.py
│   ├── confidence.py
│   ├── projector.py
│   ├── validator.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🏗 System Workflow

```text
Recruiter CSV        Resume PDF
      │                  │
      ▼                  ▼
 Read Recruiter      Extract Resume
      │                  │
      └───────┬──────────┘
              ▼
      Candidate Matching
 (Email → Phone → Name)
              │
              ▼
      Data Normalization
              │
              ▼
        Merge Records
              │
              ▼
   Confidence Calculation
              │
              ▼
     Provenance Tracking
              │
              ▼
      Projection Layer
              │
              ▼
     Output Validation
              │
              ▼
      Canonical JSON
```

---

# 📥 Input

## Recruiter CSV

Contains recruiter-provided candidate information:

- Candidate ID
- Full Name
- Email
- Phone
- Skills
- Company
- Job Title
- Experience
- Location
- LinkedIn
- GitHub

---

## Resume PDF

Extracted candidate information:

- Full Name
- Email
- Phone Number
- Skills
- Education
- Experience

---

# 📤 Output Schema

```json
{
  "candidate_id": "C001",
  "full_name": "John Doe",
  "emails": [
    "john@gmail.com"
  ],
  "phones": [
    "+919876543210"
  ],
  "location": {
    "city": "Bangalore",
    "region": "Karnataka",
    "country": "IN"
  },
  "links": {
    "linkedin": "...",
    "github": "...",
    "portfolio": null,
    "other": []
  },
  "headline": "Software Engineer",
  "years_experience": 3,
  "skills": [
    {
      "name": "Python",
      "confidence": 1.0,
      "sources": [
        "resume.pdf",
        "recruiter.csv"
      ]
    }
  ],
  "experience": [
    {
      "company": "Infosys",
      "title": "Software Engineer"
    }
  ],
  "education": [
    {
      "degree": "B.Tech Computer Science"
    }
  ],
  "provenance": [
    {
      "field": "full_name",
      "source": "resume.pdf",
      "method": "Regex Extraction"
    }
  ],
  "overall_confidence": 0.95
}
```

---

# ⚙ Runtime Configuration

The application supports configurable output using JSON.

Supported options include:

- Select output fields
- Rename fields
- Toggle confidence ON/OFF
- Toggle provenance ON/OFF
- Missing value handling
  - null
  - omit
  - error

Example:

```json
{
  "include_confidence": true,
  "include_provenance": true,
  "on_missing": "null"
}
```

---

# 📊 Confidence Calculation

| Condition | Score |
|------------|-------|
| Email Match | +0.40 |
| Phone Match | +0.30 |
| Name Match | +0.20 |
| Skills Match | +0.10 |

**Maximum Score = 1.00**

---

# 📜 Provenance

Every field stores information about:

- Source (CSV or Resume PDF)
- Extraction Method

Example:

```json
{
  "field": "emails",
  "source": "resume.pdf",
  "method": "Regex Extraction"
}
```

---

# 🛠 Technologies Used

- Python 3
- pdfplumber
- phonenumbers
- Regular Expressions (Regex)
- JSON
- CSV

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/MultiSourceCandidateDataTransformer.git
```

Navigate to the project

```bash
cd MultiSourceCandidateDataTransformer
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

```bash
python src/main.py
```

The generated output will be available at:

```text
output/result.json
```

---

# 📦 Modules

| Module | Purpose |
|----------|----------|
| csv_reader.py | Reads recruiter CSV data |
| pdf_reader.py | Extracts text from PDF resumes |
| merger.py | Matches and merges candidate data |
| normalizer.py | Standardizes phone numbers, skills, and locations |
| confidence.py | Calculates confidence score |
| projector.py | Projects configurable output |
| validator.py | Validates output schema |
| main.py | Executes the complete workflow |

---

# ⚠ Edge Cases Handled

- Missing Email
- Missing Phone
- Invalid Phone Number
- Duplicate Skills
- Candidate Not Found
- Missing Values
- Configurable Missing Value Strategy

---

