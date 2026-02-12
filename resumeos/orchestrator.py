from resumeos.analysis import ats_analysis # Matches the renamed function
from resumeos.rewriting import rewrite_bullets
from resumeos.pdf_export import export_to_pdf

def full_system_resolution(
    name, email, school, degree, skills, experience, job_desc
):
    combined_profile = f"{skills} {experience}"

    # Transform the experience bullets
    bullets = rewrite_bullets(experience)
    
    # Run the keyword gap analysis
    score, matched, missing = ats_analysis(job_desc, combined_profile)

    # Pick a color based on the score (Green for >= 70, Yellow for >= 40, Red for < 40)
    score_color = "#22c55e" if score >= 70 else "#eab308" if score >= 40 else "#ef4444"

    # Convert dictionaries to clean lists
    matched_list = ", ".join(list(matched.keys())[:12])
    missing_list = ", ".join(list(missing.keys())[:12])

    bullet_html = "".join(f"<li style='margin-bottom:8px;'>{b}</li>" for b in bullets)

    preview_html = f"""
    <div style="background:#f1f5f9; padding:20px; font-family:sans-serif;">
      <div style="background:white; padding:30px; border-radius:12px; max-width:800px; margin:auto; border: 1px solid #e2e8f0;">
        <h1 style="margin:0; color:#1e293b;">{name}</h1>
        <p style="color:#64748b; margin:5px 0;">{email} | {school}</p>
        <p><strong>{degree}</strong></p>
        
        <div style="display:inline-block; padding:10px 20px; border-radius:8px; background:{score_color}; color:white; font-weight:bold; margin:15px 0;">
            ATS Match Score: {score}%
        </div>

        <h3 style="border-bottom:2px solid #f1f5f9; padding-bottom:5px;">Refined Experience</h3>
        <ul style="color:#334155;">{bullet_html}</ul>

        <div style="background:#f8fafc; padding:15px; border-radius:8px; margin-top:20px;">
            <p><strong>✅ Top Matches:</strong> <span style="color:#16a34a;">{matched_list or "None"}</span></p>
            <p><strong>⚠️ Key Gaps:</strong> <span style="color:#dc2626;">{missing_list or "None - Perfect Match! 🎉"}</span></p>
        </div>
      </div>
    </div>
    """

    pdf_path, success_flag = export_to_pdf(name, email, school, degree, skills, bullets)

    return preview_html, pdf_path
