from pdf_handler import PDFHandler
from web_handler import WebHandler
from prompt_chains import PromptChain
from utils.logger import logger

class JobApplicationAssistant:
    def __init__(self, pdf_path, job_posting_url):
        try:
            self.pdf_handler = PDFHandler(pdf_path)
            self.web_handler = WebHandler(job_posting_url)
            self.prompt_chain = PromptChain()
            logger.info("JobApplicationAssistant initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing JobApplicationAssistant: {e}")
            raise

    def extract_resume_data(self):
        try:
            pages = self.pdf_handler.get_pdf_text()
            chunks = self.pdf_handler.get_text_chunks()
            pdf_text = self.pdf_handler.get_all_text()
            resume_data = self.prompt_chain.get_pdf_chain(pdf_text)
            logger.info("Resume data extracted successfully.")
            return resume_data
        except Exception as e:
            logger.error(f"Error extracting resume data: {e}")
            raise

    def extract_job_posting_data(self):
        try:
            web_text = self.web_handler.get_web_text()
            job_description = self.prompt_chain.get_web_chain(web_text)
            logger.info("Job posting data extracted successfully.")
            return job_description
        except Exception as e:
            logger.error(f"Error extracting job posting data: {e}")
            raise

    def generate_cold_email(self, job_description, resume_data):
        try:
            email_content = self.prompt_chain.get_email_chain(job_description, resume_data)
            logger.info("Cold email generated successfully.")
            return email_content
        except Exception as e:
            logger.error(f"Error generating cold email: {e}")
            raise