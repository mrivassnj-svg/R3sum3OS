import gradio as gr
from resumeos.orchestrator import full_system_resolution

# Custom CSS to give it that 'Diamond' shine and clean UI
custom_css = """
body { background-color: #0f172a; }
.gradio-container { border-radius: 15px; }
.diamond-btn { 
    background: linear-gradient(45deg, #00d2ff 0%, #3a7bd5 100%) !important; 
    color: white !important; 
    border: none !important;
}
"""

def process_and_polish(name, email, school, degree, skills, experience, job_desc):
    # This calls our Orchestrator which now uses the perfected Scorer and Rewriter
    preview_html, pdf_path = full_system_resolution(
        name, email, school, degree, skills, experience, job_desc
    )
    return preview_html, pdf_path

with gr.Blocks(theme=gr.themes.Soft(), css=custom_css) as demo:
    gr.HTML("""
        <div style="text-align:center; padding: 20px;">
            <h1 style="color:#3b82f6; margin-bottom:0;">💎 R3sum3OS</h1>
            <p style="color:#64748b;">Turn your raw experience into a polished professional asset.</p>
        </div>
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 🪨 The Raw Material (Input)")
            name = gr.Textbox(label="Full Name", placeholder="John Doe")
            email = gr.Textbox(label="Email Address")
            with gr.Row():
                school = gr.Textbox(label="University")
                degree = gr.Textbox(label="Degree/Major")
            
            skills = gr.Textbox(label="Skills (Comma separated)", lines=3)
            experience = gr.Textbox(label="Raw Experience Bullets", lines=5, placeholder="I did some python and helped the team...")
            job_desc = gr.Textbox(label="Target Job Description", lines=5)
            
            submit_btn = gr.Button("Polish to Diamond 💎", variant="primary", elem_classes="diamond-btn")

        with gr.Column(scale=1):
            gr.Markdown("### ✨ The Polished Result")
            output_html = gr.HTML(label="Resume Preview")
            output_file = gr.File(label="Download Polished PDF")

    submit_btn.click(
        fn=process_and_polish,
        inputs=[name, email, school, degree, skills, experience, job_desc],
        outputs=[output_html, output_file]
    )

if __name__ == "__main__":
    demo.launch()
