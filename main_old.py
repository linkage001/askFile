import os
from PyPDF2 import PdfReader
import fitz
import requests
import csv

source = 'CVs/Contabilista'  # Replace with your desired path
output = 'output/Contabilista'

def save_to_csv(data_list, filename):
    # Get the keys from the first dictionary (assuming all dictionaries have the same keys)
    keys = data_list[0].keys()

    # Open the CSV file for writing
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)

        # Write the header row
        writer.writeheader()

        # Iterate through the data and write each row
        for item in data_list:
            writer.writerow(item)
def completion(text, max_tokens=30):

    url = "http://127.0.0.1:5000/v1/completions"
    prompt = text
    data = {
        "prompt": prompt,
        "max_tokens": max_tokens
    }

    response = requests.post(url, json=data)
    completion = ''
    if response.status_code == 200:
        completions = response.json()['choices']
        # print(f"Generated completions:")
        for c in completions:
            completion = c['text']
    else:
        print(f"Error occurred: {response.text}")
    return completion

def translate(text):
    # Set up the API endpoint and headers
    endpoint = "http://127.0.0.1:5000/v1/chat/completions"
    headers = {"Content-Type": "application/json"}

    # Create the data payload
    data = {
        "messages": [
            {"role": "system",
             "content": "You are a helpful assistant that translates text from Portuguese to English."},
            {"role": "user", "content": text + '\n\nTranslate the text above to English'}
        ],
        "max_tokens": 4096,
    }

    # Make the API request and parse the response
    response = requests.post(endpoint, headers=headers, json=data)
    response_dict = response.json()
    translation = response_dict["choices"][0]["message"]["content"]
    return translation


def save_text_files_with_pdf_content(directory):
    # List all files (not directories) in a specified directory
    file_names = os.listdir(directory)

    for filename in file_names:
        file_path = os.path.join(directory, filename)

        if filename.endswith('.pdf'):
            try:
                with open(file_path, 'rb') as pdf_file:
                    # Open the PDF document
                    doc = fitz.open(file_path)

                    # Extract text from all pages
                    text = ""
                    for page in doc:
                        text += page.get_text()
                    text = translate(text)
                    print(text)

                    # reader = PdfReader(pdf_file)
                    # num_pages = len(reader.pages)

                    # Create a new text file for each PDF
                    txt_filename = os.path.splitext(filename)[0] + '.txt'
                    txt_file_path = os.path.join(output, txt_filename)

                    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
                        txt_file.write(text)

            except Exception as e:
                print(f"Error occurred while processing {file_path}: {e}")

        elif os.path.isfile(file_path):
            print("{} is not a PDF file.".format(filename))

import os

def get_files_in_folder(folder):
   """
   This function takes a folder path as input and returns a list of all file paths within that folder.
   :param folder: str, path to the folder.
   :return: list of strings, each string is a full path to a file in the folder.
   """
   # Use os.listdir to get all entries in the folder (both files and directories)
   entries = os.listdir(folder)

   # Filter out directories and only keep files
   files = [entry for entry in entries if not os.path.isdir(os.path.join(folder, entry))]

   # Construct full file paths
   file_paths = [os.path.join(folder, file) for file in files]

   return file_paths


if __name__ == '__main__':
    # if os.path.exists(source) and os.access(source, os.R_OK):
    #     save_text_files_with_pdf_content(source)
    # else:
    #     print(f"The provided folder ({source}) does not exist or you don't have permission to access it.")
    folder = "output/Contabilista"
    results = []
    file_paths = get_files_in_folder(folder)
    for file in file_paths:
        with open(file, mode='r', encoding='utf-8') as f:
            data = f.read()
            name = file.split('/')[-1].split('.')[0]
            name = name.replace('-cv', '').replace('-', ' ').replace('  ', ' ').strip()

            question = """Choose the option that best describes the candidate's situation:

<a> Complete elementary education

<b> Complete secondary education

<c> Complete technical education

<d> Complete higher education

<e> Complete postgraduate education"""
        education = completion(f'{data} \n{question}\n\nAssistant: <', 1)

        question = """"Please choose the option that best describes your years of experience working in Accounting:

<a> Less than 1 year

<b> 1-3 years

<c> 3-5 years

<d> 5-10 years

<e> Over 10 years"""
        experience_a = completion(f'{data} \n{question}\n\nAssistant: <', 1)

        question = """"Please choose the option that best describes your years of experience working in Accounting:

        <a> Less than 1 year

        <b> 1-3 years

        <c> 3-5 years

        <d> 5-10 years

        <e> Over 10 years"""
        experience_c = completion(f'{data} \n{question}\n\nAssistant: <', 1)

        question = """"What is the probable age of the person described above?

Assistant: The probable age of the person is """
        age = completion(f'{data} \n{question}', 2)

        print(data)
        print('===============')
        print(education)
        print(experience_a)
        print(experience_c)
        print(age)
        options = {
            'a': 'Less than 1 year',
            'b': '1-3 years',
            'c': '3-5 years',
            'd': '5-10 years',
            'e': 'Over 10 years'
        }
        options_education = {
            'a': 'Complete elementary education',
            'b': 'Complete secondary education',
            'c': 'Complete technical education',
            'd': 'Complete higher education',
            'e': 'Complete postgraduate education'
        }
        try:
            education = options_education[education]
        except Exception:
            education = 'unknown'

        try:
            experience_a = options[experience_a]
        except Exception:
            experience_a = 'unknown'

        try:
            experience_c = options[experience_c]
        except Exception:
            experience_c = 'unknown'

        item = {
            "name": name,
            "Education": education,
            "Experience Accounting": experience_a,
            "Experience Consulting": experience_c,
            "Age": age,
        }
        results.append(item)
    save_to_csv(results, "results.csv")
