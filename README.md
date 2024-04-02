# CV Analysis Tool using Oobabooga API

This repository contains a Python script that uses the Oobabooga API to analyze CVs (Curriculum Vitaes) and extract relevant information. The tool reads PDF files from a specified directory, processes their content, and saves the results in a CSV file.

## Features
- Reads PDF files containing CVs
- Extracts textual data from each CV
- Uses the Ooba API to process the extracted text and answer predefined questions about the candidate's profile
- Saves the analysis results in a CSV file

## Requirements
To run the provided code, you need:
- A running instance of the Ooba API server at `http://127.0.0.1:5000/v1/completions` or update the URL in `ooba_api.py` accordingly.
- Python 3.x installed on your system
- The following libraries installed: requests, fitz (PyMuPDF)

You can install the required libraries by running:
```bash
pip install requests PyMuPDF
```

## How it works
The main logic is implemented in `main.py`. It lists all PDF files within a specific folder (`CVs/GV`), reads their contents using the `read_pdf()` function from `tools.py`, and sends them as prompts to the Ooba API for processing. The tool then extracts relevant information based on predefined questions stored in `questions.py`. Finally, the results are saved into a CSV file named "results.csv".

## Running the script
1. Make sure that the Ooba API server is up and running.
2. Place your CV files inside the `CVs/GV/` directory.
3. Run the `main.py` script with Python:
   ```bash
   python main.py
   ```
4. Check the generated "results.csv" file containing the analysis of each CV.

Feel free to modify the code according to your needs or contribute back to this project!
