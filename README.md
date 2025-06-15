# Vaccination CRUD Application

## Task Overview

This project was developed as part of a task assignment for Python development at Younderbots.  
The objective was to build a CRUD web application to manage vaccination records with:

- Frontend using HTML templates.
- Backend using Python (FastAPI).
- Database integration using MySQL.
- ORM using SQLAlchemy.


## Tech Stack Used

- **Frontend:** HTML, CSS (Jinja2 Templates)
- **Backend:** Python (FastAPI)
- **Database:** MySQL
- **ORM:** SQLAlchemy
- **Web Server:** Uvicorn

---

## Project Features

- Add new vaccination records
- View all vaccination records
- Edit vaccination records
- Delete vaccination records

---

## Project Structure

Vaccination_CRUD/
│
├── main.py
├── database.py
├── requirements.txt
├── schema.sql
├── templates/
│ ├── index.html
│ └── edit.html
├── screenshots/
│ ├── add_record.png
│ ├── data_table.png
│ ├── Update_record.png
│ └── updated_table.png
└── README.md

---

## Setup Instructions

### 1️⃣ Clone Repository
git clone https://github.com/aashi984/Younderbots-TaskAssignment1_Updated.git

2️⃣ Install Required Packages
pip install -r requirements.txt

3️⃣ Database Setup
Create MySQL database:
CREATE DATABASE vaccination_data;
Note:
Tables will be created automatically when you run the app using SQLAlchemy models.
You can also refer to schema.sql for the database structure.

4️⃣ Database Configuration
Update your database credentials inside database.py file if needed:
DATABASE_URL = "mysql+pymysql://root:@127.0.0.1:3306/vaccination_data"

5️⃣ Run the Application
uvicorn main:app --reload
Open in browser:
http://127.0.0.1:8000/


## Screenshots

### ➡ Add Record Form
[Add Record](screenshots/add_record.png)

### ➡ Vaccination Records Table (Before Update)
[Data Table](screenshots/data_table.png)

### ➡ Edit Vaccination Record
[Edit Record](screenshots/Update_record.png)

### ➡ Vaccination Records Table (After Update)
[Updated Table](screenshots/updated_table.png)


