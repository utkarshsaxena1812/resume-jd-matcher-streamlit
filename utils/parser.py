import PyPDF2
import re

def extract_text_from_pdf(file_path):
    """Extract raw text from PDF resume"""
    with open(file_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def clean_text_simple(text):
    """Basic text cleaning: lowercase and remove special characters"""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)  # keep only letters, numbers, spaces
    text = re.sub(r'\s+', ' ', text)  # replace multiple spaces with single space
    return text.strip()

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text, jd_text):
    """Calculate similarity score between resume and job description"""
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([resume_text, jd_text])
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(score * 100, 2)  # return percentage

def missing_keywords(resume_text, jd_text):
    """Find words in JD missing from resume"""
    resume_words = set(resume_text.split())
    jd_words = set(jd_text.split())
    missing = jd_words - resume_words
    return list(missing)

def extract_text_from_pdf(file):
    """Extract text from PDF file or Streamlit UploadedFile"""
    if hasattr(file, "read"):  # file is UploadedFile
        reader = PyPDF2.PdfReader(file)
    else:  # file is file path string
        with open(file, "rb") as f:
            reader = PyPDF2.PdfReader(f)
    
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
