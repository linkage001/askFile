import csv
import os
import fitz

def read_pdf(file_path: str) -> str:
    text = ''
    if file_path.endswith('.pdf'):
        try:
            with open(file_path, 'rb') as pdf_file:
                # Open the PDF document
                doc = fitz.open(file_path)

                # Extract text from all pages
                text = ""
                for page in doc:
                    text += page.get_text()

        except Exception as e:
            print(f"Error occurred while processing {file_path}: {e}")

    elif os.path.isfile(file_path):
        print("{} is not a PDF file.".format(file_path))
    return text


def list_files_in_dir(directory: str) -> list[str]:
    file_names = os.listdir(directory)
    files = []

    for filename in file_names:
        files.append(os.path.join(directory, filename))
    return files

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