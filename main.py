from pdf_handler import PDFHandler
from web_handler import WebHandler
from prompt_chains import PromptChain

class JobApplicationAssistant:
    def __init__(self, pdf_path, job_posting_url):
        self.pdf_handler = PDFHandler(pdf_path)
        self.web_handler = WebHandler(job_posting_url)
        self.prompt_chain = PromptChain()

    def extract_resume_data(self):
        pages = self.pdf_handler.get_pdf_text()
        chunks = self.pdf_handler.get_text_chunks()
        pdf_text = self.pdf_handler.get_all_text()
        resume_data = self.prompt_chain.get_pdf_chain(pdf_text)
        return resume_data

    def extract_job_posting_data(self):
        web_text = self.web_handler.get_web_text()
        job_description = self.prompt_chain.get_web_chain(web_text)
        return job_description

    def generate_cold_email(self, job_description, resume_data):
        email_content = self.prompt_chain.get_email_chain(job_description, resume_data)
        return email_content

    # def run(self):
    #     resume_data = self.extract_resume_data()
    #     job_description = self.extract_job_posting_data()
    #     email_content = self.generate_cold_email(job_description, resume_data)
    #     print(email_content)
        
# pdf_path = "research/Praveen_S_CV.pdf"
# job_posting_url = "https://sarvm.freshteam.com/jobs/1uuNcm-EuTUd/ai-ml-intern-fresher-remote"

# assistant = JobApplicationAssistant(pdf_path, job_posting_url)
# assistant.run()