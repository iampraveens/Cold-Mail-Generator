# Cold-Mail-Generator 📧🤖

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.1-orange)](https://python.langchain.com/)
[![LangChain_Community](https://img.shields.io/badge/LangChain_Community-0.3.2-orange)](https://python.langchain.com/)
[![LangChain_Groq](https://img.shields.io/badge/LangChain_Groq-0.2.0-orange)](https://python.langchain.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.39.0-red)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Cold-Mail-Generator is an advanced AI-powered tool designed to revolutionize the job application process. By leveraging the power of Large Language Models (LLMs) and natural language processing, it generates personalized cold emails for job seekers, increasing their chances of landing interviews and ultimately, their dream jobs.

## 🌟 Features

- 📄 **PDF Resume Parsing**: Extracts key information from your resume
- 🌐 **Job Posting Analysis**: Scrapes and analyzes job postings to understand requirements
- 🧠 **AI-Powered Email Generation**: Uses Groq's LLM to create tailored, persuasive emails
- 🖥️ **User-Friendly Interface**: Built with Streamlit for easy interaction
- 🔒 **Privacy-Focused**: Processes data locally, ensuring your information remains secure

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/iampraveens/Cold-Mail-Generator.git
   cd Cold-Mail-Generator
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   Create a `.env` file in the root directory and add your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## 🚀 Usage

1. **Start the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Upload your resume:**
   - Use the file uploader in the sidebar to upload your resume in PDF format.

3. **Enter job posting URL:**
   - Paste the URL of the job posting you're interested in into the chat input field.

4. **Generate your cold email:**
   - The app will process your resume and the job posting, then generate a personalized cold email.

5. **Review and customize:**
   - Read through the generated email and make any necessary adjustments to better suit your style and the specific job requirements.

## 🧩 Project Structure

```
Cold-Mail-Generator/
│
├── src/
│   ├── __init__.py
│   ├── pdf_handler.py
│   ├── web_handler.py
│   └── prompt_chains.py
│
├── utils/
│   ├── __init__.py
│   ├── utils.py
│   └── logger.py
│
├── main.py
├── app.py
├── html_template.py
├── requirements.txt
├── setup.py
├── template.py
├── .env
└── README.md
```

### Key Components

- **`src/pdf_handler.py`**: Manages PDF processing using PyPDF2 and LangChain's document loaders.
- **`src/web_handler.py`**: Handles web scraping of job postings using LangChain's WebBaseLoader.
- **`src/prompt_chains.py`**: Contains LLM prompt templates and chains for information extraction and email generation.
- **`main.py`**: Orchestrates the core application logic, connecting all components.
- **`app.py`**: Implements the Streamlit web application for user interaction.
- **`html_template.py`**: Defines styling and layout for the web interface.
- **`utils/dotenv_setup.py`**: Handles environment variable loading and provides utility functions used across the project.
- **`utils/logger.py`**: Configures logging for the entire application, ensuring comprehensive error tracking and debugging capabilities.

### Utility Modules

- **Environment Variable Management**: The `dotenv_setup.py` file uses `python-dotenv` to load environment variables, including the crucial GROQ_API_KEY for LLM integration. It ensures that all necessary configurations are properly set before the application runs.

- **Logging System**: The `logger.py` file sets up a robust logging system that writes logs to both a file and the console. It creates a new log file for each run of the application, making it easier to track issues and monitor performance over time.

These utility modules play a critical role in maintaining the application's stability, security, and debuggability. They exemplify best practices in Python application development by centralizing configuration management and establishing a comprehensive logging system.

## 💻 Technical Details

### PDF Processing
The `PDFHandler` class in `pdf_handler.py` uses PyPDF2 to extract text from resumes. It then employs LangChain's `RecursiveCharacterTextSplitter` to break the text into manageable chunks for processing.

### Web Scraping
The `WebHandler` class in `web_handler.py` utilizes LangChain's `WebBaseLoader` to fetch and parse job postings from provided URLs.

### LLM Integration
The `PromptChain` class in `prompt_chains.py` interfaces with Groq's LLM API through LangChain. It uses carefully crafted prompts to extract relevant information from resumes and job postings, and to generate personalized cold emails.

### User Interface
The Streamlit app in `app.py` provides an intuitive interface for users to upload resumes, input job posting URLs, and receive generated emails. It leverages Streamlit's file uploader and chat input components for seamless interaction.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/MIT) file for details.

## 🙏 Acknowledgements

- [LangChain](https://python.langchain.com/) for providing powerful language model tools
- [Streamlit](https://streamlit.io/) for the intuitive web application framework
- [Groq](https://groq.com/) for their advanced LLM API


Made with ❤️ by [Praveen S](https://github.com/iampraveens) | If you find this project helpful, please consider giving it a ⭐️!