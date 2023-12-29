from pyresparser import ResumeParser

def ask_pyresparser(pdf_path):
    data = ResumeParser(pdf_path).get_extracted_data()
    print(data)
