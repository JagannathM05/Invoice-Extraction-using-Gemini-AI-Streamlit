# 🧾 Invoice Extraction using Gemini AI & Streamlit

A Streamlit application that uses **Google's Gemini Vision model (`gemini-1.5-flash`)** to analyze invoice images and extract relevant information such as vendor name, total amount, date, invoice number, and more — all based on your custom prompt.

---

## 🚀 Features

- ✅ Upload `.jpg`, `.jpeg`, or `.png` invoice images
- ✅ Prompt-driven information extraction using multimodal AI
- ✅ Powered by Google's Gemini 1.5 Flash model
- ✅ Simple and elegant Streamlit UI

---

## 📂 Example Use Case

Enter a prompt like:

```

Extract the invoice number, total amount, and vendor name.

````

Upload your invoice image and receive a structured summary powered by Gemini Vision.

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Jagannath05/invoice-extraction-gemini.git
cd invoice-extraction-gemini
````

### 2. Create and activate virtual environment (optional)

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

---

## 🔐 API Key Setup

Make sure your **Google API key** is stored securely.

### Option 1: Create `.env` file

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### Option 2: Set environment variable

```bash
# On Windows PowerShell
$env:GOOGLE_API_KEY="your_gemini_api_key_here"
```

---

## ▶️ Run the App

```bash
streamlit run Invoice_extraction.py
```

---

## 📁 File Structure

```
.
├── Invoice_extraction.py    # Main Streamlit app
├── requirements.txt         # Dependencies
└── .env                     # API Key (ignored from Git)
```

---

## 📝 Requirements

Make sure `requirements.txt` contains:

```text
streamlit
google-generativeai
python-dotenv
Pillow
```

---



## 🙋 Author

**Jagannath Malode**
GitHub: [@JagannathM05](https://github.com/JagannathM05)

