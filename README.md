🚀 LifeLens AI
An AI-powered eligibility discovery platform that helps citizens find relevant government schemes based on their profile.

📌 Problem Statement
In India, millions of citizens are unaware of government schemes, scholarships, and subsidies they are eligible for.
Information is scattered, complex, and difficult to navigate.

💡 Solution
LifeLens AI simplifies scheme discovery by:

Collecting basic user details (income, state)

Matching eligibility conditions instantly

Displaying relevant schemes in real time

Providing a clean and simple interface

🛠️ Tech Stack
Backend: FastAPI (Python)

Frontend: HTML, CSS, JavaScript

Version Control: Git & GitHub

⚙️ How It Works
User enters:

Income

State

Backend processes eligibility rules

Matching schemes are returned instantly

🚀 Features
Real-time eligibility checking

Rule-based matching engine

Scalable backend architecture

Simple and user-friendly UI

🔮 Future Scope
ML-based eligibility prediction

Fuzzy matching for spelling errors

City-to-state auto detection

Document checklist generator

Multilingual support

Mobile app integration

📂 Project Structure
pgsql
Copy code
lifelens-ai/
│
├── app.py
├── index.html
└── README.md
▶️ How To Run Locally
Clone the repository:

bash
Copy code
git clone https://github.com/Supritam-005/lifelens-ai.git
Navigate to project folder:

bash
Copy code
cd lifelens-ai
Install dependencies:

nginx
Copy code
pip install fastapi uvicorn
Run the server:

lua
Copy code
python -m uvicorn app:app --reload
Open in browser:

cpp
Copy code
http://127.0.0.1:8000
