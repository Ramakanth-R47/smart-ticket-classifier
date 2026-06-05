# 🎫 Smart Ticket Classifier

A Python CLI tool that uses the **Anthropic Claude API** to automatically classify IT support tickets by category, priority, and recommended action — mimicking real-world ITSM triage workflows.

---

## 🚀 What It Does

Given a plain-text support ticket, the tool returns a structured analysis:

- **Category** — Network / Hardware / Software / Access / Other
- **Priority** — Low / Medium / High / Critical
- **Suggested Action** — Immediate response recommendation
- **Reasoning** — One-sentence explanation of the classification

---

## 📋 Sample Output

```
--- Ticket 1 ---
Input: I can't log into my email since this morning. I've tried resetting my password twice but it still says invalid credentials.

Classification:
Category: Access
Priority: High
Suggested Action: Verify account status in directory services and check for account lockouts or security blocks before requesting password reset through IT administrator.
Reasoning: Multiple failed login attempts combined with persistent invalid credentials suggests potential account lockout or security restriction requiring administrative intervention.
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Core language |
| Anthropic Claude API | LLM classification engine |
| python-dotenv | Secure API key management |
| Git / GitHub | Version control |

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Ramakanth-R47/smart-ticket-classifier.git
cd smart-ticket-classifier
```

### 2. Install dependencies
```bash
pip install anthropic python-dotenv
```

### 3. Configure your API key
Create a `.env` file in the project root:
```
ANTHROPIC_API_KEY=your_api_key_here
```
> Get your key at [console.anthropic.com](https://console.anthropic.com)

### 4. Run
```bash
python classifier.py
```

---

## 📁 Project Structure

```
smart-ticket-classifier/
├── classifier.py        # Main application script
├── .env                 # API key (not tracked by git)
├── .env.example         # Template for required environment variables
├── .gitignore           # Excludes .env from version control
└── README.md            # This file
```

---

## 🔒 Security

- API keys are stored in `.env` and excluded from version control via `.gitignore`
- No ticket data is logged or persisted — all processing is in-memory
- Never commit your `.env` file — use `.env.example` as a safe template

---

## 🔮 Future Enhancements

- [ ] Web UI via Flask or FastAPI
- [ ] CSV batch processing for bulk ticket classification
- [ ] ServiceNow REST API integration for automated ticket creation
- [ ] RAG layer using past tickets to improve accuracy
- [ ] Confidence scoring per classification
- [ ] Slack / Microsoft Teams bot integration

---

## 👤 Author

**Ramakanth Reddy Thimmaipally**
- 📧 ramakanthr47@gmail.com
- 🐙 [github.com/Ramakanth-R47](https://github.com/Ramakanth-R47)
- 📍 Hyderabad, India

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
