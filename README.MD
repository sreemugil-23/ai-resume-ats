# 🧠 ATS Resume Analyzer (Industry-Style)

A **modular, explainable ATS-style resume evaluation system** that simulates how real Applicant Tracking Systems (ATS) screen resumes during hiring.

This project is intentionally designed to **mirror real-world ATS behavior**, prioritizing **consistency, transparency, and explainability** over black-box AI or hype-driven scoring.

---

## 🚀 Key Features

### ✅ Multiple ATS Evaluation Modes
The same resume can be evaluated using **three realistic ATS strategies**:

1. **Resume ATS Readiness (Resume-Only)**
   - Evaluates resume quality without job context  
   - Used as a *first-pass filter* by many ATS platforms  

2. **Resume vs Job Description**
   - Measures relevance using NLP similarity  
   - Simulates ATS keyword-based job matching  

3. **Resume vs Job Title**
   - Uses predefined role skill templates  
   - Approximates ATS behavior when only a job role is known  

---

## 📊 Resume ATS Readiness Scoring (Industry Standard)

Resume-only evaluation is based on **commonly used ATS heuristics**, not opaque AI predictions.

| Factor | Weight |
|------|--------|
| Section Structure | 25% |
| Keyword Presence | 25% |
| Resume Length | 15% |
| Skill Density | 15% |
| Formatting Simplicity | 10% |
| Contact Information | 10% |

> ⚠️ **Important:**  
> This score measures **ATS-friendliness**, not intelligence, talent, or job fit.

---

## 🧩 Clean, Modular Architecture

The project follows a **production-style, scalable architecture** with strict separation of concerns.

ai-resume-analyzer/
│
├── app.py # Streamlit UI (orchestration only)
│
├── core/
│ ├── pdf_parser.py # PDF → raw text extraction
│ ├── preprocessing.py # NLP text cleaning
│ ├── similarity.py # TF-IDF + cosine similarity
│ ├── skills.py # Rule-based skill matching
│ ├── ats_score.py # Weighted ATS scoring logic
│ └── resume_evaluator.py # Resume-only ATS evaluation
│
├── config/
│ └── roles.py # Job role → skill templates
│
├── requirements.txt
└── README.md

This structure allows:
- Independent evolution of modules  
- Easy replacement of scoring logic  
- Real-world maintainability  

---

## 🧠 How the System Works

### 1️⃣ Resume Parsing
- Extracts text from uploaded PDF resumes  
- Handles multi-page documents safely  

### 2️⃣ NLP Preprocessing
- Lowercasing  
- Symbol removal  
- Stopword filtering  
- Designed specifically for ATS-style keyword matching  

### 3️⃣ Scoring Logic
- **Resume-only**: heuristic ATS readiness scoring  
- **JD-based**: TF-IDF + cosine similarity  
- **JT-based**: role skill template → pseudo job description  

### 4️⃣ Explainable Output
- Final score (0–100)  
- Clear breakdown of contributing factors  
- User-facing explanations and warnings  

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (UI & hosting)
- **NLTK** (NLP preprocessing)
- **scikit-learn** (TF-IDF, cosine similarity)
- **pdfplumber** (PDF parsing)

✅ No paid APIs  
✅ No LLM dependency  
✅ Fully explainable logic  

---

## 🎯 Why This Project Stands Out

Most “AI resume analyzers”:
- Use opaque LLM outputs  
- Produce inconsistent scores  
- Are hard to explain or debug  

This project:
- Uses **deterministic, auditable logic**
- Mirrors **real ATS decision-making**
- Produces **stable, repeatable results**
- Can be confidently defended in technical interviews  

---

## ⚖️ Ethical Design Principles

- ATS scores are **filters**, not judgments  
- This system does **not** assess intelligence or capability  
- Human review is always required after automated screening  

---

## 📈 Example Use Cases

- Students testing ATS-friendliness of resumes  
- Understanding why resumes get filtered  
- Demonstrating NLP + system design skills  
- Educational exploration of ATS behavior  

---

## 🚧 Known Limitations

- Scanned or image-based PDFs may not parse correctly  
- Skill matching is rule-based (no semantic inference)  
- Job title matching uses predefined templates  

These limitations are **intentional** to preserve transparency.

---

## 🔮 Possible Extensions (Not Implemented)

- OCR detection for scanned resumes  
- Section-wise score visualization  
- Resume improvement suggestions  
- Embedding-based semantic matching  
- Resume ranking across multiple candidates  

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
