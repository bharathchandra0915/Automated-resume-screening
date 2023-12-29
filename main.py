import argparse
from PyPDF2 import PdfReader
from gpt import ask_chatgpt
# from inbuilt_pyresparser import ask_pyresparser
import json
import pandas as pd

ap = argparse.ArgumentParser()
ap.add_argument("-i", '--file_path', required= True, help= 'Path to the input image or pdf (pdf, jpg, png, jpeg)')
args = vars(ap.parse_args())
pdf_path = args['file_path']

extension =  pdf_path.split('.')[-1] 
fname = pdf_path.split('.')[0].split()[-1].split('\\')[-1]

def get_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    return text

def save_to_csv(parsed_data, fname):
    csv_file_path = f'{fname}.csv'
    df = pd.DataFrame()
    df['keys'] = [key for key in parsed_data.keys()]
    df['google_vision_gpt4'] = [parsed_data[key] for key in parsed_data.keys()]
    df.to_csv(csv_file_path)


text = get_text_from_pdf(pdf_path)
gpt_response= ask_chatgpt(text)
# print(gpt_response['response'])

json_data = gpt_response['response']
parsed_data = json.loads(json_data)
# for key in parsed_data.keys():
#     print(f'{key} :: {parsed_data[key]}')
save_to_csv(parsed_data, fname)
name = parsed_data['Name']
roles_list = parsed_data['Job Roles']
print(f'The job roles for which {name} is suitable for are {", ".join(roles_list)}')