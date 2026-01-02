from resumeos.analysis import ats_analysis
from resumeos.rewriting import rewrite_bullets
from resumeos.pdf_export import export_to_pdf

def full_system_resolution(
    name, email, school, degree, skills, experience, job_desc
):
    combined_profile = f"{skills} {experience}"

    bullets = rewrite_bullets(experience)
    score, matched, missing = ats_analysis(job_desc, combined_profile)

    matched_list = ", ".join(sorted(matched.keys())[:10])
    missing_list = ", ".join(sorted(missing.keys())[:10])

    bullet_html = "".join(
        f"<li style='margin-bottom:8px;'>{b}</li>" for b in bullets
    )

    preview_html = f"""
    <div style="background:#f8fafc;padding:20px;font-family:sans-serif;">
      <div style="background:white;padding:30px;border-radius:10px;
                  max-width:800px;margin:auto;box-shadow:0 4px 12px rgba(0,0,0,.08)">
        <h1>{name}</h1>
        <p>{email} | {school}</p>
        <p><strong>{degree}</strong></p>
        <p><strong>ATS Match:</strong> {score}%</p>

        <h3>Experience</h3>
        <ul>{bullet_html}</ul>

        <p><strong>Matched:</strong> {matched_list or "None"}</p>
        <p><strong>Missing:</strong> {missing_list or "None 🎉"}</p>
      </div>
    </div>
    """

    pdf_path = export_to_pdf(
        name, email, school, degree, skills, bullets
    )

    return preview_html, pdf_path
