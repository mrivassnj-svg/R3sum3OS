import gradio as gr
from core.ontology import load_ontology
from core.scorer import calculate_weighted_ats_score
from core.parser import normalize_text

def analyze_resume(resume: str, job_desc: str, role: str = "software_engineer") -> str:
    # 1. Normalize both inputs
    resume_tokens = normalize_text(resume)
    jd_tokens = normalize_text(job_desc)

    # 2. Load the specific role ontology
    ontology = load_ontology(role)

    # 3. Calculate the score using your engine
    score = calculate_weighted_ats_score(
        resume_tokens,
        jd_tokens,
        ontology
    )

    # 4. Return the visual "Dashboard"
    return f"""
╔══════════════════════════════════════════╗
║        ATS WEIGHTED ANALYSIS             ║
╠══════════════════════════════════════════╣
║  ROLE: {role.upper()}                      ║
║  WEIGHTED SCORE: {score}%                  ║
╚══════════════════════════════════════════╝
"""

# --- GRADIO INTERFACE SETUP ---

demo = gr.Interface(
    fn=analyze_resume,
    inputs=[
        gr.Textbox(label="Paste Your Resume Content", lines=10),
        gr.Textbox(label="Paste Job Description", lines=10),
        gr.Dropdown(
            choices=["software_engineer", "data_scientist", "product_manager"], 
            label="Target Role", 
            value="software_engineer"
        )
    ],
    outputs=gr.Textbox(label="System Resolution Output", interactive=False),
    title="R3sum3OS | Ontology-Driven System Resolution",
    description="Align your professional experience with industry-standard job ontologies."
)

if __name__ == "__main__":
    demo.launch()
