from langchain_community.document_loaders import WebBaseLoader

class WebHandler:
    def __init__(self, url):
        self.url = url

    def get_web_text(self):
        loader = WebBaseLoader(web_path=self.url)
        self.pages_data = loader.load().pop().page_content
        return self.pages_data
