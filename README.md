# R3sum3OS: Ontology-Driven Resume Intelligence System

🚀 **Turning Raw Experience (Rocks) into Professional Assets (Diamonds).**

R3sum3OS is a deterministic resume optimization framework. It aligns candidate experience with industry-standard job ontologies, providing a transparent, non-generative way to bridge the gap between human talent and machine-readable requirements.

---

## 🛠️ Repository Architecture
* **`core/`**: The "Kernel" — Handles text normalization, weighted scoring, and schema validation.
* **`ontology/`**: The "Knowledge Base" — Role-specific JSON dictionaries (e.g., `data_scientist.json`).
* **`resumeos/`**: The "Logic Module" — Orchestrates the gap analysis and the "Diamond" rewriting engine.
* **`app.py`**: The "Command Center" — A polished Gradio dashboard for interactive use.
* **`tests/`**: The "Safety Net" — Automated test suite ensuring technical character preservation.

---

## ✨ The Diamond Polish Workflow
Unlike LLMs that "hallucinate" experience, R3sum3OS uses a **Deterministic Pipeline**:

1. **Extraction**: The `core/parser.py` preserves vital tech tokens like `C++`, `CI/CD`, and `Node.js`.
2. **Scrutiny**: Your resume is measured against weighted categories (Core Skills, Tools, Methodologies).
3. **Refinement**: The `rewriting.py` engine strips "weak" starts and injects high-impact action verbs.
4. **Export**: A conservative, ATS-optimized PDF is generated, free of formatting traps.



---

## 📦 Installation

```bash
pip install -r requirements.txt
python app.py
