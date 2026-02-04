# ai-file-robot
AI-powered CLI file automation tool using Python and OpenRouter
# 🤖 AI File Robot (CLI Based)

AI File Robot is a **command-line tool built with Python** that uses a **Large Language Model (LLM)** via **OpenRouter** to understand natural language commands and perform **real file system operations** like finding and organizing files.

This project demonstrates how **AI can control system-level automation** safely using structured command interpretation.

---

## 🚀 Features

- 🧠 Understands **natural language commands**
- 📂 Finds all PDF files from the system
- 🗂 Moves all PDFs into a single folder
- 💬 CLI-based interaction (terminal)
- 🔌 Uses **free LLM models** via OpenRouter
- 🛠 Modular Python backend

---

## 🧩 Example Commands

```text
find all pdf in c drive
ai-file-robot/
│
├── robot.py        # CLI entry point
├── ai_brain.py     # AI command interpreter (LLM integration)
├── file_ops.py     # File system operations
├── README.md       # Project documentation
└── .gitignore


pip install requests

setx OPENROUTER_API_KEY "your_api_key_here"

run:
python robot.py
Expected output:

🤖 AI File Robot is READY
Type 'exit' to quit
