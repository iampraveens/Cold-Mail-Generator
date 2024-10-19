import os
import tempfile
import streamlit as st
from main import JobApplicationAssistant
from html_template import web_styles

def main():
    """
    Main entry point for the Streamlit app.

    Uploads a resume PDF file from the user, extracts relevant information using the
    JobApplicationAssistant class, and generates a cold email based on a job posting URL
    also provided by the user.

    :return: None
    """
    web_styles()

    with st.sidebar:
        st.header("☰ Menu")
        uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

    job_posting_url = st.chat_input("Enter the job posting URL")

    if uploaded_file and job_posting_url:
        # Save uploaded resume to a temporary file
        # pdf_path = os.path.join("temp_resume.pdf")
        # with open(pdf_path, "wb") as f:
        #     f.write(uploaded_file.getbuffer())

        # Create an instance of JobApplicationAssistant
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                temp_file.write(uploaded_file.getbuffer())
                temp_pdf_path = temp_file.name
                
            assistant = JobApplicationAssistant(temp_pdf_path, job_posting_url)
            
            resume_data = assistant.extract_resume_data()
            job_description = assistant.extract_job_posting_data()
            
            email_content = assistant.generate_cold_email(job_description, resume_data)
            st.write(email_content)
        except Exception as e:
            st.error(f"An error occurred: {e}")
            
        finally:
            # Delete the temporary file after processing
            if os.path.exists(temp_pdf_path):
                os.remove(temp_pdf_path)

    
if __name__ == "__main__":
    main()
