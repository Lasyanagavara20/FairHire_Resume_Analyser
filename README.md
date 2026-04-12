# FairHire – AI Resume Analyzer  

🔗 **Live Application:** [FairHire Resume Analyzer](https://fairhire-resume-analyser-1.onrender.com/)  

---

## 📌 Project Overview  
FairHire is an AI-powered web application that evaluates how well a candidate’s resume matches a job description. The system processes resumes, applies NLP techniques to measure semantic similarity, and performs skill-based analysis to generate a comprehensive match score along with actionable feedback.

The application is fully deployed and enables real-time resume evaluation through a web interface.

---

## 🎯 Objectives  
- Analyze resumes against job descriptions  
- Identify semantic similarity using NLP techniques  
- Extract and compare technical skills  
- Generate a hybrid evaluation score  
- Provide actionable feedback for improvement  

---

## 🧱 System Architecture  

```text
+-------------------------------+
|        User Input             |
| (Resume + Job Description)    |
+---------------+---------------+
                |
                v
+-------------------------------+
|       Resume Parsing          |
|   (PDF / DOCX Extraction)     |
+---------------+---------------+
                |
                v
+-------------------------------+
|      Text Preprocessing       |
| (Cleaning, Normalization)     |
+---------------+---------------+
                |
                v
+-------------------------------+
|   Semantic Similarity Module  |
|  (TF-IDF + Cosine Similarity) |
+---------------+---------------+
                |
                v
+-------------------------------+
|     Skill Matching Module     |
| (Skill Extraction & Compare)  |
+---------------+---------------+
                |
                v
+-------------------------------+
|     Hybrid Scoring Engine     |
| (0.7 Semantic + 0.3 Skill)    |
+---------------+---------------+
                |
                v
+-------------------------------+
| Explanation & Suggestions     |
+---------------+---------------+
                |
                v
+-------------------------------+
|        Web Interface          |
+-------------------------------+
```
---

## 🖥️ Frontend  
- Built using **HTML**  
- Simple and user-friendly interface  
- Supports resume upload and job role selection  
- Displays:
  - Match score  
  - Matched skills  
  - Missing skills  
  - Suggestions  
- Includes dark mode support  

---

## ⚙️ Backend  
- Developed using **Flask (Python)**  
- Handles:
  - File uploads (PDF, DOCX)  
  - Resume parsing  
  - Text preprocessing  
  - Similarity computation  
  - Skill extraction and comparison  
  - Score calculation and response generation  

---

## 🗂️ Dataset  
This project does not use a traditional training dataset.

Instead, it relies on:
- Predefined job descriptions (`common_jds.py`)  
- Curated technical skill database (`skills_db.py`)  
- User-uploaded resumes (runtime input)  

---

## 🛠️ Technologies Used  

### Languages  
- Python  
- HTML  

### Libraries  
- scikit-learn (TF-IDF, cosine similarity)  
- PyMuPDF (PDF parsing)  
- python-docx (DOCX parsing)  

### Framework  
- Flask  

### Deployment  
- Render  
- Gunicorn  

---

## ⚙️ Algorithms and Methodology  

### 1. Text Preprocessing  
- Lowercasing  
- Removing punctuation  
- Removing extra spaces  

---

### 2. TF-IDF (Term Frequency–Inverse Document Frequency)  

TF-IDF(t, d) = TF(t, d) × IDF(t)  

IDF(t) = log(N / df(t))  

Where:  
- t = term  
- d = document  
- N = total number of documents  
- df(t) = number of documents containing term t  

---

### 3. Cosine Similarity  

Similarity(A, B) = (A · B) / (||A|| × ||B||)  

Where:  
- A = resume vector  
- B = job description vector  

---

### 4. Skill Matching  

Matched Skills = Resume Skills ∩ Job Description Skills  

Missing Skills = Job Description Skills − Resume Skills  

---

### 5. Skill Score  

Skill Score = Matched Skills / (Matched Skills + Missing Skills)  

---

### 6. Hybrid Scoring  

Final Score = (0.7 × Semantic Similarity) + (0.3 × Skill Score)  

Final Score (%) = Final Score × 100  

---

## 📊 Features  
- Resume upload (PDF, DOCX)  
- Automatic text extraction  
- Semantic similarity computation  
- Skill extraction and comparison  
- Hybrid scoring system  
- Explainable results  
- Web-based real-time analysis  

---

## 🌐 Deployment  

The application is deployed on Render and accessible online.

🔗 **Live URL:**  
https://fairhire-resume-analyser-1.onrender.com/

---

## 📈 Output  

The system provides:  
- Resume match score  
- Matched skills  
- Missing skills  
- Explanation of evaluation  
- Suggestions for improvement  

---

## 📂 Project Structure  

```text
FairHire_Resume_Analyser/
│
├── app.py                     # Main Flask application
├── resume_parser.py           # Extract text from PDF/DOCX
├── preprocess.py              # Text cleaning and preprocessing
├── similarity.py              # TF-IDF and cosine similarity
├── skills_matcher.py          # Skill extraction and comparison
├── skills_db.py               # Predefined technical skills list
├── common_jds.py              # Predefined job descriptions
├── explainability.py          # Generate explanations & suggestions
│
├── templates/
│   └── index.html             # Frontend UI
│
├── requirements.txt           # Dependencies
├── runtime.txt                # Python version (Render)
├── Procfile                   # Deployment configuration
│
└── README.md                  # Project documentation
```
---

## 📌 Use Cases  
- Resume optimization for job seekers  
- Initial resume screening for recruiters  
- NLP-based academic project demonstration  

---

## 📌 Summary  
FairHire demonstrates how NLP techniques can be applied to evaluate resume-job fit by combining semantic similarity and skill-based analysis, providing a structured and explainable evaluation system.
