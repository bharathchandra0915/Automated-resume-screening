from resume_parser import resumeparse

def ask_resume_parser(pdf_path):
    data = resumeparse.read_file(pdf_path)
    return data
