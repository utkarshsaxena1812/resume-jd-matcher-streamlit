import streamlit as st
from utils.parser import extract_text_from_pdf, clean_text_simple, calculate_similarity, missing_keywords

st.set_page_config(page_title="AI Resume-JD Matcher", page_icon="📄", layout="wide")
st.title("AI Resume – Job Description Matcher 🚀")

st.markdown("""
Welcome! This tool helps you match your resume with a job description.  

**Instructions:**  
1. Upload your **Resume PDF**.  
2. Paste or type the **Job Description**.  
3. Click **Run** to see the match score and missing keywords.
""")

# Streamlit columns for better layout
col1, col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
with col2:
    jd_text = st.text_area("Paste Job Description here")

# Process resume
if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)
    cleaned_resume = clean_text_simple(resume_text)
    st.success("Resume uploaded & processed!")

# Process job description
if jd_text:
    cleaned_jd = clean_text_simple(jd_text)

# Calculate similarity
if uploaded_file is not None and jd_text:
    score = calculate_similarity(cleaned_resume, cleaned_jd)
    st.subheader(f"Resume-JD Match Score: {score}%")
    
    missing = missing_keywords(cleaned_resume, cleaned_jd)
    st.subheader("Missing Keywords / Skills")
    st.write(missing[:50])
