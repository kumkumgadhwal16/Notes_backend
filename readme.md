# 📝 Notes App API

A REST API backend for managing personal notes, built using **FastAPI and PostgreSQL**.

Users can register, log in, and manage their own notes securely using JWT authentication.

## 🚀 Features

- User Registration
- User Login with JWT Authentication
- Secure Password Hashing
- Create a Note
- View All Your Notes
- View a Single Note
- Update a Note
- Delete a Note
- Users can access only their own notes
- Interactive API Documentation using Swagger UI

## 🛠️ Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- PyJWT
- Argon2 Password Hashing
- Uvicorn

## 📁 Project Structure

```text
Notes_backend/
│
├── app/
│   ├── routers/
│   │   ├── auth.py
│   │   └── notes.py
│   │
│   ├── __init__.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── security.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 💻 Installation and Setup

Follow these steps to run the project on your computer.

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/kumkumgadhwal16/Notes_backend.git
```

### 2. Open the Project Folder

```bash
cd Notes_backend
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a PostgreSQL Database

Open pgAdmin or PostgreSQL and create a database named:

```text
notes_db
```

### 6. Configure Environment Variables

Create a file named `.env` in the project root folder.

Add your own database details and JWT secret:

```env
DATABASE_URL=postgresql+psycopg://YOUR_DB_USER:YOUR_DB_PASSWORD@localhost:5432/notes_db

JWT_SECRET_KEY=YOUR_PRIVATE_SECRET_KEY
```

Replace the example values with your own credentials.

**Important:** Never upload your actual `.env` file, database password, or JWT secret to GitHub.

### 7. Run the Application

```bash
uvicorn app.main:app --reload
```

## 🌐 API Documentation

After starting the server, open these links in your browser:

| Page | URL |
|---|---|
| Health Check | http://127.0.0.1:8000/ |
| Swagger UI | http://127.0.0.1:8000/docs |
| OpenAPI Schema | http://127.0.0.1:8000/openapi.json |

## 📌 API Endpoints

All Notes endpoints require JWT authentication.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and get access token |
| POST | `/notes` | Create a note |
| GET | `/notes` | Get all your notes |
| GET | `/notes/{note_id}` | Get a note by ID |
| PATCH | `/notes/{note_id}` | Update a note |
| DELETE | `/notes/{note_id}` | Delete a note |

## 🧪 How to Test the API

1. Start the application.
2. Open Swagger UI: `http://127.0.0.1:8000/docs`
3. Register a new user using `/auth/register`.
4. Login using `/auth/login`.
5. Copy the `access_token` from the response.
6. Click the **Authorize** button and enter your token as requested.
7. Test the Notes APIs.

### Example: Create a Note

Send a POST request to `/notes`:

```json
{
  "title": "My First Note",
  "content": "I am learning FastAPI."
}
```

### Example: Update a Note

Send a PATCH request to `/notes/{note_id}`:

```json
{
  "title": "Updated Note"
}
```

## 🔐 Security

- Passwords are stored as hashed values.
- JWT authentication protects Notes endpoints.
- Users can access only their own notes.
- Environment variables are used for private credentials.
- Access tokens expire after 30 minutes.

## 🔮 Future Improvements

- Frontend using React or Flutter
- Automated API testing with Pytest
- Alembic database migrations
- Docker support
- Cloud deployment
- Improved production logging and security

## 👩‍💻 Author

**Kumkum Gadhwal**

GitHub: https://github.com/kumkumgadhwal16

---

⭐ If you find this project useful, feel free to explore the repository!