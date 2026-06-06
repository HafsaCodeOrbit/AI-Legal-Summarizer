# AI Legal Summarizer

A beginner-friendly Flask web app that uploads PDF legal documents, extracts text, and generates concise summaries for easy review.

## 🌟 Features
- Upload PDF legal documents for summarization
- Extract text from PDFs using `PyPDF2`
- Summarize using Hugging Face Transformer models
- Display both original text and generated summary in the browser
- Test summarization on local `.txt` dataset files

## 🛠 Technologies Used
- Python
- Flask
- PyPDF2
- Hugging Face Transformers
- HTML, CSS, JavaScript

## 📂 Project Structure
```
AI-Legal-Summarizer/
├── app.py
├── requirements.txt
├── README.md
├── dataset/
│   ├── README.md
│   ├── sample_1.txt
│   └── sample_2.txt
├── docs/
│   ├── AI Legal Summarizer Ppt.pptx
│   └── AI Legal Summarizer Report.pdf
├── templates/
│   ├── dataset_test.html
│   ├── index.html
│   └── result.html
├── static/
│   ├── styles.css
│   └── images/
├── uploads/
└── test_doc.txt
```

## 🚀 Installation
1. Clone the repository
```bash
git clone https://github.com/your-username/AI-Legal-Summarizer.git
```
2. Open the project folder
```bash
cd AI-Legal-Summarizer
```
3. Create a virtual environment
```bash
python -m venv venv
```
4. Activate the environment
```bash
venv\Scripts\activate
```
5. Install dependencies
```bash
pip install -r requirements.txt
```
6. Start the app
```bash
python app.py
```
7. Open the app in your browser
```text
http://127.0.0.1:5000
```

## 📸 Screenshots
*(Add screenshots here for the upload page, summary result page, and dataset test page.)*

## 🌐 Live Demo
No live demo available yet.

## 🔧 Configuration
- The app downloads the `facebook/bart-large-cnn` model on first run.
- Large PDFs may take longer to process.
- Uploaded files are stored in `uploads/` temporarily and removed after summarization.

## 📄 Downloadable Documents
Click a file name below to open or download it from the `docs/` folder:
- [AI Legal Summarizer Ppt.pptx](docs/AI%20Legal%20Summarizer%20Ppt.pptx)
- [AI Legal Summarizer Report.pdf](docs/AI%20Legal%20Summarizer%20Report.pdf)

If you run the app locally, these documents are also available via the web app download links in the sidebar.

## 🤝 Contributing
1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a pull request

## 📄 License
This project is licensed under the MIT License.

## 👩‍💻 Author
Hafsa Noor
- University of Layyah
- Department of Information Technology
- Email: noorhafsa164@gmail.com
- GitHub: [https://github.com/your-username](https://github.com/your-username)


