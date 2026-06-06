# AI Legal Document Summarizer (Flask)

## Author / About
**Name:** Hafsa Noor
**University:** University of Layyah
**Department:** Information Technology
**Roll No.:** ULBSITMA 23_53
**Teacher:** Mr. Faisal Hafeez

**Demo video (Google Drive):** https://drive.google.com/file/d/1PCimzTi1vsLxdGuLP5W2tbRowkyx7F4Y/view?usp=drive_link


**Updated PPT:** Hafsa noor.ppt

**Legal Document Summarizer Report:** Legal_Document_Summarizer_Final_Report

Beginner-friendly web app that:


1. Uploads a PDF legal document
2. Extracts text using **PyPDF2**
3. Summarizes using **HuggingFace Transformers**
4. Shows the original text and the summary

## Project structure
- `app.py` - Flask app (PDF summarization + dataset testing)
- `requirements.txt` - Python dependencies
- `templates/` - HTML templates
- `static/` - CSS files
- `uploads/` - temporary uploaded PDFs (auto-deleted after summarization)
- `dataset/` - beginner dataset folder with sample `.txt` legal documents


## How to run
1) Create a virtual environment (recommended)

```bash
python -m venv venv
```

2) Activate it

- Windows (cmd):

```bash
venv\Scripts\activate
```

3) Install dependencies

```bash
pip install -r requirements.txt
```

4) Start Flask

```bash
python app.py
```

5) Open the browser at:
- http://127.0.0.1:5000

## Notes
- The first run downloads the model `facebook/bart-large-cnn`.
- Large PDFs may take time; we truncate text for summarization to avoid token limits.

## Dataset testing (beginner feature)
- Add your legal text as `.txt` files in `dataset/`
- Start the app, then open:
  - http://127.0.0.1:5000/dataset_test
- The app will summarize each dataset file and show the results in your browser.


