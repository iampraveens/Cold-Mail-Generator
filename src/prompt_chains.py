from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from helper import GROQ_API_KEY

class PromptChain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            model="llama-3.1-70b-versatile",
            api_key=GROQ_API_KEY
        )

    def get_pdf_chain(self, pdf_text):
        prompt_pdf = PromptTemplate.from_template(
            """
            ### Resume Information Extraction

            Extract the following information from the provided resume text:

            - Name
            - Email
            - Skills
            - Projects

            Return the extracted information in a JSON format without any preamble.

            Extracted Text: {pdf_text}
            """
        )
        chain_pdf = prompt_pdf | self.llm
        result = chain_pdf.invoke(input={'pdf_text': pdf_text})
        return result.content

    def get_web_chain(self, web_text):
        prompt_web = PromptTemplate.from_template(
            """
            ### Job Posting Extraction

            Extract the following information from the provided job posting text:

            - Role
            - Experience
            - Skills
            - Description

            Return the extracted information in a JSON format without any preamble.

            Job Posting Text: {web_text}
            """
        )
        chain_web = prompt_web | self.llm
        result = chain_web.invoke(input={'web_text': web_text})
        return result.content

    def get_email_chain(self, job_description, resume_data):
        prompt_email = PromptTemplate.from_template(
            """
            ### Cold Email Generation

            Generate a cold email to the hiring manager based on the provided job posting and resume information.

            Use the following information to generate the email:

            Job Posting: {job_description}
            Resume Information: {resume_data}

            Write a persuasive email that highlights the candidate's skills and experience, and why they are the best fit for the job.

            Email should not include any preamble or the candidate's email address.

            Returns a well-structured email in plain text format.
            """
        )
        chain_email = prompt_email | self.llm
        result = chain_email.invoke(input={'job_description': job_description, 
                                           'resume_data': resume_data})
        return result.content
