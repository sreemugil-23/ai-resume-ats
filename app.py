import streamlit as st
import nltk

from core.pdf_parser import extract_text_from_pdf
from core.preprocessing import preprocess_text
from core.similarity import calculate_similarity
from core.skills import extract_skills, calculate_skill_score
from core.ats_score import calculate_ats_score
from core.resume_evaluator import evaluate_resume_only
from config.roles import JOB_ROLE_SKILLS


# ------------------- APP CONFIG -------------------
st.set_page_config(
    page_title="ATS Resume Analyzer",
    layout="centered"
)

nltk.download("stopwords", quiet=True)


# ------------------- HEADER -------------------
st.title("ATS Resume Analyzer")
st.caption(
    "Simulates how Applicant Tracking Systems (ATS) evaluate resumes"
)
st.markdown("---")


# ------------------- STEP 1: UPLOAD RESUME -------------------
st.header("1. Upload Resume")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF format only)",
    type=["pdf"]
)

resume_text = ""

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)

    if resume_text.strip():
        st.success("Resume uploaded and parsed successfully.")
    else:
        st.error(
            "The resume text could not be extracted. "
            "This may be a scanned or image-based PDF."
        )

st.markdown("---")


# ------------------- STEP 2: CHOOSE EVALUATION METHOD -------------------
st.header("2. Choose Evaluation Method")

evaluation_mode = st.selectbox(
    "How should the resume be evaluated?",
    [
        "Resume ATS Readiness",
        "Resume vs Job Description",
        "Resume vs Job Title"
    ]
)


# ============================================================
# MODE 1 — RESUME ONLY (INDUSTRY-STANDARD ATS READINESS)
# ============================================================
if evaluation_mode == "Resume ATS Readiness" and uploaded_file and resume_text:

    cleaned_resume = preprocess_text(resume_text)
    score, feedback = evaluate_resume_only(
        raw_text=resume_text,
        cleaned_text=cleaned_resume
    )

    st.markdown("---")
    st.header("ATS Evaluation Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("ATS Resume Score", f"{score}/100")

    with col2:
        st.metric("Evaluation Type", "Resume Only")

    st.info(
        "This score reflects how ATS-friendly your resume is. "
        "It does NOT measure intelligence, talent, or job fit."
    )

    st.subheader("Why you got this score")

    if feedback.get("sections_found"):
        st.write(
            "✅ Sections detected:",
            ", ".join(feedback["sections_found"])
        )

    if feedback.get("keywords_matched"):
        st.write(
            "✅ Keywords detected:",
            ", ".join(feedback["keywords_matched"])
        )

    st.write("📄 Word count:", feedback.get("word_count", "N/A"))

    # Warnings
    if feedback.get("word_count", 0) < 250:
        st.warning(
            "Resume is quite short. ATS systems usually prefer more detail."
        )

    if not feedback.get("contact_detected"):
        st.error(
            "No contact information detected. "
            "ATS systems may reject such resumes."
        )

    with st.expander("How is this score calculated?"):
        st.markdown("""
        **Resume ATS Readiness Scoring**
        - Section structure (25%)
        - Keyword presence (25%)
        - Resume length (15%)
        - Skill density (15%)
        - Formatting simplicity (10%)
        - Contact information (10%)
        """)


# ============================================================
# MODE 2 — RESUME VS JOB DESCRIPTION
# ============================================================
elif evaluation_mode == "Resume vs Job Description":

    st.markdown("---")
    st.header("Job Description Input")

    job_text = st.text_area(
        "Paste the full job description",
        placeholder="Paste the job description here..."
    )

    if uploaded_file and resume_text and job_text:

        cleaned_resume = preprocess_text(resume_text)
        cleaned_job = preprocess_text(job_text)

        similarity = calculate_similarity(
            cleaned_resume, cleaned_job
        )

        ats_score = calculate_ats_score(
            similarity=similarity,
            skill_score=0
        )

        st.markdown("---")
        st.header("ATS Match Result")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("ATS Match Score", f"{ats_score}/100")

        with col2:
            st.metric("Evaluation Type", "Resume vs Job Description")

        st.info(
            "This score reflects how closely your resume matches "
            "the provided job description based on ATS-style similarity."
        )


# ============================================================
# MODE 3 — RESUME VS JOB TITLE
# ============================================================
elif evaluation_mode == "Resume vs Job Title":

    st.markdown("---")
    st.header("Job Title Selection")

    job_title = st.selectbox(
        "Select a job title",
        list(JOB_ROLE_SKILLS.keys())
    )

    if uploaded_file and resume_text:

        role_skills = JOB_ROLE_SKILLS[job_title]
        job_text = " ".join(role_skills)

        cleaned_resume = preprocess_text(resume_text)
        cleaned_job = preprocess_text(job_text)

        similarity = calculate_similarity(
            cleaned_resume, cleaned_job
        )

        matched_skills = extract_skills(
            cleaned_resume, role_skills
        )

        skill_score = calculate_skill_score(
            matched_skills,
            len(role_skills)
        )

        ats_score = calculate_ats_score(
            similarity, skill_score
        )

        st.markdown("---")
        st.header("ATS Match Result")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("ATS Match Score", f"{ats_score}/100")

        with col2:
            st.metric("Evaluation Type", "Resume vs Job Title")

        st.subheader("Matched Skills")
        if matched_skills:
            st.write(", ".join(matched_skills))
        else:
            st.warning("No core skills detected for this role.")

        st.info(
            "Job Title matching uses a predefined skill template, "
            "similar to how ATS systems approximate job requirements."
        )


# ------------------- FOOTER -------------------
st.markdown("---")
st.caption(
    "Built with Python, NLP, and ATS-style heuristics | "
    "Educational & demonstrative project"
)
