
#  Expense Management System 

An efficient and modern **Expense Management System** designed with a responsive **Streamlit** frontend and a robust **FastAPI** backend. This project helps users track and analyze expenses seamlessly through a clean web interface backed by fast, scalable APIs.

---

##  Features

-  Add, edit, and delete expense entries
-  Visualize spending patterns through charts
-  Filter expenses by category, date, or amount
-  RESTful API for integration with other services
-  Secure backend with FastAPI

---

##  Tech Stack 

| Component | Technology      |
|----------:|-----------------|
| Frontend  | Streamlit       |
| Backend   | FastAPI         |
| Database  | MYSQL           |
| Language  | Python          |

---
Project Structure
Expense_Management/main/
│
├── database/  
├── frontend/
├── backend/             
├── tests/                
├── requirements.txt     
└── README.md            
---
##  Getting Started

### Prerequisites

- Python 3.9+
- `pip` (Python package installer)
---

##  Installation

### 1. Clone the Repository
```bash
git clone https://github.com/KaleSujit9011/Expense_Management.git
```
### 2. Virtual Environment Setup
```bash
python -m venv venv
source venv/bin/activate   # Unix/macOS
venv\Scripts\activate      # Windows
```
### 2.  Navigating to projrct Folder
```bash
cd Expense_Management/main
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 2.   Usage Section Backend
```bash
uvicorn backend.server:app --reload
```
### 2.   Usage Section Frontend
```bash
streamlit frontend.run .\app.py 
```
