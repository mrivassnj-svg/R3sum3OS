# ResumeOS (R3sum3OS)

ResumeOS (pronounced *re-soo-me-ohs*) is an open-source resume optimization system
designed for students and early-career professionals.

Its goal is simple:
help you align your resume with Applicant Tracking Systems (ATS) in a clear,
explainable, and reproducible way — without relying on black-box AI tools.

ResumeOS does not guess, hallucinate, or invent experience.
Every result is based on deterministic rules that you can inspect, understand,
and trust.

------------------------------------------------------------

## Why ResumeOS Exists

Many resume tools today:
- Automatically rewrite content without explanation
- Hide scoring logic
- Use large language models that may invent skills or experience

ResumeOS takes a different approach.

It focuses on:
- Transparency
- Control
- Repeatable results
- ATS compatibility

If you want to *understand* why your resume scores the way it does — not just
accept an output — ResumeOS is built for you.

------------------------------------------------------------

## Key Features

[+] ATS Keyword Normalization and Scoring  
ResumeOS scans the job description and your resume text to identify important
keywords commonly used by ATS software.

It calculates a match score based on how many relevant keywords overlap between
the job posting and your resume. This score is fully explainable and reproducible.

---

[+] Job-to-Resume Keyword Gap Analysis  
ResumeOS shows:
- Keywords found in both the job description and your resume
- Keywords that appear in the job description but are missing from your resume

This makes it easy to see what skills or terms you may need to add or clarify.

---

[+] Deterministic Bullet Rewriting with Action Verbs  
Raw experience text is rewritten into stronger resume bullets using a fixed list
of professional action verbs.

Important rules:
- No new experience is invented
- Meaning is preserved
- The same input always produces the same output

This improves clarity and professionalism without changing your story.

---

[+] Clean, Professional PDF Resume Export  
ResumeOS generates a simple, professional PDF resume that:
- Avoids tables, columns, icons, and graphics
- Is compatible with ATS scanners
- Works well for online applications and printing

The formatting is intentionally conservative to maximize compatibility.

---

[+] Interactive Web Interface (Gradio)  
ResumeOS includes a browser-based interface where you can:
- Enter resume information
- Paste a job description
- View an optimized resume preview
- See an ATS match score
- Download a PDF resume

No frontend or web development knowledge is required.

---

[+] Local, Colab, and Cloud-Friendly Execution  
ResumeOS can be run:
- Locally on your computer
- In Google Colab
- On cloud platforms

No paid APIs or external AI services are required.

------------------------------------------------------------

## System Architecture Overview

ResumeOS is intentionally modular and built as a clear processing pipeline:

User Input
    |
    v
Text Normalization and ATS Analysis
    |
    v
Bullet Rewrite Engine
    |
    v
HTML Resume Preview and ATS Score
    |
    v
PDF Export Engine
    |
    v
Downloadable Resume

Each stage is independent and can be modified or replaced without breaking the
entire system.

------------------------------------------------------------

## Module Breakdown (Plain English)

### 1. Text Normalization and ATS Analysis

Purpose:
Extract meaningful keywords from the job description and compare them to the
resume content.

What it does:
- Removes common stopwords that do not affect ATS scoring
- Extracts words that are at least three characters long
- Counts keyword matches and gaps

Outputs:
- ATS match percentage
- Matched keywords
- Missing (gap) keywords

This makes the scoring logic transparent and easy to understand.

------------------------------------------------------------

### 2. Bullet Rewrite Engine (ATS-Safe)

Purpose:
Improve resume bullet points without changing meaning or adding false content.

What it does:
- Removes weak starting words (e.g., "helped", "worked on")
- Prepends strong action verbs
- Preserves original experience content

Important:
This engine does not generate new ideas or fabricate experience.

------------------------------------------------------------

### 3. PDF Export Engine

Purpose:
Create a professional resume file that works with ATS systems.

What it does:
- Uses simple fonts and spacing
- Avoids layouts that break ATS parsing
- Generates a downloadable PDF file

The output is designed for real hiring systems, not visual flair.

------------------------------------------------------------

### 4. Orchestrator (System Controller)

Purpose:
Act as the central coordinator for the entire system.

What it does:
- Combines resume skills and experience
- Runs ATS analysis
- Generates rewritten bullets
- Builds the HTML preview
- Triggers PDF generation

This function is the single source of truth for ResumeOS execution.

------------------------------------------------------------

### 5. Frontend (Gradio Web Interface)

Purpose:
Provide an accessible interface for users.

Features:
- Text fields for resume and job description input
- Live ATS score display
- Resume preview
- One-click PDF download

The interface runs entirely in the browser.

------------------------------------------------------------

## Installation and Setup

### Prerequisites
- Python 3.9 or higher
- pip package manager

------------------------------------------------------------

### Install Dependencies

```bash
pip install -r requirements.txt
Run ResumeOS Locally
python app.py


After running the command, a local web interface will open in your browser.

### Who This Project Is For

- College students

- Recent graduates

- Career changers

- Educators teaching resume fundamentals

- Developers interested in explainable systems

---

***Design Philosophy***

ResumeOS is built around these principles:

Deterministic output over generative randomness

Explainability over mystery

Control over automation

ATS compatibility over visual complexity
