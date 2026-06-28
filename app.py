import re
import streamlit as st
from dotenv import load_dotenv
from pdf_reader import extract_text_from_pdf
from analyzer import analyze_resume, match_resume_to_job, generate_cover_letter

load_dotenv()

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

def extract_score(text):
    match = re.search(r"(\d{1,3})\s*/?\s*100", text)
    if match:
        return min(int(match.group(1)), 100)
    return None

st.sidebar.title("🤖 AI Resume Analyzer")
st.sidebar.write("Upload a resume and optionally paste a job description.")

uploaded_file = st.sidebar.file_uploader("Upload Resume PDF", type="pdf")
job_description = st.sidebar.text_area("Paste Job Description Optional", height=250)

st.title("🤖 AI Resume Analyzer")
st.write("Analyze your resume, compare it to a job description, and generate a cover letter.")

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if "report" not in st.session_state:
    st.session_state.report = ""

if "job_report" not in st.session_state:
    st.session_state.job_report = ""

if "cover_letter" not in st.session_state:
    st.session_state.cover_letter = ""

if uploaded_file:
    st.session_state.resume_text = extract_text_from_pdf(uploaded_file)
    st.success("Resume uploaded successfully!")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Analyze Resume"):
        if not st.session_state.resume_text:
            st.warning("Please upload a resume first.")
        else:
            with st.spinner("Analyzing resume..."):
                st.session_state.report = analyze_resume(st.session_state.resume_text)

with col2:
    if st.button("Compare to Job"):
        if not st.session_state.resume_text:
            st.warning("Please upload a resume first.")
        elif not job_description:
            st.warning("Please paste a job description first.")
        else:
            with st.spinner("Comparing resume to job description..."):
                st.session_state.job_report = match_resume_to_job(
                    st.session_state.resume_text,
                    job_description
                )

with col3:
    if st.button("Generate Cover Letter"):
        if not st.session_state.resume_text:
            st.warning("Please upload a resume first.")
        elif not job_description:
            st.warning("Please paste a job description first.")
        else:
            with st.spinner("Writing cover letter..."):
                st.session_state.cover_letter = generate_cover_letter(
                    st.session_state.resume_text,
                    job_description
                )

if st.session_state.report:
    st.divider()
    st.header("📄 Resume Analysis Report")

    score = extract_score(st.session_state.report)
    if score is not None:
        st.metric("ATS Score", f"{score}/100")

    with st.expander("View Full Resume Report", expanded=True):
        st.write(st.session_state.report)

    st.download_button(
        "Download Resume Report",
        st.session_state.report,
        file_name="resume_analysis_report.txt",
        mime="text/plain"
    )

if st.session_state.job_report:
    st.divider()
    st.header("🎯 Job Match Report")

    match_score = extract_score(st.session_state.job_report)
    if match_score is not None:
        st.metric("Job Match Score", f"{match_score}/100")

    with st.expander("View Full Job Match Report", expanded=True):
        st.write(st.session_state.job_report)

    st.download_button(
        "Download Job Match Report",
        st.session_state.job_report,
        file_name="job_match_report.txt",
        mime="text/plain"
    )

if st.session_state.cover_letter:
    st.divider()
    st.header("✉️ Cover Letter")

    st.write(st.session_state.cover_letter)

    st.download_button(
        "Download Cover Letter",
        st.session_state.cover_letter,
        file_name="cover_letter.txt",
        mime="text/plain"
    )