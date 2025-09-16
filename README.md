# LLUMO Assisment : Employee Management API – FastAPI + MongoDB- Junior SDE_Sahil_koshriya

This project is a **RESTful API** built with **FastAPI** and **MongoDB**, designed to manage employee data efficiently.  
It supports CRUD operations, querying, aggregation, and JWT authentication for security.  

---

📌 **Must Check:** The file **`LLUMO_Assingment_SAHIL110.pdf`** is included in this repository.  
   - It contains a detailed overview of the assignment and expected results.  
   - Please review it to understand the project requirements clearly before running the code. 

---


## 👨‍💻 About the Author

**Sahil Koshriya**  
🎓 NIT Sudent - Computer Application Program | 💡 Aspiring Software Engineer | ⚡ Passionate about Backend & Full-Stack Development  

I enjoy building **scalable applications** using **FastAPI, Django, React, and MongoDB**.  
Currently, I am exploring **cloud deployment (AWS/GCP)**, **data modeling**, and **system design** to grow as a well-rounded developer.  

📫 **Connect with me:**  
- GitHub: [SAHILKOSHRIYA](https://github.com/SAHILKOSHRIYA)  
- LinkedIn: [Sahil Koshriya](https://www.linkedin.com/in/sahil-koshriya/)  
- 7974426778
---

## 📌 Problem Statement
Managing employee data manually or through unstructured systems becomes inefficient as organizations grow.  
This API provides a structured way to:
- Store and manage employee records in MongoDB
- Perform CRUD operations
- Search/filter employees by department or skills
- Run aggregations (e.g., average salary per department)
- Secure sensitive operations with JWT authentication

---

## 🚀 Features
- **CRUD APIs**: Create, Read, Update, Delete employee records  
- **Query APIs**: By department, by skill  
- **Aggregation**: Average salary per department  
- **JWT Authentication**: Protects sensitive routes  
- **Enhancements**: Pagination, schema validation, MongoDB indexing  

---

## 📂 Database Details
- **Database:** `assessment_db`  
- **Collection:** `employees`

**Sample Document:**
```json
{
  "employee_id": "E123",
  "name": "John Doe",
  "department": "Engineering",
  "salary": 75000,
  "joining_date": "2023-01-15",
  "skills": ["Python", "MongoDB", "APIs"]
}
```
---

## 📂 Project Directory Structure

```bash
LLUMO_FastAPI_MongoDB_Assingment110/
│── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI entrypoint
│   ├── db.py                # MongoDB connection
│   ├── auth.py              # JWT authentication helpers
│   ├── models.py            # Converters, utility functions
│   ├── schemas.py           # Pydantic models
│   │
│   ├── routers/             # API routers
│   │   ├── __init__.py
│   │   ├── auth_routes.py   # Auth endpoints
│   │   └── employees.py     # Employee CRUD + query APIs
│
│── tests/                   # (optional) test cases
│
│── .env                     # Environment variables (MONGO_URI, DB_NAME, SECRET_KEY)
│── .DS_Store                # System file (ignored in .gitignore)
│── requirements.txt         # Dependencies
│── README.md                # Documentation
│── LLUMO_Assingment_SAHIL110.pdf   # Assignment PDF
│── EmployeeAPI.postman_collection.json   # Postman collection

```

---
## 🛠️ Setup

### 1. Clone Repository
```bash
git clone https://github.com/SAHILKOSHRIYA/LLUMO_FastAPI_MongoDB_Assingment110.git
cd LLUMO_FastAPI_MongoDB_Assingment110
```
### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
---
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Setup MongoDB
- Install **MongoDB Community Edition**  
- Start MongoDB locally:
```bash
mongod
```
### 5. Start FastAPI Server
```bash
uvicorn app.main:app --reload
```
### 6. Access API Docs
- Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- ReDoc UI → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  
---
## 📌 Core CRUD APIs

### 1. Create Employee
- **POST** `/employees`  
- Insert new employee  
- Validate `employee_id` uniqueness  

### 2. Get Employee by ID
- **GET** `/employees/{employee_id}`  
- Fetch employee details  
- Returns **404** if not found  

### 3. Update Employee
- **PUT** `/employees/{employee_id}`  
- Update employee fields  
- Supports **partial updates**  

### 4. Delete Employee
- **DELETE** `/employees/{employee_id}`  
- Delete employee record  
- Returns success/failure message  

---

## 📊 Querying & Aggregation APIs

### 5. List Employees by Department
- **GET** `/employees?department=Engineering`  
- Returns employees in department  
- Sorted by `joining_date` (newest first)  

### 6. Average Salary by Department
- **GET** `/employees/avg-salary`  
- Uses **MongoDB aggregation**  

**Example Response:**
```json
[
  {"department": "Engineering", "avg_salary": 80000},
  {"department": "HR", "avg_salary": 60000}
]
```
---
### 🔑 Authentication
- **POST** `/auth/register` → Register new user  
- **POST** `/auth/login` → Get JWT token  
(Use the returned JWT as `Authorization: Bearer <token>` for protected routes)

### 👨‍💼 Employees
- **POST** `/employees` → Create new employee  
- **GET** `/employees/{employee_id}` → Get employee by ID  
- **PUT** `/employees/{employee_id}` → Update employee (partial updates allowed)  
- **DELETE** `/employees/{employee_id}` → Delete employee  
- **GET** `/employees?department=Engineering` → List by department (sorted by joining_date DESC)  
- **GET** `/employees/avg-salary` → Average salary by department (aggregation)  
- **GET** `/employees/search?skill=Python` → Search by skill  

---

## 🎯 Bonus Features
- ✅ JWT authentication for security  
- ✅ MongoDB index on `employee_id`  
- 🚧 Pagination for listing  
- 🚧 Schema validation with MongoDB JSON Schema  

---

## 🔮 Future Work
- Dockerized deployment (API + MongoDB container)  
- Role-based access control (RBAC) for Admins/Managers  
- GraphQL API for flexible querying  
- Frontend dashboard (React/Angular)  
- CI/CD pipeline + cloud deployment (AWS/GCP/Azure)  

---

## 📂 Postman Collection
A **Postman collection** is included for quick testing:  
`EmployeeAPI.postman_collection.json`


---

## 🙏 Thank You
Thank you for reviewing this project! 🚀  
Feedback and suggestions are always welcome.  

