import streamlit as st
from main import JobApplicationAssistant
from htmlTemplate import web_styles
import os

def main():
    web_styles()

    with st.sidebar:
        st.header("☰ Menu")
        uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

    job_posting_url = st.chat_input("Enter the job posting URL")

    if uploaded_file and job_posting_url:
        # Save uploaded resume to a temporary file
        pdf_path = os.path.join("temp_resume.pdf")
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Create an instance of JobApplicationAssistant
        assistant = JobApplicationAssistant(pdf_path, job_posting_url)
        
        resume_data = assistant.extract_resume_data()
        job_description = assistant.extract_job_posting_data()
        
        email_content = assistant.generate_cold_email(job_description, resume_data)
        st.write(email_content)

    
if __name__ == "__main__":
    main()
