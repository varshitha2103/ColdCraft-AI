# 📧 Cold Email A/B Testing Assistant (Ollama + Mistral 7B)

This project helps you generate and test two AI-written cold email variations (A and B) based on your product offer and lead type. It uses the open-source **Mistral 7B** model running locally via **Ollama**, ensuring full privacy and no API keys.

## ✨ Features

- 🔁 A/B email generation using variational prompting
- 🧠 Powered by Mistral 7B LLM (via Ollama)
- 🧾 Log email performance (Opened, Replied, Ignored)
- 📊 Basic performance analytics with pandas
- ⚡️ Runs 100% locally — no API key required

---

## 🛠 Tech Stack

| Component   | Tool                         |
|-------------|------------------------------|
| Language Model | [Mistral 7B](https://ollama.com/library/mistral) |
| Model Host  | [Ollama](https://ollama.com/) |
| Frontend    | Streamlit                    |
| Tracking    | pandas + CSV logging         |

---

## 🚀 Getting Started

### 1. Install [Ollama](https://ollama.com/)

Download and install Ollama for your OS.

Then pull the Mistral model:

```bash
ollama run mistral
```
### 2. Clone the Repo

```bash
git clone https://github.com/yourusername/cold-email-ab-ollama.git
cd cold-email-ab-ollama
```

### 3. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Run the Streamlit App
```bash
streamlit run app.py
```

📸 Screenshots

<img width="317" alt="output2" src="https://github.com/user-attachments/assets/cc529b8c-e1a4-4598-98a9-7223d2437a85" />

<img width="380" alt="image" src="https://github.com/user-attachments/assets/39d71096-dd8f-4625-a630-2fc13cf84e6e" />

🧠 Example Use Case
Offer: AI-powered resume writer

Lead Type: Tech recruiters at startups

The app generates:

✉️ Email A and Email B

You log whether each version was opened, replied to, or ignored

Results are stored and summarized in a table

📁 Project Structure
```bash
cold-email-ab-ollama/
├── app.py               # Streamlit UI
├── email_variants.py    # Mistral prompt handling
├── tracker.py           # CSV-based result logging
├── requirements.txt     # Project dependencies
└── README.md            # Documentation
```

💬 Questions?
```yaml
Would you like help:
- Generating a screenshot to include?
- Creating a GitHub repo + pushing it live?
- Adding features like charts or CSV download?
```





