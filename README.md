# R3sum3OS: Ontology-Driven Resume Intelligence System

🚀 **Bridging the gap between candidate data and industry-standard job ontologies.**

R3sum3OS is an intelligent resume optimization framework that utilizes "system resolution" to align experience with job requirements. Unlike traditional keyword scanners, this system performs semantic alignment of skills and experience without the "black box" randomness of Generative AI.

---

## 🛠️ Repository Architecture
* **`core/parser.py`**: The semantic engine that extracts and normalizes resume data.
* **`ontology/`**: Role-specific JSON schemas (e.g., `software_engineer.json`) for system resolution.
* **`resumeos/`**: The main logic module handling full system resolution and score mapping.
* **`app.py`**: A Gradio-powered web interface for interactive processing.
* **`tests/`**: Automated validation suite ensuring parser reliability via `test_parser.py`.

---

## 💡 Why R3sum3OS Exists
Many modern resume tools rewrite content without explanation or use LLMs that "invent" experience. R3sum3OS is built for:
* **Transparency**: Understand *why* you score the way you do.
* **Control**: You maintain the narrative; the system handles the optimization.
* **Determinism**: The same input always produces the same high-quality output.
* **ATS Compatibility**: Engineered for machine-readability first.

---

## ✨ Key Features

### [+] ATS Keyword Normalization & Scoring
Scans job descriptions and resume text to identify critical overlaps. It calculates a match score that is fully explainable and reproducible.

### [+] Job-to-Resume Gap Analysis
Identifies exactly what is missing. The system highlights "Matched Keywords" vs. "Missing Gaps," giving you a clear roadmap for manual adjustments.

### [+] Deterministic Bullet Rewriting
Raw experience is transformed using a fixed list of professional action verbs. 
* **Rule 1**: No new experience is invented.
* **Rule 2**: Meaning is preserved.
* **Rule 3**: ATS-friendly action verbs are prioritized.

### [+] Clean PDF Export
Generates a conservative, high-compatibility PDF. It avoids tables, columns, and icons that typically break ATS scanners.



---

## 📐 System Architecture Overview
R3sum3OS is a modular processing pipeline:

1. **User Input** (Resume + Job Description)
2. **Text Normalization** (Stopword removal & tokenization)
3. **Bullet Rewrite Engine** (Action verb integration)
4. **HTML Preview** (Real-time ATS score calculation)
5. **PDF Export** (Final document generation via fpdf2)

---

## 📦 Installation and Setup

### Prerequisites
* Python 3.9 or higher
* pip package manager

### Setup
```bash
# Clone the repository
git clone [https://github.com/mrivassnj-svg/R3sum3OS.git](https://github.com/mrivassnj-svg/R3sum3OS.git)

# Install Dependencies
pip install -r requirements.txt

# Run Locally
python app.py
