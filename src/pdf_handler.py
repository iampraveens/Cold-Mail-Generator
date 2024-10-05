from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class PDFHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_pdf_text(self):
        loader = PyPDFLoader(file_path=self.file_path)
        self.pages = loader.load()
        return self.pages

    def get_text_chunks(self, chunk_size=1500, chunk_overlap=200):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap,
            length_function=len, separators=['\n\n', '\n', ' ', '', '.', ',']
        )
        self.chunks = text_splitter.split_documents(self.pages)
        return self.chunks

    def get_all_text(self):
        page_contents = [chunk.page_content for chunk in self.chunks]
        return ' '.join(page_contents)
