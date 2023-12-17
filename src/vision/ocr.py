import PyPDF2
import os

class PDFTextExtractor:
    def __init__(self, file_path, base_file):
        self.full_path = os.path.join(file_path, base_file)

    def extract_text_from_pdf(self):
        text_per_page = []

        with open(self.full_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            for page_number in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_number]
                text_per_page.append(page.extract_text())
                
            return {
               "text_per_page": [text.replace("\n", "") for text in text_per_page]
            }

