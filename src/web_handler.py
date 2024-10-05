from langchain_community.document_loaders import WebBaseLoader
from utils.logger import logger

class WebHandler:
    def __init__(self, url):
        self.url = url
        logger.info(f"WebHandler initialized with URL: {url}")

    def get_web_text(self):
        try:
            loader = WebBaseLoader(web_path=self.url)
            pages_data = loader.load().pop().page_content
            logger.info("Web text loaded successfully.")
            return pages_data
        except Exception as e:
            logger.error(f"Error loading web text: {e}")
            raise
