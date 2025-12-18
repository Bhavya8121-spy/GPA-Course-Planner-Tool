# Dallas College to UT Austin: CS Transfer Planner 🤘

A full-stack web application designed to help **Dallas College** students navigate the competitive transfer process into the **UT Austin Computer Science** program.

## Features
- **Real-time GPA Calculation:** Handles weighted credit hours and letter grades.
- **Course Mapping:** Automatically maps Dallas College (TCCNS) codes to UT Austin equivalents (e.g., COSC 1436 -> CS 312).
- **Academic Audit:** Tracks progress through core CS prerequisites.
- **Persistence:** Uses LocalStorage and Flask to manage session data.

## Tech Stack
- **Backend:** Python (Flask)
- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **Logic:** Object-Oriented Programming (OOP)

## Installation & Setup
1. Clone the repo: `git clone https://github.com/YOUR_USERNAME/Dallas-To-Longhorn-Planner.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`
4. View in browser: `http://127.0.0.1:5000`

## Technical Highlight
The backend utilizes a normalized lookup algorithm to bridge the gap between community college numbering systems and university-specific degree plans, ensuring 100% accuracy for transfer audits.