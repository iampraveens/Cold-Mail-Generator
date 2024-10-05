from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils.logger import logger

class PDFHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        logger.info(f"PDFHandler initialized with file: {file_path}")

    def get_pdf_text(self):
        try:
            loader = PyPDFLoader(file_path=self.file_path)
            self.pages = loader.load()
            logger.info("PDF text loaded successfully.")
            return self.pages
        except Exception as e:
            logger.error(f"Error loading PDF text: {e}")
            raise

    def get_text_chunks(self, chunk_size=1500, chunk_overlap=200):
        try:
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=chunk_size, chunk_overlap=chunk_overlap,
                length_function=len, separators=['\n\n', '\n', ' ', '', '.', ',']
            )
            self.chunks = text_splitter.split_documents(self.pages)
            logger.info("PDF text split into chunks successfully.")
            return self.chunks
        except Exception as e:
            logger.error(f"Error splitting PDF text into chunks: {e}")
            raise

    def get_all_text(self):
        try:
            page_contents = [chunk.page_content for chunk in self.chunks]
            logger.info("All PDF text combined successfully.")
            return ' '.join(page_contents)
        except Exception as e:
            logger.error(f"Error combining PDF text: {e}")
            raise
